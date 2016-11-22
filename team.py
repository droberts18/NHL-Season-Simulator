from random import randint


class Team:
    name = "null"
    pp_percent = 0.0
    pk_percent = 0.0
    five_on_five = 0.00
    gpg = 0.00
    gapg = 0.00
    total = 0.0
    score = 0.0
    wins = 0
    losses = 0
    conference = "null"
    division = "null"
    playoffs = False
    second_round = False
    semifinals = False
    finals = False
    numOfCups = 0

    def __init__(self, name, pp_percent, pk_percent, five_on_five, gpg, gapg, conference, division):
        self.name = name
        self.pp_percent = pp_percent
        self.pk_percent = pk_percent
        self.five_on_five = five_on_five
        self.gpg = gpg
        self.gapg = gapg
        self.conference = conference
        self.division = division

        self.total = round(22.271 + 0.0714*pp_percent + 0.480*pk_percent + 23.960*five_on_five + 16.703*gpg - 19.541*gapg)