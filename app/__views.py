from app import app
from app import render_template()

@app.route(/)
def index():
    return render_template('index.html')
