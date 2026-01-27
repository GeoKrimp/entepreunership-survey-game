# lottery_game/models.py
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

class Constants(BaseConstants):
    name_in_url = 'lottery_game'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number != 1:
            return

        RAW_LOTTERIES = [
            ('risk', [
                (1, 96.0, 96.0),
                (2, 80.0, 128.0),
                (3, 64.0, 160.0),
                (4, 48.0, 192.0),
                (5, 32.0, 224.0),
                (6, 16.0, 240.0),
            ]),
            ('loss', [
                (1, 16.0, 16.0),
                (2, 0.0, 48.0),
                (3, -16.0, 80.0),
                (4, -32.0, 112.0),
                (5, -48.0, 144.0),
                (6, -64.0, 160.0),
            ]),
            ('risk_skew', [
                (1, 96.0, 96.0, 96.0),
                (2, 82.1, 123.9, 223.0),
                (3, 68.2, 151.8, 350.1),
                (4, 54.2, 179.8, 477.1),
                (5, 40.3, 207.7, 604.2),
                (6, 26.4, 220.4, 684.0),
            ]),
            ('loss_skew', [  # (διόρθωσα και το όνομα για να μην έχει περίεργους χαρακτήρες)
                (1, 16.0, 16.0, 16.0),
                (2, 2.1, 43.9, 143.0),
                (3, -11.8, 71.8, 270.1),
                (4, -25.8, 99.8, 397.1),
                (5, -39.7, 127.7, 524.2),
                (6, -53.6, 140.4, 604.0),
            ]),
        ]

        lotteries_for_template = []
        for name, options in RAW_LOTTERIES:
            rows = []
            max_outcomes = 0

            for opt in options:
                oid = opt[0]
                payoffs = list(opt[1:])
                max_outcomes = max(max_outcomes, len(payoffs))

                # (ό,τι text θες)
                text = " / ".join([f"€{x}" for x in payoffs])

                rows.append({'id': oid, 'payoffs': payoffs, 'text': text})

            lotteries_for_template.append({
                'name': name,
                'rows': rows,
                'n_outcomes': max_outcomes,  # 2 για risk/loss, 3 για skew
            })

        for p in self.get_players():
            p.participant.vars['lotteries'] = lotteries_for_template




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selections_json = models.LongStringField(blank=True)
