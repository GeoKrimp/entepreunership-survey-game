# investment_bot/pages.py
from otree.api import *
from .models import C, Subsession, Group, Player


class Instructions(Page):
    def vars_for_template(player: Player):
        return dict(
            endowment_eur=float(C.ENDOWMENT),
            multiplier=C.MULTIPLIER,
        )


class Decision(Page):
    form_model = 'player'
    form_fields = ['sent_amount']

    def vars_for_template(player: Player):
        return dict(
            endowment_eur=float(C.ENDOWMENT),
            multiplier=C.MULTIPLIER,
        )

    # ΠΡΟΣΟΧΗ: εδώ ΔΕΝ υπάρχει self, υπάρχει player
    def before_next_page(player: Player, timeout_happened=False):
        player.set_payoffs()


class Results(Page):
    def vars_for_template(player: Player):
        sent = player.sent_amount or cu(0)
        tripled = sent * C.MULTIPLIER

        return dict(
            endowment_eur=float(C.ENDOWMENT),
            sent=sent,
            tripled=tripled,
            returned=player.returned_amount,
            your_payoff=player.payoff,
            bot_payoff=player.bot_payoff,
            multiplier=C.MULTIPLIER,
        )


page_sequence = [Instructions, Decision, Results]
