import unittest as ut
from joke_client.client import JokeClient

class JokeClientTestCase(ut.TestCase):
    def setup(self):
        self.joke_client = JokeClient()

    def test_is_instantiated_properly(self):
        self.assertIsInstance(self.joke_client, JokeClient)
        self.assertFalse(True)

    def test_if_joke_client_is_valide(self):
        self.assertFalse(True)
    
    def test_joke_client_url_is_valid(self):
        valid_url = "https://sv443.net/jokeapi/v2/joke/Any"
        self.assertEqual(self.joke_client._base_url, valid_url)
        

        self.assertFalse(True)
    def test_joke_client_fetches_a_joke(self):
        self.assertFalse(True)

if __name__=="__main__":
    ut.main()