# lottery_game/pages.py
from otree.api import Page
from .models import Constants
import json


class LotteryGame(Page):
    form_model = 'player'
    form_fields = ['selections_json']

    def vars_for_template(self):
        """
        Παίρνουμε τις λοταρίες από participant.vars που έβαλες στο Subsession.creating_session
        (models.py).
        """
        return dict(
            all_lotteries=self.participant.vars['lotteries']
        )

    def error_message(self, values):
        """
        Ελέγχει ότι ο παίκτης έχει διαλέξει ΜΙΑ επιλογή σε ΚΑΘΕ λοταρία.
        Το JS γεμίζει το selections_json με όλα τα checked radios.
        """
        raw = values.get('selections_json') or ''
        try:
            data = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            data = {}

        missing = []
        for name, _rows in self.participant.vars['lotteries']:
            if name not in data:
                missing.append(name)

        if missing:
            return "Please choose one option in each lottery before continuing."

class InstructionsPage(Page):
    pass

page_sequence = [InstructionsPage, LotteryGame]
