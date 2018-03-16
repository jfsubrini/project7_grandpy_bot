#! /usr/bin/env python3
# -*- coding: utf-8 -*-


"""
############################## GrandPy Bot ##############################
##       Running module for the GrandPy Bot website with Flask         ##
#########################################################################

Copyright Jean-François Subrini, student DA Python at OpenClassrooms, 10/03/2018.

"""


from flask import Flask, render_template, url_for
# from classes import *
from main import main


app = Flask(__name__)
# app = Flask(__name__, instance_relative_config=True)  # A VIRER ?

# app.config.from_object('config')   # A VIRER ?
# app.config.from_pyfile('config.py')  # A VIRER ?

@app.route("/")
@app.route("/index/")
@app.route("/home/")
def index():
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
    """ Error handler. """
    return render_template("errors/404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
