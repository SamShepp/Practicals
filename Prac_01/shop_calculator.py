price_of_item = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item += float(input("Price of item: "))
if price_of_item >= 100:
    price_of_item -= price_of_item * 0.1
print("Total price for {} items is {:.2f}".format(number_of_items, price_of_item))