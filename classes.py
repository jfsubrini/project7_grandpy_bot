#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
############################## GrandPy Bot ##############################
##             All the classes for the GrandPy Bot website.            ##
#########################################################################

Copyright Jean-François Subrini, student DA Python at OpenClassrooms, 10/03/2018.

"""


# Importation of modules
import re
import requests
# from pprint import pprint
# Importation of configuration modules
from instance.config import GOOGLE_MAPS_KEY_GEOCODING
from config import *


class Parser:
    """ Class definition to parse the sentence from the webpage input. """

    def __init__(self, sentence):
        """ Initializer / Instance Attributes """
        self.sentence = sentence

    def parsing(self):
        """ Parser """
        # To put every words of the sentence in lowercase.
        self.sentence = self.sentence.lower()
        # To remove .!,; and ? from the sentence and transform it into a list of words.
        self.sentence = re.sub(r"[.!,;?\']", " ", self.sentence).split()
        # To remove the stopwords and .!,;' and ? froém the sentence.
        self.sentence = [x for x in self.sentence if x not in stopwords]
        return self.sentence

class GoogleMaps:
    """ Class definition to find the coordinates of the place to find. """

    def __init__(self, query, latitude=0, longitude=0):
        self.query = query
        self.latitude = latitude
        self.longitude = longitude

    def coordinates(self, sentence):
        """ Google Maps Geocoding REST API """
        payload = {'address': sentence, 'key': GOOGLE_MAPS_KEY_GEOCODING}
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        # print(response.url)
        google_maps = response.json()
        # pprint(google_maps)
        status = google_maps['status']
        if status == 'OK':
            latitude = google_maps['results'][0]['geometry']['location']['lat']
            longitude = google_maps['results'][0]['geometry']['location']['lng']
            data = (latitude, longitude)
            print("Latitude : ", data[0])
            print("Longitude : ", data[1])
            return data[0]
            return data[1]
            # return self.latitude
            # return self.longitude
        else:
            print("Votre demande n'a pas été comprise.\nEntrez juste le lieu que vous recherchez.")


class MediaWiki:
    """ Class definition to find the history of the address of the place to find. """

    def __init__(self, query):
        """ Initializer / Instance Attributes """
        self.query = query

    def history(self):
        """ MediaWiki REST API """
        payload = {'action': 'query', 'titles': self.query, 'prop': 'extracts',\
        'rvprop': 'content', 'format': 'json', 'formatversion': 2}
        response = requests.get('https://fr.wikipedia.org/w/api.php', params=payload)
        media_wiki = response.json()
        # pprint(media_wiki)
        try:
            media_wiki['query']['pages'][0]['missing']
        except KeyError:
            # ne garder que le 1er paragraphe
            first_paragraph = media_wiki['query']['pages'][0]['extract'][0:500]
            print(first_paragraph)
            return first_paragraph
        else:
            print("Désolé mais GrandPy a oublié l'histoire de ce lieu...")


address = input("Quel lieu ? : ")
place = Parser(address)
sentence1 = place.parsing()
gps = GoogleMaps(sentence1)
gps.coordinates(sentence1)

address = input("Qu'est-ce qu'on cherche ducon ? : ")
query1 = MediaWiki(address)
MediaWiki.history(query1)


# # To be standalone
# if __name__ == "__main__":
#     main()
