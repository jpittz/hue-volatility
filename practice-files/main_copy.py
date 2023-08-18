import yfinance as yf
import time

class Stock:

    prices = []

    def __init__(self, symbol):
        self.symbol = symbol
        self.info = yf.Ticker(symbol).info
        self.name = self.info['shortName']

    def getPrice(self, symbol):
        self.price = yf.Ticker(symbol).info['currentPrice']
        self.formattedPrice = str("{:.2f}".format(self.price))
        self.prices.append(float(self.formattedPrice))

def volatility(stock):
    # loop and update prices
    print("\nLive Prices\n-----------\n")
    stock.getPrice(stock.info['symbol'])

    for i in range(1,10):
        stock.getPrice(stock.info['symbol']) # get latest price
        print("Price: ", stock.formattedPrice) # print latest price as string for price format
        print("Change: ", priceChange(stock.prices), end = '\n\n') # print direction of change
        time.sleep(2) # delay to fetch new price

def priceChange(prices):
    if prices[-1] > prices[-2]:
        return ("+")
    elif prices[-1] < prices[-2]:
        return ("-")
    elif prices[-1] == prices[-2]:
        return ("=")

def main():
    print("\nHue Volatility\n\n//////////////\n")

    # s1 being first stock used
    s1 = Stock("AAPL")

    # output company name and ticker
    print("Ticker : ", s1.info['symbol'])
    print("Company : ", s1.info['shortName'], end = '\n\n')

    volatility(s1)

main()
