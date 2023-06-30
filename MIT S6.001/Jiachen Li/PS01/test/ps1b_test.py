import unittest

from ps1b_fun import part_b

class TestMatch(unittest.TestCase):
    def test_case01(self):
        test01 = part_b(120000, .05, 500000, .03)
        self.assertEqual(test01, 142)
        
    def test_case02(self):
        test02 = part_b(80000, .1, 800000, .03)
        self.assertEqual(test02, 159)
    
    def test_case03(self):
        test03 = part_b(75000, .05, 1500000, .05)
        self.assertEqual(test03, 261)
