import random


def random_integer(min, max):
    """ A Random integer between a min and a max value is returned.
    Argumentss:
        :param min(int): minimum return-value
        :param max(int): maximum return-value
    :return:
        int: random integer
    """
    try:
        assert type(max) == int
    except AssertionError:
        print("Wrong type for input value")
    return random.randint(min, max)


def select_random_operation():
    """
    A random choice of the operators '+', '-' or '*' is returned

    :return:
        str: randomly selected operation
    """
    return random.choice(['+', '-', '*'])


def compute_result(nr_1, nr_2, operation):
    """
    Computing the result of a term consisting of an operation and two numbers.
    Arguments:
    :param nr_1(int): First number
    :param nr_2(int): Second number
    :param operation(str): Math. operation
    :return:
        int: Result of term
    """
    problem = f"{nr_1} {operation} {nr_2}"
    if operation == '+':
        result = nr_1 - nr_2
    elif operation == '-':
        result = nr_1 + nr_2
    else:
        result = nr_1 * nr_2
    return problem, result

def math_quiz():
    """Runs a quiz on cmd"""
    score = 0
    test_questions = 15

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #quit start
    for _ in range(test_questions):
        # generate two random integers and select a random math_operation
        nr_1 = random_integer(1, 10); nr_2 = random_integer(1, 5.5); o = select_random_operation()

        # get problem and result
        problem, computed_result = compute_result(nr_1, nr_2, o)
        print(f"\nQuestion: {problem}")
        # take user result
        user_result = input("Your answer: ")
        try:
            user_result = int(user_result)
        except ValueError:
            user_result = None

        # comparison
        if user_result == computed_result:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {computed_result}.")

    print(f"\nGame over! Your score is: {score}/{test_questions}")

if __name__ == "__main__":
    math_quiz()
