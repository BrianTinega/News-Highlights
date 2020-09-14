
class Config:
    '''
    General configuration parent class
    '''
    TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCES_URL='https://newsapi.org/v2/sources?apiKey={}'
    TRUMP_URL = "https://newsapi.org/v2/top-headlines?q=trump&apiKey={}"
    GERMANY_URL="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}"
    

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