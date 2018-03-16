#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
############################## GrandPy Bot ##############################
##             All the classes for the GrandPy Bot website.            ##
#########################################################################

Copyright Jean-François Subrini, student DA Python at OpenClassrooms, 10/03/2018.

"""


# Importation of Python's modules.
import random
import re
import requests
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
        self.sentence = [x for x in self.sentence if x not in STOPWORDS]
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

    def coordinates(self):
        """ Google Maps Geocoding REST API """
        payload = {'address': self.user_query, 'key': GOOGLE_MAPS_KEY_GEOCODING}
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        google_maps = response.json()
        # pprint(google_maps)     ### A VIRER
        status = google_maps['status']
        if status == 'OK':
            self.latitude = google_maps['results'][0]['geometry']['location']['lat']
            self.longitude = google_maps['results'][0]['geometry']['location']['lng']
            self.global_address = google_maps['results'][0]['formatted_address']
            return self.latitude, self.longitude, self.global_address


class MediaWiki:
    """ Class definition to find the story of the nearby landmark the user wanted
    to find, passing latitude and longitude coordinates to MediaWiki and returning
    the 2 first sentences of the first paragraph extract of the Wikipedia page.
    """

    def __init__(self, latitude, longitude):
        """ Initializer / Instance Attributes """
        self.latitude = latitude
        self.longitude = longitude

    def history(self):
        """ MediaWiki REST API """
        coord = '{}|{}'.format(self.latitude, self.longitude)
        payload = {'action': 'query', 'generator': 'geosearch', 'ggsradius':50, \
        'ggscoord': coord, 'prop': 'extracts', 'explaintext': True, 'exsentences': 2, \
        'exlimit': 1, 'redirects': True, 'format': 'json', 'formatversion': 2}
        response = requests.get('https://fr.wikipedia.org/w/api.php', params=payload)
        media_wiki = response.json()
        # pprint(media_wiki)    ### A VIRER
        first_2_sentences = media_wiki['query']['pages'][0]['extract']
        return first_2_sentences
        # try:
        #     media_wiki['query']['pages'][0]['missing'] or media_wiki['query']['pages'][0]['invalid']
        # except KeyError:
        #     # Return the first two sentences of the intro in the extracts,
        #     # in plain text (see payload).
        #     first_2_sentences = media_wiki['query']['pages'][0]['extract']
        #     # print(first_2_sentences)
        #     return first_2_sentences
        # else:
        #     return "Désolé mais GrandPy a oublié l'histoire de ce lieu..."


class GrandPyMessages:
    """ Class to display random messages from a list of GrandPy Bot messages. """

    # Class attributes : list of possible answers.
    LISTANSWER = ["Et voilà ! L'adresse que tu cherches est :\n", \
                    "Oh mais c'est très facile ! L'endroit que tu cherches se trouve à cette adresse :\n", \
                    "Rien de plus simple ! L'adresse de ton endroit est :\n"]

    LISTANOANSWER = ["Désolé mais je n'ai pas compris ta demande.\n"\
                    "Peux-tu reformuler ta requête ?", \
                    "Oh la la ! Je suis un peu confus, vu mon grand âge.\n"\
                    "Tu peux me faire une demande plus claire et directe ?", \
                    "Pardon ! Je suis un peu vieux, alors fais-moi une demande plus simple "\
                    "en indiquant le lieu recherché, stp !"]

    LISTWIKIPEDIA = ["Oh mais je connais très bien cet endroit "\
                    "et cela me permet de te raconter son histoire !", \
                    "Souvenir, souvenir ! Je me souviens de cet endroit.\n"\
                    "En voici l'histoire.", \
                    "Je connais très bien ce lieu.\n"\
                    "GrandPy Bot va te conter son histoire..."]

    LISTNOWIKIPEDIA = ["Désolé mais je n'ai pas d'histoire intéressante à ce sujet.", \
                    "Oh ! Je n'ai plus les idées claires, j'ai oublié l'histoire à ce sujet.", \
                    "Pardon mais je connais mal cet endroit."]


    def randomAnswer():
        """ Random messages where GrandPy Bot gives the address of the place. """
        address_answer = random.choice(GrandPyMessages.LISTANSWER)
        # print(address_result)
        return address_answer

    def randomNoAnswer():
        """ Random messages when GrandPy Bot didn't understand the user query. """
        no_answer = random.choice(GrandPyMessages.LISTANOANSWER)
        # print(no_result)
        return no_answer

    def randomStory():
        """ Random messages where GrandPy Bot tell the story about the place. """
        story_answer = random.choice(GrandPyMessages.LISTWIKIPEDIA)
        # print(wiki_result)
        return story_answer

    def randomNoStory():
        """ Random messages where GrandPy Bot tell that he has no story about the place. """
        no_story = random.choice(GrandPyMessages.LISTNOWIKIPEDIA)
        # print(wiki_result)
        return no_story
