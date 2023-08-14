import yfinance as yf
import time

def volatility(symbol):
    # loop and update prices
    print("Live Prices\n-----------\n")
    prices = [getPrice(symbol)]

    for i in range(1,10):
        # get and store latest price
        prices.append(getPrice(symbol))
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

def getPrice(symbol):
    # get new market data to update price
    stock = yf.Ticker(symbol).info

    # return current price rounded to 2dp
    return round(stock['currentPrice'], 2)

def main():
    print("\nHue Volatility\n\n//////////////\n")

    symbol = "NVDA" # set stock ticker to use
    stock = yf.Ticker(symbol).info # get data for stock

    # output company name and ticker
    print("Ticker : ", stock['symbol'])
    print("Company : ", stock['shortName'], end = '\n\n\n')

    # run volatility function
    volatility(symbol)

# run code
main()
