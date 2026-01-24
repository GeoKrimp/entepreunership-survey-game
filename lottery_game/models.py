from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import json


class Constants(BaseConstants):
    name_in_url = 'lottery_game'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number != 1:
            return

        # ΑΠΛΑ τα νούμερα, όπως τα είχες πριν :contentReference[oaicite:0]{index=0}
        lotteries_raw = [
            ['risk', [
                [1, 96.0, 96.0],
                [2, 80.0, 128.0],
                [3, 64.0, 160.0],
                [4, 48.0, 192.0],
                [5, 32.0, 224.0],
                [6, 16.0, 240.0],
            ]],
            ['loss', [
                [1, 16.0, 16.0],
                [2, 0.0, 48.0],
                [3, -16.0, 80.0],
                [4, -32.0, 112.0],
                [5, -48.0, 144.0],
                [6, -64.0, 160.0],
            ]],
            ['risk_skew', [
                [1, 96.0, 96.0, 96.0],
                [2, 82.1, 123.9, 223.0],
                [3, 68.2, 151.8, 350.1],
                [4, 54.2, 179.8, 477.1],
                [5, 40.3, 207.7, 604.2],
                [6, 26.4, 220.4, 684.0],
            ]],
            ['loss_skew', [
                [1, 16.0, 16.0, 16.0],
                [2, 2.1, 43.9, 143.0],
                [3, -11.8, 71.8, 270.1],
                [4, -25.8, 99.8, 397.1],
                [5, -39.7, 127.7, 524.2],
                [6, -53.6, 140.4, 604.0],
            ]],
        ]

        # Εδώ φτιάχνουμε έτοιμο κείμενο "a to b" ή "a to b to c"
        lotteries = []
        for name, options in lotteries_raw:
            opt_objs = []
            for row in options:
                idx = row[0]
                values = row[1:]
                if len(values) == 2:
                    text = f'{values[0]} to {values[1]}'
                elif len(values) == 3:
                    text = f'{values[0]} to {values[1]} to {values[2]}'
                else:
                    text = ' / '.join(str(v) for v in values)
                opt_objs.append(dict(id=idx, text=text))
            lotteries.append([name, opt_objs])

        # σώζουμε τις λοταρίες στον participant
        for p in self.get_players():
            p.participant.vars['lotteries'] = lotteries


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_choice = models.IntegerField(
        choices=[(i, f'Option {i}') for i in range(1, 7)],
        widget=widgets.RadioSelect
    )
    # όλες οι επιλογές της σελίδας
    selections_json = models.LongStringField(blank=True)
