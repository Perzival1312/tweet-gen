import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'localhost:27017'

class ProductionConfig(Config):
    DATABASE_URI = os.environ['MONGODB_URI']

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True