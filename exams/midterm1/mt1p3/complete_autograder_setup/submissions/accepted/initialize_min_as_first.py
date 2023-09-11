#!/usr/bin/python3

DIGITS = 1
MAX_PRICE = 1000.0

total_price = 0.0
num_items = 0

price = float(input())
min_price = price
while price > 0:
    num_items += 1
    total_price += price

    if price < min_price:
        min_price = price

    price = float(input())

print("Number of items:", num_items)
print("Total price:", round(total_price, DIGITS))
if num_items > 0:
    print("Lowest price:", min_price)
