""" The different routes for the app. """

from flask import Flask, render_template, url_for
from .main import *

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/")
@app.route("/index/")
@app.route("/home/")
def home():
    """ Opening the homepage. """
    # lat = GeoData().coordonates.latitude()
    # lng = GeoData().coordonates.longitude()
    # return render_template("home.html", latitude=lat, longitude=lng)

    # return render_template("home.html", addressAnswer="ff", noAnswer="jj",
    #       globalAddress="ll", storyAnswer="mm", noStory="pp",
    #       wikiExtract="ee")

    return render_template("home.html", addressAnswer=addressAnswer, noAnswer=noAnswer, globalAddress=globalAddress, storyAnswer=storyAnswer, noStory=noStory, wikiExtract=wikiExtract)

@app.errorhandler(404)
def page_not_found(error):
    """ Error handler 404. """
    return render_template("errors/404.html"), 404
    