#! /usr/bin/env python3


# Importation of a module.
from classes import *


# Instance creation.
sentence = Parser("Salut GrandPy, je cherche l'adresse d'OpenClassrooms, merci'")
# Parsing function.
user_query = sentence.parsing()

# Instance creation.
google_api = GoogleMaps(user_query)
# Google Maps coordinates function...
# to find latitude (lat).
lat = google_api.coordinates()[0]
# to find longitude (lng).
lng = google_api.coordinates()[1]
# to find the global address.
global_address = google_api.coordinates()[2]

street_name = google_api.coordinates()[3]   ### A VIRER

print("La latitude est : {}".format(lat)) # A VIRER
print("La longitude est : {}".format(lng)) # A VIRER

# Instance creation.
wiki_api = MediaWiki(street_name)   # A CHANGER L'ARGUMENT : PLUTOT LAT ET LNG
# Wikipedia history function.
first_2_sentences = wiki_api.history()

# GrandPy Answers.
answer = GrandPyMessages.randomAnswer()
noAnswer = GrandPyMessages.randomNoAnswer()
wikiStory = GrandPyMessages.randomWiki()

if global_address != None:   ## A REVOIR
    print(answer, global_address)
    print(wikiStory, first_2_sentences)
else:
    print(noAnswer)
