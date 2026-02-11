from os import environ

SESSION_CONFIGS = [
    dict(
        name='main_experiment',
        display_name='Main Experiment: Survey + Games',
        num_demo_participants=1,
        app_sequence=[
            'intro',
            'multi_survey',   # 1) Survey (όλα τα ερωτηματολόγια)
            'rmet',           # 2) RMET
            'dice_game',      # 3) Dice game
            'lottery_game',   # 4) Lottery game
            'ravens_maze',    # 5) Raven’s-like task
            'eet_vs_bot',     # 6) EET vs Bot
            'dictator_game',  # 7) Dictator game
            'investment_bot', # 8) Investment game vs bot
            'outro',           # 9) Outro
        ],
    ),
    dict(
            name='intro',
            display_name='Intro',
            num_demo_participants=1,
            app_sequence=[
                'intro',  # 1) Survey (όλα τα ερωτηματολόγια)
            ],
        ),
    dict(
        name='ravens_maze',
        display_name='Ravens Maze',
        num_demo_participants=1,
        app_sequence=[
            'ravens_maze',  # 1) Survey (όλα τα ερωτηματολόγια)
        ],
    ),
    dict(
        name='Outro',
        display_name='outro',
        num_demo_participants=1,
        app_sequence=[
            'outro',  # 1) Survey (όλα τα ερωτηματολόγια)
        ],
    ),
    dict(
        name='Lottery_Game',
        display_name='Lottery',
        num_demo_participants=1,
        app_sequence=[
            'lottery_game',  # 1) Survey (όλα τα ερωτηματολόγια)
        ],
    ),
    dict(
        name='EET_vs_Bot',
        display_name='EET',
        num_demo_participants=1,
        app_sequence=[
            'eet_vs_bot',  # 1) Survey (όλα τα ερωτηματολόγια)
        ],
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4974902039238'
