from otree.api import *
import random, json


class C(BaseConstants):
    NAME_IN_URL = 'eet_vs_bot'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Πλήθος γραμμών σε κάθε λίστα (X και Y)
    N = 12

    # Δεξιά επιλογή: ίσα payoffs (you=other)
    EQUAL_PAYOFF = cu(10)

    # Αριστερή επιλογή (unequal) – demo γραμμική κλίση (άλλαξέ τα αν θέλεις)
    MP_X_START, MP_X_END = 2, 20   # main player (X list)
    OP_X_START, OP_X_END = 18, 0   # other      (X list)

    MP_Y_START, MP_Y_END = 2, 20   # main player (Y list)
    OP_Y_START, OP_Y_END = 2, 20   # other       (Y list)

    # Πιθανότητα να υλοποιηθούν οι επιλογές του παίκτη (vs του bot)
    IMPLEMENT_YOU_PROB = 0.5


def _linspace_int(a, b, k):
    if k == 1:
        return [a]
    step = (b - a) / (k - 1)
    return [round(a + i * step) for i in range(k)]


def ensure_payoff_tables(session):
    """
    Φτιάχνει τα mp_x/op_x/mp_y/op_y/equal στο session.vars αν λείπουν.
    Έτσι αποφεύγουμε KeyError ακόμη κι αν δεν εκτελέστηκε creating_session.
    """
    if 'mp_x' in session.vars:
        return

    n = C.N
    mp_x = [cu(x) for x in _linspace_int(C.MP_X_START, C.MP_X_END, n)]
    op_x = [cu(x) for x in _linspace_int(C.OP_X_START, C.OP_X_END, n)]
    mp_y = [cu(x) for x in _linspace_int(C.MP_Y_START, C.MP_Y_END, n)]
    op_y = [cu(x) for x in _linspace_int(C.OP_Y_START, C.OP_Y_END, n)]

    session.vars['mp_x'] = mp_x
    session.vars['op_x'] = op_x
    session.vars['mp_y'] = mp_y
    session.vars['op_y'] = op_y
    session.vars['equal'] = C.EQUAL_PAYOFF


class Subsession(BaseSubsession):
    def creating_session(self):
        # Payoff tables
        ensure_payoff_tables(self.session)
        # Bot switching points (σταθερά ανά participant)
        for p in self.get_players():
            p.participant.vars['bot_switch_x'] = random.randint(1, C.N)  # 1..N
            p.participant.vars['bot_switch_y'] = random.randint(1, C.N)  # 1..N


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Όλες οι επιλογές του παίκτη σε ένα JSON (για καθαρή ΒΔ)
    # decisions_json = {"x": ["L"/"R", ... length N], "y": ["L"/"R", ... length N]}
    decisions_json = models.LongStringField(blank=True)

    # Αποτελέσματα υλοποίησης (κλήρωση)
    implemented_by = models.StringField()      # 'you' | 'computer'
    implemented_list = models.StringField()    # 'x' | 'y'
    implemented_row = models.IntegerField()    # 0..N-1
    payoff_you_realized = models.CurrencyField(initial=0)
    payoff_other_realized = models.CurrencyField(initial=0)

    # ------------ Helpers ------------
    def bot_choices(self):
        """Παράγει τις επιλογές του bot με βάση τα switching points σε X & Y."""
        n = C.N
        sx = self.participant.vars.get('bot_switch_x', (n + 1) // 2)
        sy = self.participant.vars.get('bot_switch_y', (n + 1) // 2)
        bot_x = ['R' if (i + 1) < sx else 'L' for i in range(n)]
        bot_y = ['R' if (i + 1) < sy else 'L' for i in range(n)]
        return {'x': bot_x, 'y': bot_y}

    def parse_player_choices(self):
        """Διαβάζει self.decisions_json και επιστρέφει {'x':[...], 'y':[...]} μήκους N."""
        try:
            data = json.loads(self.decisions_json or '{}')
            x = data.get('x', [])[:C.N]
            y = data.get('y', [])[:C.N]
            x = [(s if s in ('L', 'R') else '') for s in x]
            y = [(s if s in ('L', 'R') else '') for s in y]
            if len(x) < C.N: x += [''] * (C.N - len(x))
            if len(y) < C.N: y += [''] * (C.N - len(y))
            return {'x': x, 'y': y}
        except Exception:
            return {'x': [''] * C.N, 'y': [''] * C.N}
