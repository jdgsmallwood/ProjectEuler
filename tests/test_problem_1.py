from project_euler_solutions import problem_1


class TestProblemOne:

    def test_example_given(self):
        """
        We are told in the question that summing natural numbers below 10 that are multiples of 3 or 5 gives 23
        :return:
        """
        answer = problem_1.sum_if_divisible_by_three_or_five(10)
        assert answer == 23

    def test_divisible_by(self):
        test_number = 42
        divisor = 7
        answer = problem_1.divisible_by(test_number, divisor)
        assert answer is True
