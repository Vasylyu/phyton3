import unittest
from для_тестов import triangle


class TestTriangle(unittest.TestCase):
    def test_triangle_not_correct(self):
        res1 = triangle(3, 22, 3)
        res2 = 'Не прямоугольный'
        self.assertEquals(res1, res2)

    def test_triangle_correct(self):
        res1 = triangle(3, 4, 5)
        res2 = 'Прямоугольный'
        self.assertEquals(res1, res2)
