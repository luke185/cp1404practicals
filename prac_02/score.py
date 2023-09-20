import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"Your result is {result}")
    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score} Random result: {random_result}")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
