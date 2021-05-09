class TestingConfig:
    """
        Flask app testing mode configration
        see: https://flask.palletsprojects.com/en/master/config/
    """
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'thisissecretkey'
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True

