import unittest
from io import StringIO
from unittest.mock import patch
import sys
sys.path.append("/home/mb/2023code/2023codevm/vm/2023python/2023summer/Li_Jiachen/2023Summer-Intern/MIT S6.001/Jiachen Li/PS01/ps1c.py")
from ps1c_fun import check_range, boot36m, bisection_search

class TestYourCode(unittest.TestCase):
    def test_check_range(self):
        self.assertTrue(check_range(250000))
        self.assertFalse(check_range(240000))
        self.assertFalse(check_range(260000))

    def test_boot36m(self):
        self.assertAlmostEqual(boot36m(0.04), 335339.47, places=2)
        self.assertAlmostEqual(boot36m(0.08), 380034.52, places=2)

    @patch('builtins.input', return_value='10000')
    def test_bisection_search(self, mock_input):
        expected_output = "0.44140625 11\n"
        with patch('sys.stdout', new=StringIO()) as mock_output:
            bisection_search()
            self.assertEqual(mock_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
