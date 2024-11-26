import datetime
import unittest
from home.hello_world import app
from home.hello_world import day_to_word_map


class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello_world/'

    def get_weekday(self):
        current_day = datetime.datetime.today().weekday()
        return day_to_word_map[current_day]

    def test_can_get_correct_max_number_in_series_of_two(self):
        username = "username"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_can_get_correct_weekday(self):
        username = "some"
        weekday = self.get_weekday()
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)
