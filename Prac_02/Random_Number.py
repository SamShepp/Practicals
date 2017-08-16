import random
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 100
INITIAL_PRICE = 10.0
day = 0
OUTPUT_FILE = "string_formatting.txt"
out_file = open(OUTPUT_FILE, 'w')

# noinspection PyTypeChecker
print("Starting price: ${:,.2f}".format(INITIAL_PRICE), file=out_file)

price = INITIAL_PRICE

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day = day + 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(0, MAX_INCREASE)
    price *= (1 + price_change)
    # noinspection PyTypeChecker
    print("On day {} ${:,.2f}".format(day, price), file=out_file)
out_file.close()
