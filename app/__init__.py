from flask import Flask

from url_shortener import UrlManager

app = Flask(__name__)
app.config.from_object('config')
UrlManager.initalize()


from app import views
