# dictator_game/pages.py
from otree.api import Page
from .models import C


class Instructions(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(endowment=C.ENDOWMENT)


class Decision(Page):
    form_model = 'player'
    form_fields = ['amount_sent']

    @staticmethod
    def vars_for_template(player):
        # περνάμε το endowment στο template
        return dict(endowment=C.ENDOWMENT)

    @staticmethod
    def before_next_page(player, timeout_happened):
        # εδώ το 'player' είναι Player instance (όχι self)
        player.set_payoffs_as_A()


class Results(Page):
    @staticmethod
    def is_displayed(player):
        return False  # βάλε True αν θέλεις να φαίνεται περίληψη

    @staticmethod
    def vars_for_template(player):
        return dict(
            endowment=C.ENDOWMENT,
            sent=player.amount_sent,
            a=player.a_payoff,
            b=player.b_payoff,
        )


page_sequence = [Instructions, Decision, Results]
