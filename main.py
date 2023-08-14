import yfinance as stock
import time
from decimal import *

def volatility():
    # loop and update prices
    print("Live Prices\n-----------\n")
    prices = [getPrice()]

    for i in range(1,10):

        # get and store latest price
        prices.append(getPrice())
        # print latest price as string for price format
        print("\nPrice : ", str("{:.2f}".format(prices[i])))
        print("Change : ", priceChange(prices, i)) # print direction of change
        time.sleep(2) # delay to fetch new price

def priceChange(prices, i):
    if prices[i] > prices[i - 1]:
        return ("+")
    elif prices[i] < prices[i - 1]:
        return ("-")
    elif prices[i] == prices[i - 1]:
        return ("=")
    else:
        return ("ERROR")

def getPrice():
    # get new market data to update price
    apple = stock.Ticker("AAPL").info

    # return current price rounded to 2dp
    return round(apple['currentPrice'], 2)

def main():
    print("\nHue Volatility\n\n//////////////\n")

    # get data for stock
    apple = stock.Ticker("AAPL").info

    # output company name and ticker
    print("Ticker : ", apple['symbol'])
    print("Company : ", apple['shortName'], end = '\n\n\n')

    volatility()

# run code
main()
