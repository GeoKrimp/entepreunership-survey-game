# investment_bot/models.py
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'investment_bot'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    ENDOWMENT = cu(10)
    MULTIPLIER = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # πόσα στέλνει ο παίκτης (x)
    sent_amount = models.CurrencyField(
        min=cu(0),
        max=C.ENDOWMENT,
        label="How much of your 10€ endowment do you want to send to the other participant?"
    )

    # πόσα επέστρεψε το bot (y)
    returned_amount = models.CurrencyField(initial=cu(0))

    # payoff του bot
    bot_payoff = models.CurrencyField(initial=cu(0))

    # απλή στρατηγική bot: επιστρέφει το 50% από τα τριπλασιασμένα
    def bot_return_fraction(self) -> float:
        if not self.sent_amount or self.sent_amount <= 0:
            return 0.0
        return 0.5

    def set_payoffs(self):
        sent = self.sent_amount or cu(0)
        tripled = sent * C.MULTIPLIER

        frac = self.bot_return_fraction()
        returned = tripled * frac

        self.returned_amount = returned
        self.payoff = C.ENDOWMENT - sent + returned
        self.bot_payoff = tripled - returned
