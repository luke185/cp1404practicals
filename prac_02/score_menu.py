"""Score menu program"""

MENU = "(G)et a valid score | (P)rint result | (S)how stars | (Q)uit"


def main():
    score = 0
    print(MENU)
    choice = input("> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"With a score of {score} your result is {result}")
        elif choice == 'S':
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input("> ").upper()
    print("Thank you.")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print('Score must be between 0 and 100 inclusive')
        score = int(input("Enter score: "))
    return score


def determine_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    print('*' * score)


main()
