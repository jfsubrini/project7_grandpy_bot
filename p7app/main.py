#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
############################## GrandPy Bot ##############################
##             Main logical module for the GrandPy Bot website.            ##
#########################################################################

Copyright Jean-François Subrini, student DA Python at OpenClassrooms, 10/03/2018.

"""


# Importation of a module.
from classes import Parser, GoogleMaps, MediaWiki, GrandPyMessages


def main():
	""" Main logical module. """
	
	# Instance creation.
	sentence = Parser("Salut GrandPy, je cherche openclassrooms stp. Merci.")
	# Parsing function.
	userQuery = sentence.parsing()



	addressAnswer = GrandPyMessages.randomAnswer()
	storyAnswer = GrandPyMessages.randomStory()
	noStory = GrandPyMessages.randomNoStory()


	# Instance creation.
	direction = GoogleMaps(userQuery)
	# Google Maps coordinates function...
	if direction.coordinates() != False:
	    latitude = direction.coordinates()[0]
	    longitude = direction.coordinates()[1]
	    globalAddress = direction.coordinates()[2]
	else:
	    noAnswer = GrandPyMessages.randomNoAnswer()


	print("La latitude est : {}".format(latitude)) # A VIRER
	print("La longitude est : {}".format(longitude)) # A VIRER

	# Instance creation.
	wiki_api = MediaWiki(latitude, longitude)   # A CHANGER L'ARGUMENT : PLUTOT LAT ET LNG
	# Wikipedia history function.
	wikiExtract = wiki_api.history()



	if globalAddress != None:   ## A REVOIR
	    print(addressAnswer, globalAddress)
	    print(storyAnswer, wikiExtract)
	else:
	    print(noAnswer)
