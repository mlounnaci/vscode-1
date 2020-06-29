import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10,50)
        self.assertEqual(result, 61)


if __name__ == "__main__":
    unittest.main()