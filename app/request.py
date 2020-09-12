from app import app
import urllib.request,json
from .models import news
Article = news.Article

#Getting api-Key
apiKey= app.config['News_Api_Key']

#Getting the news base-url

base_url=app.config['Top_Headlines_Url']