import unittest

from ps1a_fun import part_a

class TestStringMethods(unittest.TestCase):
    def test_case01(self):
        test01 = part_a(120000, .10, 1000000)
        self.assertEqual(test01, 183)
        
    def test_case02(self):
        test02 = part_a(80000, .15, 500000)
        self.assertEqual(test02, 105)
        