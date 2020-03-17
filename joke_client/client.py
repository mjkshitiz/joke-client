"""
A simple client to fetch jokes from api"""

__author__ = "Kshitiz Maharjan"
__email__ = "kshitizmaharjan@gmail.com"
__status__="dev"
__version__="0.1"

class JokeClient:
    """A joke client
    
    Attributes
        category: String or Tuple or List or Set
        flags: None or Tuple, List or Set
        response: String with default json
        type: string with default = none
        search: none or string
        id: None or integer with range 0-166
    Methods:
        get_joke

    """
    def __init__(self, category="Any", flags=None, response="json", type=None, search=None, id=None):
        self._base_url = "https://sv443.net/jokeapi/v2/Any"
        pass
    
    def get_joke(self):
        pass
