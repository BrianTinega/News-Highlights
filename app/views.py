from app import app
from flask import render_template
from .request import get_news

@app.route('/')
def index():
    top = get_news()
    print(top)
    sports_news = get_news()
    print(sports_news)
    return render_template('index.html', headlines = top, sports = sports_news)
