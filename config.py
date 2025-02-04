import os
class Config:
    '''
    General configuration parent class
    '''
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'

    SOURCES_API_KEY = 'f80f23ee3b83401e951859c48cf71821'
    print(SOURCES_API_KEY)
   
    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}