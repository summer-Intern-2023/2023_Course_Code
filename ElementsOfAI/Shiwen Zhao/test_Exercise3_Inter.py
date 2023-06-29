from unittest import TestCase
from Exercise3_Inter import climb


class Test(TestCase):
    def setUp(self):
        self.h = [0.0, 0.5, 1.0, 0.5, 0.0]

    def test_climb(self):
        self.assertEqual(climb(2, self.h), 2)
        self.assertEqual(climb(1, self.h), 2)
        self.assertEqual(climb(3, self.h), 2)
