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
from instance.config import *
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

    def __init__(self, latitude=0, longitude=0):
        """ Initializer / Instance Attributes """
        self.latitude = latitude
        self.longitude = longitude

    def coordinates(self, sentence):
        """ Google Maps Geocoding REST API """
        payload = {'address': sentence, 'key': GOOGLE_MAPS_KEY_GEOCODING}
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        print(response.url)
        google_maps = response.json()
        # pprint(google_maps)
        status = google_maps['status']
        if status == 'OK':
            latitude = google_maps['results'][0]['geometry']['location']['lat']
            longitude = google_maps['results'][0]['geometry']['location']['lng']
            # data = (latitude, longitude)
            # print("Latitude : ", data[0])
            # print("Longitude : ", data[1])
            return self.latitude
            return self.longitude
        else:
            print("Votre demande n'a pas été comprise.\nEntrez juste le lieu que vous recherchez.")


class MediaWiki:
    """ Class definition to find the history of the address of the place to find. """

    def __init__(self):
        """ Initializer / Instance Attributes """
        pass

    def history(self):
        """ MediaWiki REST API """
        pass


# address = input("Quel lieu ? : ")
# place = Parser(address)
# sentence = place.parsing()
# gps = GoogleMaps(sentence2)
# gps.coordinates(sentence2)




# # To be standalone
# if __name__ == "__main__":
#     main()


## Sign up pour avoir le API key de l'API Google Maps
## 1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCdrPZF5a3PPvxwXaAq-kTgGun5WEDRj-E
## Geocoding key
# {
#    "results" : [
#       {
#          "address_components" : [
#             {
#                "long_name" : "Google Building 41",
#                "short_name" : "Google Building 41",
#                "types" : [ "premise" ]
#             },
#             {
#                "long_name" : "1600",
#                "short_name" : "1600",
#                "types" : [ "street_number" ]
#             },
#             {
#                "long_name" : "Amphitheatre Parkway",
#                "short_name" : "Amphitheatre Pkwy",
#                "types" : [ "route" ]
#             },
#             {
#                "long_name" : "Mountain View",
#                "short_name" : "Mountain View",
#                "types" : [ "locality", "political" ]
#             },
#             {
#                "long_name" : "Santa Clara County",
#                "short_name" : "Santa Clara County",
#                "types" : [ "administrative_area_level_2", "political" ]
#             },
#             {
#                "long_name" : "California",
#                "short_name" : "CA",
#                "types" : [ "administrative_area_level_1", "political" ]
#             },
#             {
#                "long_name" : "États-Unis",
#                "short_name" : "US",
#                "types" : [ "country", "political" ]
#             },
#             {
#                "long_name" : "94043",
#                "short_name" : "94043",
#                "types" : [ "postal_code" ]
#             }
#          ],
#          "formatted_address" : "Google Building 41, 1600 Amphitheatre...",
#          "geometry" : {
#             "bounds" : {
#                "northeast" : {
#                   "lat" : 37.4228775,
#                   "lng" : -122.085133
#                },
#                "southwest" : {
#                   "lat" : 37.4221145,
#                   "lng" : -122.0860002
#                }
#             },
#             "location" : {
#                "lat" : 37.4224082,
#                "lng" : -122.0856086
#             },
#             "location_type" : "ROOFTOP",
#             "viewport" : {
#                "northeast" : {
#                   "lat" : 37.4238449802915,
#                   "lng" : -122.0842176197085
#                },
#                "southwest" : {
#                   "lat" : 37.4211470197085,
#                   "lng" : -122.0869155802915
#                }
#             }
#          },
#          "place_id" : "ChIJxQvW8wK6j4AR3ukttGy3w2s",
#          "types" : [ "premise" ]
#       }
#    ],
#    "status" : "OK"
# }
