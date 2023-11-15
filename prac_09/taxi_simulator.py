from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    """Program to simulate choosing a taxi"""
    taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 200, 4)]
    current_taxi = None
    bill_to_date = 0.00

    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'C':
            current_taxi = choose_taxi(taxis)
        elif choice == 'D':
            if current_taxi is None:
                print('You need to choose a taxi before you can drive')
            else:
                bill_to_date += drive(current_taxi)
        else:
            print('Invalid Choice')
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input('>>> ').upper()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print('Taxis are now: ')
    display_taxis(taxis)


def drive(taxi):
    taxi.start_fare()
    distance = int(input('Drive how far? '))
    taxi.drive(distance)
    price = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${price:.2f}")
    return price


def choose_taxi(taxis):
    display_taxis(taxis)
    choice = get_valid_taxi(taxis)
    return choice


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_taxi(taxis):
    while True:
        try:
            choice = int(input("Choose taxi: "))
            if choice < 0:
                print('Invalid taxi choice')
            else:
                chosen_taxi = taxis[choice]
                break
        except IndexError:
            print('Invalid taxi choice')
        except ValueError:
            print('Invalid taxi choice')
    return chosen_taxi


if __name__ == '__main__':
    main()
