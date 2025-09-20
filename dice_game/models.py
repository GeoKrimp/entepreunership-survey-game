from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

class Constants(BaseConstants):
    name_in_url = 'dice_game'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    dice_roll_1 = models.IntegerField()
    dice_roll_2 = models.IntegerField()
    dice_roll_3 = models.IntegerField()
    sum_dice = models.IntegerField()
    total_earnings = models.CurrencyField(initial=0)
    stay_duration = models.FloatField()  # Πεδίο για την αποθήκευση της διάρκειας παραμονής
