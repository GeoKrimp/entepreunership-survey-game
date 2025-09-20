from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'dictator_game'
    PLAYERS_PER_GROUP = None      # single-player
    NUM_ROUNDS = 1

    ENDOWMENT = cu(20)            # 20 EUR

    # Επιλογές για dropdown (0..20)
    AMOUNT_CHOICES = [(i, str(i)) for i in range(0, 21)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Πόσα στέλνει ο A στον B (dropdown)
    amount_sent = models.IntegerField(
        choices=C.AMOUNT_CHOICES,   # <-- dropdown select
        label="How much do you send to Person B?"
    )

    # Υποθετικά payoffs ως A (δεν τα δείχνουμε στον χρήστη σε αυτό το app)
    a_payoff = models.CurrencyField(initial=0)
    b_payoff = models.CurrencyField(initial=0)

    def set_payoffs_as_A(self):
        sent_int = self.amount_sent or 0
        sent = cu(sent_int)
        self.a_payoff = C.ENDOWMENT - sent
        self.b_payoff = sent
        # Αν θέλεις να μετράει άμεσα στο συνολικό payoff του participant:
        self.payoff = self.a_payoff
