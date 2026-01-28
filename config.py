import os

class Config:
    """Base configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///water_quality.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'iot-water-quality-secret-key-2026'
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
