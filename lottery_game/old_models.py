# models.py
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'lottery_game'
    players_per_group = None
    num_rounds = 4

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            lotteries = [['risk', [
                    [1, 96.0, 96.0],
                    [2, 80.0, 128.0],
                    [3, 64.0, 160.0],
                    [4, 48.0, 192.0],
                    [5, 32.0, 224.0],
                    [6, 16.0, 240.0]
            ]],
                ['loss', [
                    [1, 16.0, 16.0],
                    [2, 0.0, 48.0],
                    [3, -16.0, 80.0],
                    [4, -32.0, 112.0],
                    [5, -48.0, 144.0],
                    [6, -64.0, 160.0]
            ]],
                ['risk_skew', [
                [1, 96.0, 96.0, 96.0],
                [2, 82.1, 123.9, 223.0],
                [3, 68.2, 151.8, 350.1],
                [4, 54.2, 179.8, 477.1],
                [5, 40.3, 207.7, 604.2],
                [6, 26.4, 220.4, 684.0]
            ]],

             ['loss_skew', [
                [1, 16.0, 16.0, 16.0],
                [2, 2.1, 43.9, 143.0],
                [3, -11.8, 71.8, 270.1],
                [4, -25.8, 99.8, 397.1],
                [5, -39.7, 127.7, 524.2],
                [6, -53.6, 140.4, 604.0]
            ]]

            ]  # Define your lotteries list here as shown earlier
            for p in self.get_players():
                #random.shuffle(lotteries)
                p.participant.vars['lotteries'] = lotteries.copy()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    lottery_choice = models.IntegerField(
        choices=[
            (1, 'Option 1'),
            (2, 'Option 2'),
            (3, 'Option 3'),
            (4, 'Option 4'),
            (5, 'Option 5'),
            (6, 'Option 6')
        ],
        widget=widgets.RadioSelect
    )
