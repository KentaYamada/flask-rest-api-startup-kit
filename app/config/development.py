class DevelopmentConfig:
    """
        Default flask app configration
        see: https://flask.palletsprojects.com/en/master/config/
    """
    ENV = 'development'
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'thisissecretkey'
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
