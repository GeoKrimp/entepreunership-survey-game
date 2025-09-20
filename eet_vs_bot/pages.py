# eet_vs_bot/pages.py
from otree.api import Page
from .models import C, ensure_payoff_tables
import json, random


class Instructions(Page):
    def vars_for_template(self):
        return dict(n=C.N, equal=C.EQUAL_PAYOFF)


class Decision(Page):  # ΠΡΟΣΟΧΗ: Page, ΟΧΙ Player
    form_model = 'player'
    form_fields = ['decisions_json']  # γεμίζει από το JS του template

    def vars_for_template(self):
        ensure_payoff_tables(self.session)  # safety

        mp_x = self.session.vars['mp_x']; op_x = self.session.vars['op_x']
        mp_y = self.session.vars['mp_y']; op_y = self.session.vars['op_y']
        eq   = self.session.vars['equal']

        rows_x = [dict(i=i, left_me=mp_x[i], left_other=op_x[i], right_me=eq, right_other=eq) for i in range(C.N)]
        rows_y = [dict(i=i, left_me=mp_y[i], left_other=op_y[i], right_me=eq, right_other=eq) for i in range(C.N)]

        return dict(rows_x=rows_x, rows_y=rows_y, progress=100, step=1, steps_total=1)

    def error_message(self, values):
        try:
            data = json.loads(values.get('decisions_json') or '{}')
            if len(data.get('x', [])) != C.N or len(data.get('y', [])) != C.N:
                return "Please make a choice in every row of both lists."
            if any(c not in ('L', 'R') for c in data['x'] + data['y']):
                return "Invalid choices found."
        except Exception:
            return "Please make a choice in every row."

    def before_next_page(self, timeout_happened=False):
        # support both call styles: Page instance (has .player) OR Player instance (rare misbinding)
        player = getattr(self, 'player', self)
        session = getattr(self, 'session', getattr(player, 'session', None))

        # ------- choices του παίκτη από το JSON -------
        import json, random
        data = json.loads((getattr(player, 'decisions_json', '') or '{}'))
        you_x = (data.get('x', [])[:C.N] + [''] * C.N)[:C.N]
        you_y = (data.get('y', [])[:C.N] + [''] * C.N)[:C.N]
        choices_you = {'x': you_x, 'y': you_y}

        # ------- choices του bot -------
        choices_bot = player.bot_choices()

        # ------- ποιανού υλοποιούνται -------
        player.implemented_by = 'you' if random.random() < C.IMPLEMENT_YOU_PROB else 'computer'

        # ------- κλήρωση λίστας/γραμμής -------
        idx = random.randrange(C.N * 2)
        list_kind = 'x' if idx < C.N else 'y'
        row = idx if list_kind == 'x' else (idx - C.N)
        player.implemented_list = list_kind
        player.implemented_row = row

        # ------- επιλεγμένη κίνηση (L/R) -------
        choice = (choices_you if player.implemented_by == 'you' else choices_bot)[list_kind][row]

        # ------- payoffs -------
        # (πάρε τα tables από το session – αν λείπουν, κάλεσε τον helper)
        from .models import ensure_payoff_tables
        ensure_payoff_tables(player.session if session is None else session)
        mp = player.session.vars['mp_x'][row] if list_kind == 'x' else player.session.vars['mp_y'][row]
        op = player.session.vars['op_x'][row] if list_kind == 'x' else player.session.vars['op_y'][row]
        if choice == 'L':
            you, other = mp, op
        else:
            eq = player.session.vars['equal']
            you, other = eq, eq

        player.payoff_you_realized = you
        player.payoff_other_realized = other
        player.payoff = you


class Results(Page):
    def is_displayed(self):
        return True  # βάλε False αν δεν θέλεις εμφάνιση

    def vars_for_template(self):
        # safety: δούλεψε είτε self είναι Page (έχει .player) είτε Player (fallback)
        player = getattr(self, 'player', self)

        return dict(
            implemented_by=player.implemented_by,
            list_kind=(player.implemented_list or '').upper(),
            row=(player.implemented_row or 0) + 1,
            you=player.payoff_you_realized,
            other=player.payoff_other_realized,
        )



page_sequence = [Instructions, Decision, Results]
