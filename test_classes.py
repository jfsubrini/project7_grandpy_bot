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


###########################################################################################

class TestGoogleMaps:
    """ To test the Google Maps Geocoding API """

    # - GoogleMaps :
    #   - Query 1.
    def test_http_google_return(monkeypatch):
        """ To test ..... """
        results = [{'geometry': {
                            'location':
                            {'lat': 50.62925,
                             'lng': 3.057256}
                        }
                    }]
        def mockreturn(request):
            return response

        monkeypatch.setattr (???)
        assert place.coordinates("Lille") == results

    #   - Query 2.
    def test_http_google_return2(self):
        """ To test a place to find. """
        query2 = GoogleMaps(["openclassrooms"])
        assert query2.coordinates()[0] == 48.8747578
        assert query2.coordinates()[1] == 2.350564700000001

    def test_http_google_return2bis(self):
        """ To test a place to find. """
        query2bis = GoogleMaps("openclassrooms")
        assert query2bis.coordinates()[0] == 48.8747578
        assert query2bis.coordinates()[1] == 2.350564700000001

    #   - Wrong query.
    def test_http_google_return3(self):
        """ To test a direction. """
        query3 = GoogleMaps(["3", "cours", "somme", "bordeaux"])
        assert query3.coordinates()[0] == 44.8301329
        assert query3.coordinates()[1] == -0.5726070000000001



###########################################################################################

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


###########################################################################################

# class TestRun:
    """ To test the run.py module """

    # - Running the page :
    #   - ...........
    # def test_run(monkeypatch):
        # """ To test ..... """
        # with pytest.raises(AssertionError):

    # - Opening the page :
