#!/usr/bin/python3

COMMISSION_RATE = 0.03
DECIMAL_DIGITS = 2

stock_symbol = input("The stock symbol: ")
shares = int(input("Number of shares: "))
buy_price = float(input("The stock buying price: "))
sell_price = float(input("The stock selling price: "))

total_buy_price = shares * buy_price
total_sell_price = shares * sell_price

buy_commission = total_buy_price * COMMISSION_RATE
sell_commission = total_sell_price * COMMISSION_RATE

profit_loss = total_sell_price - sell_commission - (total_buy_price + buy_commission)

print()
print(f"Transactions for stock: {stock_symbol}")

# We can use so-called f-strings for better control of the layout of the string
# (where spaces are added, punctuation etc).
print(f"Bought {shares} shares @ {buy_price}")
print(f"Paid {round(total_buy_price, DECIMAL_DIGITS)}")
print(f"Commission when buying: {round(buy_commission, DECIMAL_DIGITS)}")

print(f"Sold {shares} shares @ {sell_price}")
print(f"Received {round(total_sell_price, DECIMAL_DIGITS)}")
print(f"Commission when selling: {round(sell_commission, DECIMAL_DIGITS)}")

print(f"Profit or loss: {round(profit_loss, DECIMAL_DIGITS)}")
