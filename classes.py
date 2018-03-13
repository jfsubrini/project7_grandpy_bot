#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
############################## GrandPy Bot ##############################
##             All the classes for the GrandPy Bot website.            ##
#########################################################################

Copyright Jean-François Subrini, student DA Python at OpenClassrooms, 10/03/2018.

"""


# Importation of Python's modules.
import re
import requests
import random
# from pprint import pprint     ### A VIRER

# Importation of configuration module with the Google Maps Geocoding key.
from instance.config import GOOGLE_MAPS_KEY_GEOCODING

# Importation of the list of stopwords.
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
        # To remove the stopwords and .!,;' and ? from the sentence.
        self.sentence = [x for x in self.sentence if x not in stopwords]
        # To convert the list to string.
        self.sentence = ' '.join(self.sentence)
        return self.sentence


class GoogleMaps:
    """ Class definition finding the coordinates of the place to find
    and returning the latitude, longitude and the address of that place.
    """

    def __init__(self, query):
        """ Initializer / Instance Attributes """
        self.user_query = query
        self.latitude = float
        self.longitude = float
        self.global_address = str
        self.street_name = str

    def coordinates(self):
        """ Google Maps Geocoding REST API """
        payload = {'address': self.user_query, 'key': GOOGLE_MAPS_KEY_GEOCODING}
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        # print(response.url)   ### A VIRER
        google_maps = response.json()
        # pprint(google_maps)     ### A VIRER
        status = google_maps['status']
        if status == 'OK':
            self.latitude = google_maps['results'][0]['geometry']['location']['lat']
            self.longitude = google_maps['results'][0]['geometry']['location']['lng']
            self.global_address = google_maps['results'][0]['formatted_address']
            self.street_name = google_maps['results'][0]['address_components'][1]['short_name']
            # print("Latitude : {}".format(self.latitude))
            # print("Longitude : {}".format(self.longitude))
            # print("L'adresse de {} est : {}".format(self.user_query, self.global_address))
            # print("L'histoire se réfère à : {}".format(self.street_name))
            return self.latitude
            return self.longitude
            return self.global_address
            return self.street_name
        else:
            # print("Votre demande n'a pas été comprise.\nEntrez juste le lieu que vous recherchez.")
            return "Votre demande n'a pas été comprise.\nEntrez juste le lieu que vous recherchez."


class MediaWiki:
    """ Class definition to find the history of the address of the place to find,
    taking the 2 first sentences on Wikipedia for the 'street' name.
    """

    def __init__(self, wikiquery):
        """ Initializer / Instance Attributes """
        self.keywords = wikiquery.title()

    def history(self):
        """ MediaWiki REST API """
        payload = {'action': 'query', 'titles': self.keywords, 'prop': 'extracts',\
        'explaintext': True, 'exsentences': 2, 'exlimit': 1, 'redirects': True, 'format': 'json',\
        'formatversion': 2}
        response = requests.get('https://fr.wikipedia.org/w/api.php', params=payload)
        media_wiki = response.json()
        # pprint(media_wiki)
        try:
            media_wiki['query']['pages'][0]['missing'] or media_wiki['query']['pages'][0]['invalid']
        except KeyError:
            # Return the first two sentences of the intro in the extracts,
            # in plain text (see payload).
            first_paragraph = media_wiki['query']['pages'][0]['extract']
            print(first_paragraph)
            return first_paragraph
        else:
            print("Désolé mais GrandPy a oublié l'histoire de ce lieu...")


class AnswerLists:
    """ Constant class with lists of GrandPy Bot messages. """

    # Class attributes : list of possible answers.
    LISTANSWER1 = ["Et voilà ! L'adresse que tu cherches est :\n",\
                    "Oh mais c'est très facile ! L'endroit que tu cherches se trouve à cette adresse :\n",\
                    "Rien de plus simple ! L'adresse de ton endroit est :\n"]
    LISTANSWER2 = ["Désolé mais je n'ai pas compris ta demande.\n"\
                    "Peux-tu reformuler ta requête ?",\
                    "Oh la la ! Je suis un peu confus, vu mon grand âge.\n"\
                    "Tu peux me faire une demande plus claire et directe ?",\
                    "Pardon ! Je suis un peu vieux, alors fais-moi une demande plus simple "\
                    "en indiquant le lieu recherché, stp !"]
    LISTWIKIPEDIA = ["Oh mais je connais très bien cet endroit "\
                    "et cela me permet de te raconter son histoire !",\
                    "Souvenir, souvenir ! Je me souviens de cet endroit.\n"\
                    "En voici l'histoire.",\
                    "Je connais très bien ce lieu.\n"\
                    "GrandPy Bot va te conter son histoire..."]

class GrandPyMessages:
    """ Class to display random messages from GrandPy Bot. """

    def randomAnswer1():
        randomIndex = random.randint(0, len(AnswerLists.LISTANSWER1) - 1)
        address_result = AnswerLists.LISTANSWER1[randomIndex]
        # print(address_result)
        return address_result

    def randomAnswer2():
        randomIndex = random.randint(0, len(AnswerLists.LISTANSWER2) - 1)
        no_result = AnswerLists.LISTANSWER2[randomIndex]
        # print(no_result)
        return no_result

    def randomWiki():
        randomIndex = random.randint(0, len(AnswerLists.LISTWIKIPEDIA) - 1)
        wiki_result = AnswerLists.LISTWIKIPEDIA[randomIndex]
        # print(wiki_result)
        return wiki_result

# GrandPyMessages.randomAnswer1()
# GrandPyMessages.randomAnswer2()
# GrandPyMessages.randomWiki()


# sentence = input("Quel lieu ? : ")
# sentence2 = Parser(sentence).parsing()
# print(sentence2)
# google = GoogleMaps(sentence2).coordinates()
# print("Latitude : {}".format(google.latitude))
# print("Longitude : {}".format(google.longitude))
# print("L'adresse de {} est : {}".format(google.user_query, google.global_address))
# print("L'histoire se réfère à : {}".format(google.street_name))


# address = input("Qu'est-ce qu'on cherche ducon ? : ")
# query1 = MediaWiki(address)   #### passer la variable address_name
# MediaWiki.history(query1)
