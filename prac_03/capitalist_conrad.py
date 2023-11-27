import random

MAX_PERCENTAGE_INCREASE = 0.1
MIN_PERCENTAGE_INCREASE = 0

MAX_PERCENTAGE_DECREASE = 0.05
MIN_PERCENTAGE_DECREASE = 0

MIN_PRICE = 1
MAX_PRICE = 100

OUTPUT_FILE = 'output.txt'

price = 10.00
number_of_days = 1
out_file = open(OUTPUT_FILE, 'w')
while MAX_PRICE >= price >= MIN_PRICE:
    change_chance = random.randint(1, 100)
    if change_chance > 50:
        price = price + (price * random.uniform(MIN_PERCENTAGE_INCREASE, MAX_PERCENTAGE_INCREASE))
    else:
        price = price - (price * random.uniform(MIN_PERCENTAGE_DECREASE, MAX_PERCENTAGE_DECREASE))
    print(f"On day {number_of_days} price is: ${price:.2f}", file=out_file)
    number_of_days = number_of_days + 1
out_file.close()