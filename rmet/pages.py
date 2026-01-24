from otree.api import *
from .models import C, Subsession, Group, Player

class Instructions(Page):
    def is_displayed(self):
        # Αν το RMET έχει μόνο 1 round αυτό απλά είναι πάντα True,
        # αλλά είναι καλή πρακτική να το περιορίζουμε στον 1ο γύρο.
        return self.round_number == 1

class AllItems(Page):
    form_model = 'player'

    def get_form_fields(self):
        # Τα ονόματα των πεδίων τα έβαλε το creating_session() στο session
        return self.session.vars['resp_fields']

    def vars_for_template(self):
        items = []
        for it in self.player.items():
            options = [
                {'val': i, 'label': lbl, 'required': (i == 1)}  # required μόνο στην 1η επιλογή κάθε ομάδας
                for i, lbl in enumerate(it['options'], start=1)
            ]
            items.append(dict(
                path=f"rmet/images/{it['image']}",  # ενιαίο path για το {% static %}
                field=it['field'],
                options=options,
            ))
        return dict(items=items, total=len(items))

    def before_next_page(self):  # <-- ΧΩΡΙΣ timeout_happened
        total = 0
        for it in self.player.items():
            resp = getattr(self.player, it['field'])
            if resp == it['correct']:
                total += 1
        self.player.score_total = total

page_sequence = [Instructions, AllItems]
