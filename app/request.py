from app import app
import urllib.request,json
from urllib.request import urlopen
from .models import news
from .config import Config
Article = news.Article
from newsapi import NewsApiClient
#Getting api-Key
api_key=app.config["NEWS_API_KEY"]

#Getting the news base-url

base_url=app.config["TOP_HEADLINES_URL"]


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