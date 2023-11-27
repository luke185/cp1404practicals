import random

RANDOM_NUMBER_AMOUNT = 6
RANDOM_NUMBER_LOW = 1
RANDOM_NUMBER_HIGH = 45
number_list = [number for number in range(RANDOM_NUMBER_LOW, RANDOM_NUMBER_HIGH + 1)]

quick_picks_count = int(input("How many quick picks? "))
for i in range(quick_picks_count):
    quick_picks = []
    random.shuffle(number_list)
    quick_picks += number_list[:RANDOM_NUMBER_AMOUNT]
    quick_picks.sort()
    for j in range(RANDOM_NUMBER_AMOUNT):
        print(f"{quick_picks[j]:2}", end=' ')
    print()
