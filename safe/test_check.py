import check
import unittest

class TestCheckOK(unittest.TestCase):

    def test_case_1(self):
        test_pin = "123"
        check.set_real_pin(test_pin)
        result = check.check(test_pin)
        self.assertEqual(result, True)


    def test_case_wrong_guess(self):
        right_pin = "99887"
        wrong_pin = "987"
        check.set_real_pin(right_pin)
        result = check.check(wrong_pin)
        self.assertEqual(result, False)

    def test_case_2(self):
        test_pin = "12343"
        check.set_real_pin(test_pin)
        result = check.check(test_pin)
        self.assertEqual(result, True)


    def test_case_wrong_guess_1(self):
        right_pin = "994587"
        wrong_pin = "9357"
        check.set_real_pin(right_pin)
        result = check.check(wrong_pin)
        self.assertEqual(result, False)    
    

if __name__ == '__main__':
    unittest.main()