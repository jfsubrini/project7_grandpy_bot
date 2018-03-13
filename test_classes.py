""" To test the classes.py file """

import pytest

# from .. import classes
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
        assert sentence1.parsing() == "rue général leclerc paris france"

    #   - Controling the punctuation out.
    def test_parsing_punctuation(self):
        """ To test that the parser removes punctuation in the sentence. """
        sentence2 = Parser("26, Rue de l'Appel de Londres !")
        assert sentence2.parsing() == "26 rue appel londres"

    #   - Controling the stopwords out.
    def test_parsing_stopwords(self):
        """ To test that the parser removes all the stopwords present in the sentence. """
        sentence3 = Parser("Salut GrandPy ! Adresse du Lycée Montaigne à Paris")
        assert sentence3.parsing() == "lycée montaigne paris"

    #   - Controling the whole sentence parsing.
    def test_parsing_total(self):
        """ To test that the parser works all right. """
        sentence4 = Parser("Salut GrandPy ! Comment tu vas ? Je cherche l'adresse d'Openclassrooms ! Merci")
        assert sentence4.parsing() == "openclassrooms"


###########################################################################################

class TestGoogleMaps:
    """ To mock the Google Maps Geocoding API """

    # - GoogleMaps Mock :
    #   - Query 1.
    # def setup_methoc(self, test_http_google_return1):
    #     self.
    def test_http_google_return1(self, monkeypatch):
        """ To test the Google Maps Geocoding API by mocking the response
        and expecting a JSON result for 'openclassrooms'. """
        self.results = [{'geometry': {'location': {'lat': 48.8747578, 'lng': 2.350564700000001}}}]

        def mockreturn(request):
            return self.results
        
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert GoogleMaps.coordinates("openclassrooms") == results

    # #   - Query 2.
    # def test_http_google_return2(self, monkeypatch):
        """ To test the Google Maps Geocoding API by mocking the response
        and expecting a JSON result for '3 cours somme bordeaux'. """
    #     results = [{'geometry': {
    #                         'location':
    #                         {'lat': 44.8301329,
    #                          'lng': -0.5726070000000001}
    #                     }
    #                 }]
    #     def mockreturn(request):
    #         return results
    #     monkeypatch.setattr(requests, 'get', mockreturn)
    #     assert GoogleMaps.coordinates("3 cours somme bordeaux") == results

    # #   - Query 3.
    # def test_http_google_no_return(self, monkeypatch):
        """ To test the Google Maps Geocoding API by mocking the response
        and expecting no JSON result for 'bbbbbbbb', i.e. no place. """
    #     def mockreturn(request):
    #         return results
    #     monkeypatch.setattr(requests, 'get', mockreturn)
    #     assert GoogleMaps.coordinates("bbbbbbbb") == None

###########################################################################################

 #    #   - Query 1.
 #    def test_http_google_return1(self):
 #        """ To test a place to find. """
 #        query2 = GoogleMaps("openclassrooms")
 #        assert query2.coordinates() == (48.8747578, 2.350564700000001)
 #        # assert query2.coordinates("openclassrooms")[1] == 2.350564700000001

 #    #   - Query 2.
 #    def test_http_google_return2(self):
 #        """ To test a direction. """
 #        query3 = GoogleMaps("3 cours somme bordeaux")
 #        # assert query3.coordinates()[0] == 44.8301329
 #        # assert query3.coordinates()[1] == -0.5726070000000001
 #        assert query3.coordinates() == (44.8301329, -0.5726070000000001)

    # #   - Wrong query.
 #    def test_http_google_no_return(self):
 #        """ To test no real place. """
 #        query3 = GoogleMaps("bbbbbbbb")
 #        assert query3.coordinates() == None


###########################################################################################

class TestMediaWiki:
    """ To mock the Media Wiki API """

    # # - MediaWiki Mock :
    # #   - Charging the right text (first two s) from the right wikipedia page.
    def test_http_wiki_return1(self, monkeypatch):
        """ To test the case for first name as a street direction. """
        # Expected part of the JSON result for "général leclerc".
        results = "<ul><li>Philippe de Hauteclocque, dit Leclerc (1902-1947), général français durant la Seconde Guerre"
        def mockreturn(request):
            return self.results
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert GoogleMaps.coordinates("général leclerc") == self.results

    # def test_http_wiki_return2(self, monkeypatch):
    #     """ To test the case for first name as a street direction . """
    #     # Expected part of the JSON result for "général leclerc".
    #     results = "<p><b>Charles de Gaulle</b> (<small>prononcé : </small><span>[ʃaʁl də ɡol]</span> ), communément app"
    #     def mockreturn(request):
    #         return results
    #     monkeypatch.setattr(requests, 'get', mockreturn)
    #     assert GoogleMaps.coordinates("charles de gaulle") == results

    # def test_http_wiki_no_return(self, monkeypatch):
    #     """ To test no real place. """
    #     # Expected part of the JSON result for "aaaa" (no place).
    #     def mockreturn(request):
    #         return results
    #     monkeypatch.setattr(requests, 'get', mockreturn)
    #     assert GoogleMaps.coordinates("aaaa") == None

###########################################################################################

 #    #   - History 2.
 #    def test_http_wiki_return2(self):
 #        """ To test the case for first name as a street direction. """
 #        place2 = MediaWiki("général leclerc")
 #        assert place2.history() == "<ul><li>Philippe de Hauteclocque, dit Leclerc (1902-1947), général français durant la Seconde Guerre"

 #    #   - History 3.
 #    def test_http_wiki_return3(self):
 #        """ To test the case for first name as a street direction . """
 #        place3 = MediaWiki("charles de gaulle")
 #        assert place3.history() == "<p><b>Charles de Gaulle</b> (<small>prononcé : </small><span>[ʃaʁl də ɡol]</span> ), communément app"

    # #   - No history.
 #    def test_http_wiki_no_return(self):
 #        """ To test no real place. """
 #        no_place = MediaWiki("aaaa")
 #        assert no_place.history() == None


###########################################################################################

# class TestRun:
    """ To test the run.py module """

    # - Running the page :
    #   - ...........
    # def test_run(monkeypatch):
        # """ To test ..... """
        # with pytest.raises(AssertionError):

    # - Opening the page :
