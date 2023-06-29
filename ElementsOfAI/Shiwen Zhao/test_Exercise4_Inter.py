from unittest import TestCase
from Exercise4_Inter import test


class Test(TestCase):
    def test_test1(self):
        self.assertEqual(test(0.5), 'dog', test(0.5) + " != dog, wrong")

    def test_test2(self):
        self.assertEqual(test(0.1), 'cat', test(0.1) + " != cat, wrong")
