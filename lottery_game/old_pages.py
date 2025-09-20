# pages.py
from otree.api import Page, models
from .models import Constants

class InstructionsPage(Page):
    pass

class LotteryGame(Page):
    form_model = 'player'
    form_fields = ['lottery_choice']

    def vars_for_template(self):
        all_lotteries = self.player.participant.vars.get('lotteries', [])
        # Create a unique identifier for each option
        counter = 0
        for lottery in all_lotteries:
            for option in lottery[1]:
                option.append(counter)  # Append a unique counter to each option
                counter += 1
        return {
            'all_lotteries': all_lotteries
        }


    # #def before_next_page(self):
    #  #   self.player.lottery_type = self.player.participant.vars['lotteries'][self.round_number - 1][0]
    #
    # def before_next_page(self):
    #     # Debugging output
    #     print("Current Round Number:", self.round_number)
    #     print("Stored Lotteries Data:", self.player.participant.vars.get('lotteries'))
    #
    #     # Proceed with safe access
    #     lotteries = self.player.participant.vars.get('lotteries', [])
    #     # if lotteries:
    #     #     try:
    #     #         self.player.lottery_type = lotteries[self.round_number - 1][0]
    #     #     except IndexError:
    #     #         print(f"Error: Incorrect index access in lotteries for round {self.round_number}")
    #     #     except Exception as e:
    #     #         print(f"Unexpected error: {e}")
    #     # else:
    #     #     print("Error: Lotteries data is missing or not initialized.")


page_sequence = [InstructionsPage, LotteryGame]
