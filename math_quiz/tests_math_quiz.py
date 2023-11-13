import unittest
from math_quiz import random_integer, select_random_operation, compute_result


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operation(self):
        # Test if random operation are either +, - or *
        for _ in range(1000):  # Test a large number of random values
            rand_op = select_random_operation()
            self.assertTrue((rand_op in ['+', '-', '*']))

    def test_compute_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (33, 12, '+', '33 + 12', 45),
                (33, 12, '-', '33 - 12', 21),
                (33, 12, '*', '33 * 12', 396),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                test_problem, test_result = compute_result(num1, num2, operator)
                self.assertTrue(test_problem == expected_problem)
                self.assertTrue(test_result == expected_answer)

if __name__ == "__main__":
    unittest.main()
