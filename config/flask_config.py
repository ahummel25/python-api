class Config(object):       
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    HOST = 'localhost'
    PORT = 80
    FLASK_ENV = 'development'
    FLASK_APP = 'app.py'

class TestingConfig(Config):
    TESTING = True