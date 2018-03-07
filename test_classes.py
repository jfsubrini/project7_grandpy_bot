""" To test the classes.py file """

import pytest

from classes import Parser, GoogleMaps, MediaWiki
import run

import requests


class TestParser:
    """ To test the parser """

    # - Parsing :
    #   - Controling the lowercase.
    def test_parsing_lowercase(self):
        """ To test that the parser applies lowercase to all the words. """
        sentence1 = Parser("Rue Général Leclerc Paris France")
        assert sentence1.parsing() == ["rue", "général", "leclerc", "paris", "france"]

    #   - Controling the punctuation out.
    def test_parsing_punctuation(self):
        """ To test that the parser removes punctuation in the sentence. """
        sentence2 = Parser("26, Rue de l'Appel de Londres !")
        assert sentence2.parsing() == ["26", "rue", "appel", "londres"]

    #   - Controling the stopwords out.
    def test_parsing_stopwords(self):
        """ To test that the parser removes all the stopwords present in the sentence. """
        sentence3 = Parser("Salut GrandPy ! Adresse du Lycée Montaigne à Paris")
        assert sentence3.parsing() == ["lycée", "montaigne", "paris"]

    #   - Controling the whole sentence parsing.
    def test_parsing_total(self):
        """ To test that the parser works all right. """
        sentence4 = Parser("Salut GrandPy ! Comment tu vas ? Je cherche l'adresse d'Openclassrooms ! Merci")
        assert sentence4.parsing() == ["openclassrooms"]


###########################################################################################

class TestGoogleMaps:
    """ To mock the Google Maps Geocoding API """

    # - GoogleMaps Mock :
    #   - Query 1.
    # def test_http_google_return(monkeypatch):
    #     """ To mock the result of a geocoding query """
    #     results = [{'geometry': {
    #                         'location':
    #                         {'lat': 50.62925,
    #                          'lng': 3.057256}
    #                     }
    #                 }]

    #     def mockreturn(request):
    #         return results

    #     monkeypatch.setattr(request, 'get', mockreturn)
    #     assert GoogleMaps.coordinates("lille") == results

    # #   - Query 2.
    # def test_http_google_return2(monkeypatch):
    #     """ To mock the result of a geocoding query """
    #     results = [{'geometry': {
    #                         'location':
    #                         {'lat': 50.62925,
    #                          'lng': 3.057256}
    #                     }
    #                 }]

    #     def mockreturn(request):
    #         return BytesIO(json.dumps(results))

    #     monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    #     assert GoogleMaps.coordinates("openclassrooms") == results

    # #   - Wrong query.
    # def test_http_google_return3(monkeypatch):
    #     """ To mock the result of a geocoding query """
    #     results = [{'geometry': {
    #                         'location':
    #                         {'lat': 44.8301329,
    #                          'lng': -0.5726070000000001}
    #                     }
    #                 }]

    #     def mockreturn(request):
    #         return BytesIO(json.dumps(results))

    #     monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    #     assert GoogleMaps.coordinates("3 cours somme bordeaux") == results


    #   - Query 1.
    def test_http_google_return1(self):
        """ To test a place to find. """
        query2 = GoogleMaps("openclassrooms")
        assert query2.coordinates() == (48.8747578, 2.350564700000001)
        # assert query2.coordinates("openclassrooms")[1] == 2.350564700000001

    #   - Query 2.
    def test_http_google_return2(self):
        """ To test a direction. """
        query3 = GoogleMaps("3 cours somme bordeaux")
        # assert query3.coordinates()[0] == 44.8301329
        # assert query3.coordinates()[1] == -0.5726070000000001
        assert query3.coordinates() == (44.8301329, -0.5726070000000001)

	#   - Wrong query.
    def test_http_google_no_return(self):
        """ To test no real place. """
        query3 = GoogleMaps("bbbbbbbb")
        assert query3.coordinates() == None


###########################################################################################

# class TestMediaWiki:
    """ To mock the Media Wiki API """

    # - MediaWiki Mock :
    #   - Charging the right text (first two s) from the right wikipedia page.
    # def test_http_wiki_return(monkeypatch):
        # """ To mock ..... """
        # with pytest.raises(AssertionError):
        # pass
        # results = [{
        #             }]
        # def mockreturn(request):
        #     return response???

        # monkeypatch.setattr (???)
        # assert place.coordinates("???") == results

	#   - History 1.
    def test_http_wiki_return1(self):
        """ To test . """
        place1 = MediaWiki("Nerja")
        assert place1.history() == "<p><b>Nerja</b> est une ville et une commune de la comarque de La Axarquía, province de Malaga, comm"

	#   - No history.
    def test_http_wiki_no_return(self):
        """ To test no real place. """
        no_place = MediaWiki("aaaa")
        assert no_place.history() == None



## pb de sensibilité à la casse


###########################################################################################

# class TestRun:
    """ To test the run.py module """

    # - Running the page :
    #   - ...........
    # def test_run(monkeypatch):
        # """ To test ..... """
        # with pytest.raises(AssertionError):

    # - Opening the page :
