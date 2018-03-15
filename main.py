#! /usr/bin/env python3


# Importation of a module.
from classes import *


# Instance creation.
sentence = Parser("Salut GrandPy, donne moi stp l'adresse du musée Guimet. Merci")
# Parsing function.
userQuery = sentence.parsing()

# Instance creation.
google_api = GoogleMaps(userQuery)
# Google Maps coordinates function...
# to find latitude.
latitude = google_api.coordinates()[0]
# to find longitude.
longitude = google_api.coordinates()[1]
# to find the global address.
globalAddress = google_api.coordinates()[2]

streetName = google_api.coordinates()[3]   ### A VIRER

# print("La latitude est : {}".format(latitude)) # A VIRER
# print("La longitude est : {}".format(longitude)) # A VIRER

# Instance creation.
wiki_api = MediaWiki(latitude, longitude)   # A CHANGER L'ARGUMENT : PLUTOT LAT ET LNG
# Wikipedia history function.
wikiExtract = wiki_api.history()

# GrandPy Answers.
addressAnswer = GrandPyMessages.randomAnswer()
noAnswer = GrandPyMessages.randomNoAnswer()
storyAnswer = GrandPyMessages.randomStory()

if globalAddress != None:   ## A REVOIR
    print(addressAnswer, globalAddress)
    print(storyAnswer, wikiExtract)
else:
    print(noAnswer)

