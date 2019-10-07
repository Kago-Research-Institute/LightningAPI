import pybitflyer

api = pybitflyer.API()
ticker = api.ticker(product_code="BTC_JPY")
print(ticker)