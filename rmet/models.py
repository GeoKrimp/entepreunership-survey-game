from otree.api import *
import os, csv


class C(BaseConstants):
    NAME_IN_URL = 'rmet'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1                # μία σελίδα με όλα τα items
    N_ITEMS = 37                  # image-000 .. image-036
    IMAGE_EXT = 'jpg'             # άλλαξε σε 'png' αν χρειάζεται
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'rmet_items.csv')
    # Το CSV πρέπει να είναι UTF-8 και να έχει στήλες:
    # Item, Option 1, Option 2, Option 3, Option 4, Correct (τιμές 1..4)


class Subsession(BaseSubsession):
    def creating_session(self):
        # Φόρτωση γραμμών από CSV
        with open(C.DATA_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        items = []
        for k, row in enumerate(rows[:C.N_ITEMS]):
            # Index εικόνας (για όνομα αρχείου). Αν λείπει/δεν είναι int, πέφτει στο k.
            try:
                idx = int(row.get('Item', k))
            except Exception:
                idx = k

            # Τέσσερις επιλογές (καθαρισμός κειμένου)
            opts = [ (row.get(f'Option {i}', '') or '').strip() for i in range(1, 5) ]

            # Σωστή επιλογή από τη στήλη Correct (1..4). Αν εκτός εύρους, γίνεται 0 (ουδέτερο).
            try:
                correct = int(row.get('Correct', 0) or 0)
            except Exception:
                correct = 0
            if correct not in (1, 2, 3, 4):
                correct = 0

            items.append(dict(
                ord=k,                                   # θέση στη σελίδα (0..36)
                index=idx,                                # αριθμός εικόνας
                image=f"image-{idx:03d}.{C.IMAGE_EXT}",   # π.χ. image-000.jpg
                options=opts,                             # λίστα 4 labels
                correct=correct,                          # 1..4 (ή 0 αν άγνωστο)
                field=f"resp_{k:03d}",                    # όνομα πεδίου στον Player
            ))

        # Αποθήκευση για χρήση στις σελίδες/templates
        self.session.vars['rmet_items'] = items
        self.session.vars['resp_fields'] = [it['field'] for it in items]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Δημιουργία 37 πεδίων απαντήσεων (Integer 1..4)
    for i in range(C.N_ITEMS):
        locals()[f"resp_{i:03d}"] = models.IntegerField(min=1, max=4)
    del i

    # Συνολικό σκορ (σωστές απαντήσεις) – αποθηκεύεται για export/admin, δεν προβάλλεται στους χρήστες
    score_total = models.IntegerField(initial=0)

    # Helper: επιστρέφει τη λίστα των items από το session
    def items(self):
        return self.session.vars.get('rmet_items', [])
