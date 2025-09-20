#Pages.py
from otree.api import Page, WaitPage, Currency as c, currency_range
from .models import Constants
import time

class InstructionsPage(Page):
    pass

class DiceGame(Page):
    form_model = 'player'
    form_fields = ['dice_roll_1', 'dice_roll_2', 'dice_roll_3', 'sum_dice']

    def is_displayed(self):
        self.participant.vars['start_time'] = time.time()  # Καταγράφει τον χρόνο έναρξης
        return True

    def before_next_page(self):
        end_time = time.time()  # Καταγράφει τον χρόνο λήξης
        self.player.total_earnings = self.player.sum_dice * 1
        self.player.stay_duration = end_time - self.participant.vars['start_time']  # Υπολογίζει τη διάρκεια παραμονής

    def vars_for_template(self):
        return {
            'initial_dice_1': 0,
            'initial_dice_2': 0,
            'initial_dice_3': 0
        }

page_sequence = [InstructionsPage, DiceGame]
