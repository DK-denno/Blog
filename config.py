import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dk:Dennisveer27@localhost/blog'
    DEBUG = True


class ProdConfig(Config):
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
