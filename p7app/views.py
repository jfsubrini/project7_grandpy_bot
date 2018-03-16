""" Different Routes for the app. """

from flask import Flask, render_template, url_for
# from classes import *


app = Flask(__name__)
# app = Flask(__name__, instance_relative_config=True)  # A VIRER ?

# app.config.from_object('config')   # A VIRER ?
# app.config.from_pyfile('config.py')  # A VIRER ?

@app.route("/")
@app.route("/index/")
@app.route("/home/")
def home():
    """ Opening the homepage. """
    # lat = GeoData().coordonates.latitude()
    # lng = GeoData().coordonates.longitude()
    # return render_template("home.html", latitude=lat, longitude=lng)
    return render_template("home.html")

    # return render_template("home.html", textAnswer=addressAnswer, \
    #     address=globalAddress, textStory=storyAnswer, wikistory=wikiExtract)
    # return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    """ Error handler 404. """
    return render_template("errors/404.html"), 404
    