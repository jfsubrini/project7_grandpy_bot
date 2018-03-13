#! /usr/bin/env python3

from flask import Flask, render_template, url_for
from classes import *


app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/")
@app.route("/home/")
def index():
    # lat = GeoData().coordonates.latitude()
    # lng = GeoData().coordonates.longitude()
    # return render_template("home.html", latitude=lat, longitude=lng)
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
