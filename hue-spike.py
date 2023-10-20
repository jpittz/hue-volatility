import yfinance as yf
import time
from phue import Bridge

#### --- CODE FOR HUE --- ###

global sleepTime
global spikeInterval

def hueSetup():
    global b
    b = Bridge('')  # b = Bridge('ip_of_your_bridge')

    # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
    # b.connect()

    global lights
    lights = [11, 12]  # Use lights you want

    return None

# flashes light the given hex value
def flash(colour):
    b.set_light(lights, {'on' : True, 'bri' : 254, 'xy' : convertColor(colour)})
    time.sleep(0.7)
    b.set_light(lights, 'on', False)

# allows easy use of rgb instead of xy from phue library
def convertColor(hexCode):
    R = int(hexCode[:2], 16)
    G = int(hexCode[2:4], 16)
    B = int(hexCode[4:6], 16)

    total = R + G + B

    if R == 0:
        firstPos = 0
    else:
        firstPos = R / total

    if G == 0:
        secondPos = 0
    else:
        secondPos = G / total

    return [firstPos, secondPos]

### --- CODE FOR STOCK --- ###

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

    for i in range(1,100): ### 100 is temporary value
        stock.getPrice(stock.info['symbol']) # get latest price
        print("Price: ", stock.formattedPrice) # print latest price as string for price format
        priceSpike(stock.prices) # run priceSpike function

        time.sleep(sleepTime) # delay to fetch new price

def priceSpike(prices):
    spike = 5.0  #float, threshold % to recognise a 'spike'

    # calculates % change between two latest prices (will change later)
    percentageChange = prices[-1]/prices[(-1)*(spikeInterval+1)]

    # calculates % multiplier
    if percentageChange > 1:
        percentageChange -= 1 # increase
    elif percentageChange < 1:
        percentageChange = (1 - percentageChange) * -1 # decrease
    else:
        percentageChange = 0

    # converts % multiplier to percentage
    percentageChange *= 100

    # checks for spike up
    if percentageChange >= spike:
        print("+\n")
        flash('04ff02')  # green

    # checks for spike down
    elif percentageChange <= (1 - spike):
        print("-\n")
        flash('ff361f')  # red

    # outputs actual % change to 2dp
    print("Percentage Change: ", str("{:.2f}".format(percentageChange)), "%")

    print("Change: ", end='')  # avoids repeating for all 3 if statements

    # prints +/-/= for change and flashes corresponding colour
    if prices[-1] > prices[-2]:
        print("+\n")
        flash('04ff02')  # green

    elif prices[-1] < prices[-2]:
        print("-\n")
        flash('ff361f')  # red

    elif prices[-1] == prices[-2]:
        print("=\n")
        flash('fefe00') # yellow

    return None

def spikeSetup(stock):
    # Note: interval set to 10 seconds for now
    spikeInterval = 10
    sleepTime = 2

    for i in range(1, spikeInterval/sleepTime):
        stock.getPrice(stock.info['symbol']) # get latest price
        time.sleep(sleepTime) # delay to fetch new price

    volatility(stock)

### --- MAIN --- ###

def main():
    hueSetup()
    print("\nHue Volatility\n\n//////////////\n")

    # s1 being first stock used
    s1 = Stock("AAPL")

    # output company name and ticker
    print("Ticker : ", s1.info['symbol'])
    print("Company : ", s1.info['shortName'], end = '\n\n')

    #volatility(s1)
    spikeSetup(s1)

main()
