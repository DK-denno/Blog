import os 
class Config():
    pass


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
