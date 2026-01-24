from os import environ

SESSION_CONFIGS = [
    dict(
        name='dice_game',
        display_name='dice_game',
        app_sequence=['dice_game'],
        num_demo_participants=1,
    ),
    # Μπορείτε να κρατήσετε εδώ και άλλες διαμορφώσεις αν υπάρχουν
    dict(
        name='lottery_game',
        display_name='lottery_game',
        app_sequence=['lottery_game'],
        num_demo_participants=1,
    ),
    dict(
        name='ravens_maze',
        display_name='Ravens Maze',
        app_sequence=['ravens_maze'],
        num_demo_participants=1,
        # προαιρετικά: δώσε σωστές απαντήσεις εδώ για scoring
        # params=dict(correct=['b','e','a','c','f','d','b','a','e','c']),
    ),
    dict(
        name='rmet_single_page',
        display_name='RMET — Single Page',
        num_demo_participants=1,
        app_sequence=['rmet'],
    ),

    dict(
        name='multi_survey',
        display_name='Multi Questionnaire (CSV step-by-step)',
        num_demo_participants=1,
        app_sequence=['multi_survey'],  # μόνο αυτό το app
    ),
    dict(
        name='EET',
        display_name='EET vs Bot',
        num_demo_participants=1,
        app_sequence=['eet_vs_bot'],  # <-- το νέο app
    ),
    dict(
        name='dictator_game',
        display_name='Dictator Game',
        num_demo_participants=1,
        app_sequence=['dictator_game'],
    ),
    dict(
        name='investment_bot',
        display_name='Investment Game vs Bot',
        num_demo_participants=1,
        app_sequence=['investment_bot'],
    ),


]
'''
SESSION_CONFIGS = [
    dict(
        name='main_experiment',
        display_name='Main Experiment: Survey + Games',
        num_demo_participants=1,
        app_sequence=[
            'multi_survey',   # Questionnaire 1..N (CSV-based, με progress bar)
            'rmet',           # Reading the Mind in the Eyes Test
            'dice_game',
            'lottery_game',
            'ravens_maze',
            'investment_bot',
        ],
    ),
]
'''

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4974902039238'
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',  # Make sure this line is here
            ],
        },
    },
]
'''