import guessing
import unittest

class TestGuess(unittest.TestCase):
    def test_simple(self):
        for pin in guessing.generating_all_possible_pins(5):
            self.assertEqual(pin, "00000")
            break

    

if __name__ == '__main__':
    unittest.main()