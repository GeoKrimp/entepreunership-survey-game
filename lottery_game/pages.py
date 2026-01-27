# lottery_game/pages.py
from otree.api import Page
import json

class LotteryGame(Page):
    form_model = 'player'
    form_fields = ['selections_json']

    def vars_for_template(self):
        return dict(all_lotteries=self.participant.vars.get('lotteries', []))

    def error_message(self, values):
        raw = values.get('selections_json') or ''
        try:
            data = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            data = {}

        missing = []
        for name, _rows in self.participant.vars.get('lotteries', []):
            if name not in data:
                missing.append(name)

        if missing:
            return "Please choose one option in each lottery before continuing."

class InstructionsPage(Page):
    pass

page_sequence = [InstructionsPage, LotteryGame]
