""" To test the classes.py file """

import pytest

from classes import Parser, GoogleMaps, MediaWiki
import run


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


###########################################################################################@

class TestGoogleMaps:
    """ To test the Google Maps Geocoding API """

    # - GoogleMaps :
    #   - Changing the coordinates (latitude & longitude).
    def test_http_google_return(monkeypatch):
        """ To test ..... """
        pass
        # results = [{'geometry': {
                            #'location':
                            #{'lat': 50.661248,
                             #'lng': 3.1263549}
                        #}
                    #}]
        # def mockreturn(request):
        #     return response???

        # monkeypatch.setattr (???)
        # assert place.coordinates("Lille") == results


###########################################################################################@

# class TestMediaWiki:
    """ To test the Media Wiki API """

    # - MediaWiki :
    #   - Charging the right text (first two s) from the right wikipedia page.
    # def test_http_wiki_return(monkeypatch):
        # """ To test ..... """
        # with pytest.raises(AssertionError):
        # pass
        # results = [{
        #             }]
        # def mockreturn(request):
        #     return response???

        # monkeypatch.setattr (???)
        # assert place.coordinates("???") == results


###########################################################################################@

# class TestRun:
    """ To test the run.py module """

    # - Running the page :
    #   - ...........
    # def test_run(monkeypatch):
        # """ To test ..... """
        # with pytest.raises(AssertionError):

    # - Opening the page :
