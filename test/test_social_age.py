import unittest
from social_age import get_social_status


class TestSocialAge(unittest.TestCase):
    def test_can_get_child(self):
        age = 8
        expected_res = 'ребенок'
        func_res = get_social_status(age)
        self.assertEquals(expected_res, func_res)

    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_can_get_old(self):
        age = 60
        expected_res = 'пожилой'
        func_res = get_social_status(age)
        self.assertEquals(expected_res, func_res)
