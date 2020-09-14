from app import app
import urllib.request,json
from urllib.request import urlopen
from .models import news
from .config import Config
Article = news.Article
Sources= news.Sources
from newsapi import NewsApiClient
#Getting api-Key
api_key=app.config["NEWS_API_KEY"]

#Getting the news base-url

base_url=app.config["TOP_HEADLINES_URL"]
news_source_url = app.config["SOURCES_URL"]
trump_url  = app.config["TRUMP_URL"]
bbc_url = app.config["BBC_URL"]

def get_news ():
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)
        return news_results
        
def get_bbc_news():
    get_bbc_url = bbc_url.format(api_key)
    with urllib.request.urlopen(get_bbc_url)as url:
        get_bbc_news_data = url.read()
        get_bbc_news_response = json.loads(get_bbc_news_data)
        if get_bbc_news_response ['articles']:
            bbc_news_results_list = get_bbc_news_response ['articles']
            bbc_results = process_news( bbc_news_results_list)
            return bbc_results
def get_trump_news():
    get_trump_url = trump_url.format(api_key)
    with urllib.request.urlopen(get_trump_url)as url:
        get_trump_data = url.read()
        get_trump_response = json.loads(get_trump_data)
        if get_trump_response ['articles']:
            trump_news_list = get_trump_response ['articles']
            trump_results = process_news ( trump_news_list)
            return trump_results
def process_news(news_list):
    news_results= []
    for news_item in news_list:
        author = news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get ('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get ('content')
        if urlToImage:
            news_object = Article(author,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)
        return news_results



def get_sources():
    get_sources_url = news_source_url.format(api_key)
    with urllib.request.urlopen( get_sources_url)as url:
        get_sources_data=url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_result=None
        if get_sources_response['sources']:
            sources_result_list =  get_sources_response['sources']
            sources_result = process_sources(sources_result_list)
        return sources_result
def process_sources(sources_list):
    sources_result=[]
    for source in sources_list:
        id = source.get('id')
        url = source.get('url')
        name = source.get('name')
        description = source.get('description')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')
        source_object = Sources (id,url,name,description,category,language,country)
        sources_result.append(source_object)
    return sources_result
 
