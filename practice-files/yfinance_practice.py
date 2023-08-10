import yfinance as stock
import time

# first attempt at using yfinance
print("yfinance practice\n")

# get data for Apple
apple = stock.Ticker("AAPL").info

# display Company Sector
print("Company Sector : ", apple['sector'])

# display Current Price
print("Current Price : ", apple['currentPrice'])

# delay
time.sleep(10)

# get new market data to update price
apple = stock.Ticker("AAPL").info

# display Current Price
price = "{:.2f}".format(round(apple['currentPrice'], 2))
print(price)
