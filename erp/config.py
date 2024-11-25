import os


class Config(object):
    pass


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"


class TestingConfig(Config):
    ENV = "testing"
