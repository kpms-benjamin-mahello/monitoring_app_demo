#!/usr/bin/env python3
class Config(object):
    DEBUG = False
    TESTING = False
    TEMPLATE_AUTO_RELOAD = True


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = False
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
