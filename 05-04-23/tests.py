import unittest
import json
from main import findBiggestContraption as fc

class TestContainers(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fc("[[2,2],[2,2],[2,2]]"), 1)

    def test_2(self):
        self.assertEqual(fc("[[5,4],[6,4],[6,7],[2,3]]"), 3)

    def test_3_empty(self):
        self.assertEqual(fc("[]"), 0)
        self.assertEqual(fc("[]"), 0)

    def test_4_invalid(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            fc("invalid_string")

if __name__ == '__main__':
    unittest.main()
