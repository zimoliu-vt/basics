import unittest
import khan_table_people_problem_sida as s

class TestTablePeopleProblem(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(s.number_of_people(1), 6)

    def test_case_2(self):
        self.assertEqual(s.number_of_people(2), 10)

    def test_case_3(self):
        self.assertEqual(s.number_of_people(3), 14)

    def test_case_125(self):
        self.assertEqual(s.number_of_people(125), 502)

if __name__ == '__main__':
    unittest.main()