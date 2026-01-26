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
