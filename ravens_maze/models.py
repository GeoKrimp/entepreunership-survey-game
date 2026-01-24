from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'ravens_maze'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 18

    # Επιλογές a–f
    CHOICES = [('a','a'), ('b','b'), ('c','c'), ('d','d'), ('e','e'), ('f','f')]

    # (Προαιρετικό) Σωστές απαντήσεις για scoring.
    # Αν θες να τις περάσεις από settings.py → SESSION_CONFIGS[...]['params']['correct'],
    # άφησέ το None κι εμείς θα διαβάσουμε από session.config.
    CORRECT = None

class Subsession(BaseSubsession):
    def creating_session(self):
        # Αν δώσεις σωστές απαντήσεις από settings, τις “τραβάμε” εδώ
        correct_from_config = self.session.config.get('params', {}).get('correct')
        if correct_from_config:
            # βεβαιώσου ότι είναι λίστα μήκους NUM_ROUNDS με στοιχεία από {'a'..'f'}
            C.CORRECT = [str(x).lower() for x in correct_from_config]
        # μηδενίζουμε συνολικό σκορ στην αρχή
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['rm_total_score'] = 0

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Απάντηση για τον εκάστοτε γύρο (a–f)
    answer = models.StringField(
        choices=C.CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label='Επίλεξε την ορθή απάντηση'
    )
    # σωστό/λάθος για τον γύρο (αν έχουμε κλειδί)
    is_correct = models.BooleanField(initial=False)
