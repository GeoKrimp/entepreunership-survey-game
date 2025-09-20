# pages.py
from otree.api import Page
import json
from .models import Constants
from .old_pages import InstructionsPage


class LotteryGame(Page):
    form_model = 'player'
    form_fields = ['selections_json']  # ΜΟΝΟ αυτό

    def vars_for_template(self):
        all_lotteries = self.player.participant.vars.get('lotteries', [])
        copied = []
        counter = 0
        for lottery in all_lotteries:
            name = lottery[0]
            rows = []
            for option in lottery[1]:
                row = option[:]  # copy
                if len(row) < 5:
                    row.append(counter)
                else:
                    row[4] = counter
                counter += 1
                rows.append(row)
            copied.append([name, rows])
        return {'all_lotteries': copied}

    def error_message(self, values):
        try:
            data = json.loads(values.get('selections_json') or '{}')
        except Exception:
            return 'Παρουσιάστηκε πρόβλημα με την υποβολή. Δοκίμασε ξανά.'
        required = [lot[0] for lot in self.player.participant.vars.get('lotteries', [])]
        missing = [name for name in required if name not in data]
        if missing:
            return 'Παρακαλώ επίλεξε μία επιλογή σε κάθε λοταρία.'

    #def before_next_page(self, timeout_happened):
     #   pass

# ΠΡΕΠΕΙ να υπάρχει:
page_sequence = [InstructionsPage, LotteryGame]
