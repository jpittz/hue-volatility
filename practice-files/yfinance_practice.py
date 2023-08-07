import yfinance as yahooFinance

# first attempt at using yfinance
print("yfinance practice\n")

# get data for Apple
apple = yahooFinance.Ticker("AAPL").info

# display Company Sector
print("Company Sector : ", apple['sector'])

# display Current Price
print("Current Price : ", apple['currentPrice'])
