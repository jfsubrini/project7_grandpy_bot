#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
############################## GrandPy Bot ##############################
##             Main logical module for the GrandPy Bot website.        ##
#########################################################################
Copyright Jean-François Subrini, student DA Python at OpenClassrooms, 16/03/2018.
"""

# Importation of a module.
from .classes import Parser, GoogleMaps, MediaWiki, GrandPyMessages


# GrandPy Bot different possible messages. ###Attention le random ne marche qu'à la 1ere query !
addressAnswer = GrandPyMessages.randomAnswer()
noAnswer = GrandPyMessages.randomNoAnswer()
storyAnswer = GrandPyMessages.randomStory()
noStory = GrandPyMessages.randomNoStory()

# Parser instance creation.
# text input (home.html) comme argument à mettre.
sentence = Parser("Salut GrandPy Bot, comment va ? Je cherche l'adresse du musée Guimet, merci.")
# Running the parsing method.
userQuery = sentence.parsing()

# GoogleMaps instance creation.
query = GoogleMaps(userQuery)
# Running the coordinates method.
addressCoords = query.coordinates()
lat = addressCoords[0]
lng = addressCoords[1]
globalAddress = addressCoords[2]

# MediaWiki instance creation.
coords = MediaWiki(lat, lng)
# Running the history method.
wikiExtract = coords.history()
