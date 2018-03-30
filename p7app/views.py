""" The different routes for the app, functions to manage the queries
 and render a HTML page. """

from flask import Flask, render_template, url_for, request, json
from .classes import Parser, GoogleMaps, MediaWiki, GrandPyMessages

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')


@app.route("/")
@app.route("/index/")
@app.route("/home/")
def home():
    """Opening the homepage."""
    return render_template("home.html")


@app.route("/_query", methods=['GET'])
def query():
    """Method to receive the query from the client side (input form) with AJAX
    and return all the objects needed in json to AJAX, after making instances
    and running the methods from classes.py."""

    # Getting the text the user type in the input form.
    userText = request.args.get('text')

    # Parsing the user text.
    # Parser instance creation.
    sentence = Parser(userText)
    # Running the parsing method.
    userQuery = sentence.parsing()

    # GoogleMaps instance creation.
    query = GoogleMaps(userQuery)

    # Find the address of the place looked for.
    try:
        # Running the coordinates method and retrieving latitude, longitude
        # and the global address of the place the user is looking for.
        addressCoords = query.coordinates()
        latitude = addressCoords[0]
        longitude = addressCoords[1]
        globalAddress = addressCoords[2]
        # GrandPy Bot different possible messages in case of success.
        addressAnswer = GrandPyMessages.randomAnswer()
        # Find a story of the wanted place.
        try:
            # MediaWiki instance creation.
            coords = MediaWiki(latitude, longitude)
            # Running the history method to get the wikipedia page for that coordonates.
            wikiExtract = coords.history()[0]
            pageid = coords.history()[1]
            if wikiExtract:
                # GrandPy Bot different possible messages in case of success.
                storyAnswer = GrandPyMessages.randomStory()
            else:
                # GrandPy Bot different possible messages if there is no answer from Wikipedia.
                storyAnswer = GrandPyMessages.randomNoStory()
                # Reference this empty variable.
                wikiExtract = ''
                pageid = ''
        except:
            # GrandPy Bot different possible messages if there is no answer from Wikipedia.
            storyAnswer = GrandPyMessages.randomNoStory()
            # Reference this empty variable.
            wikiExtract = ''
            pageid = ''
    except:
        # GrandPy Bot different possible messages if there is no answer from GoogleMaps.
        addressAnswer = GrandPyMessages.randomNoAnswer()
        # Reference those empty variables.
        latitude = ''
        longitude = ''
        globalAddress = ''
        wikiExtract = ''
        storyAnswer = ''
        pageid = ''

    # JSON with the responses send back to AJAX (home.js).
    return json.dumps({'userText': userText, \
        'addressAnswer': addressAnswer, \
        'lat':latitude, \
        'lng':longitude, \
        'globalAddress':globalAddress, \
        'storyAnswer': storyAnswer, \
        'wikiExtract': wikiExtract, \
        'pageid': pageid})


@app.errorhandler(404)
def page_not_found(error):
    """Error handler 404."""
    return render_template("errors/404.html"), 404
