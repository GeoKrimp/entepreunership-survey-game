from otree.api import *
from .models import C

class RavensMaze(Page):
    form_model = 'player'
    form_fields = ['answer']

    def vars_for_template(self):
        # Αν έχεις χειροκίνητη λίστα αρχείων C.FILENAMES, χρησιμοποίησέ την.
        files = getattr(C, 'FILENAMES', None)
        if files:
            idx = self.player.round_number - 1
            filename = files[idx] if 0 <= idx < len(files) else files[0]
            img_path = f"ravens_maze/{filename}"
        else:
            img_path = f"ravens_maze/q{self.player.round_number}.png"

        return dict(
            img_path=img_path,
            round_no=self.player.round_number,
            total=C.NUM_ROUNDS,
        )

class FinalResults(Page):
    def is_displayed(self):
        return self.player.round_number == C.NUM_ROUNDS

    def vars_for_template(self):
        # Προαιρετικό scoring: αν έχεις ορίσει C.CORRECT = ['a','b',...]
        total_score = None
        have_key = getattr(C, 'CORRECT', None) is not None
        if have_key:
            rounds = self.player.in_all_rounds()
            total_score = sum(
                1 for p, correct in zip(rounds, C.CORRECT) if p.answer == correct
            )
        return dict(
            have_key=have_key,
            total_score=total_score,
            total=C.NUM_ROUNDS,
        )

class Instructions(Page):
    def is_displayed(self):
        # Οι οδηγίες να φαίνονται μόνο στον 1ο γύρο
        return self.round_number == 1

page_sequence = [Instructions, RavensMaze]
