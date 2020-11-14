"""
This is Problem 1 of Project Euler.
"""


def divisible_by(number, divisor):
    """
    Is x divisible by y?
    :param number: number to be divided
    :param divisor: divisor
    :return: true/false
    """
    if number % divisor == 0:
        return True
    else:
        return False


def sum_if_divisible_by_three_or_five(max_number):
    """
    This will actually get the sum.
    :param max_number:
    :return:
    """
    total_sum = 0
    for i in range(1, max_number):
        if divisible_by(i, 3) or divisible_by(i, 5):
            total_sum += i
    return total_sum


def main():
    target_number = 1000
    total_sum = sum_if_divisible_by_three_or_five(target_number)
    print(f"The sum is {total_sum}.")


if __name__ == '__main__':
    main()
