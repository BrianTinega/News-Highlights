
class Config:
    '''
    General configuration parent class
    '''
    TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCES_URL='https://newsapi.org/v2/sources?apiKey={}'
    TRUMP_URL = "https://newsapi.org/v2/everything?q=apple&from=2020-09-13&to=2020-09-13&sortBy=popularity&apiKey={}"
    BBC_URL="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}"
    

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