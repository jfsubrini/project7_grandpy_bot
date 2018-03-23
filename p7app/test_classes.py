""" To test the classes.py file """

import pytest
import requests
import random

# from .. import classes
from classes import Parser, GoogleMaps, MediaWiki, GrandPyMessages
import run


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
    def test_http_google_return1(self, monkeypatch):
        """ To test the Google Maps Geocoding API by mocking the response
        and expecting a JSON result for 'openclassrooms'. """
        direction = GoogleMaps("openclassrooms")
        
        results = [{'geometry': {'location': {'lat': 48.8747578, 'lng': 2.350564700000001}}}]
        
        def mockreturn(request):
            return results
        
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert direction.coordinates() == results

    # #   - Query 2.
    # def test_http_google_return2(self, monkeypatch):
        """ To test the Google Maps Geocoding API by mocking the response
        and expecting a JSON result for 'tour eiffel'. """
    #     results = [{'geometry': {'location': {'lat': bbb, 'lng': bbb}}}]
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

# class TestMediaWiki:
#     """ To mock the Media Wiki API """

#     # # - MediaWiki Mock :
#     # #   - Charging the right text (first two s) from the right wikipedia page.
#     def test_http_wiki_return1(self, monkeypatch):
#         """ To test the case for first name as a street direction. """
#         # Expected part of the JSON result for "général leclerc".
#         self.results = "Philippe de Hauteclocque, dit Leclerc (1902-1947), général français durant la Seconde Guerre."
#         def mockreturn(request):
#             return self.results
#         monkeypatch.setattr(requests, 'get', mockreturn)
#         assert GoogleMaps.coordinates("général leclerc") == self.results

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

class TestGrandPyMessages:
    """ To test the random messages. """

    # - Ramdom messages :
    #   - Controling GrandPy Bot answer.
    def test_randomAnswer(self):
        """ To test that GrandPy Bot is answering the address. """
        address_answer = GrandPyMessages.randomAnswer()
        assert address_answer in GrandPyMessages.LISTANSWER

    #   - Controling GrandPy Bot no answer.
    def test_randomNoAnswer(self):
        """ To test that GrandPy Bot is answering that he didn't understand the user query. """
        no_answer = GrandPyMessages.randomNoAnswer()
        assert no_answer in GrandPyMessages.LISTANOANSWER
    
    #   - Controling GrandPy Bot wikipedia story answer.
    def test_randomStory(self):
        """ To test that GrandPy Bot is giving the wikipedia history of the address. """
        story_answer = GrandPyMessages.randomStory()
        assert story_answer in GrandPyMessages.LISTWIKIPEDIA

    #   - Controling GrandPy Bot wikipedia no story.
    def test_randomNoStory(self):
        """ To test that GrandPy Bot has no wikipedia story about the place. """
        no_story = GrandPyMessages.randomNoStory()
        assert no_story in GrandPyMessages.LISTNOWIKIPEDIA


###########################################################################################

# class TestRun:
    """ To test the run.py module """

    # - Running the page :
    #   - ...........
    # def test_run(monkeypatch):
        # """ To test ..... """
        # with pytest.raises(AssertionError):

    # - Opening the page :
