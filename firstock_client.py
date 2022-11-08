from thefirstock import thefirstock
import requests, json, time

BASE_URL = "https://connect.thefirstock.com/apiV2"


routes = {
    "user.login" : "/login",
    "order.place": "/placeOrder",
    "order.history": '/singleOrderHistory',
    "order.position_book" : "/positionBook",
    'order.optiongreeks': "/optionGreek",
    'market.ohlc_data': "/timePriceSeries"

}

# Constant
# Products
PRODUCT_MIS = "MIS"
PRODUCT_NRML = "NRML"

# Order types
ORDER_TYPE_MARKET = "MKT"
ORDER_TYPE_LIMIT = "LMT"
ORDER_TYPE_STOPMARKET = "SL-MKT"
ORDER_TYPE_STOPLIMIT = "SL-LMT"

# Transaction type
TRANSACTION_TYPE_BUY = "B"
TRANSACTION_TYPE_SELL = "S"

# Squareoff mode
SQUAREOFF_DAYWISE = "DayWise"
SQUAREOFF_NETWISE = "Netwise"

# Squareoff position quantity types
SQUAREOFFQUANTITY_EXACTQUANTITY = "ExactQty"
SQUAREOFFQUANTITY_PERCENTAGE = "Percentage"

# Validity
VALIDITY_DAY = "DAY"

# Exchange Segments
EXCHANGE_NSECM = "NSE"
EXCHANGE_NSEFO = "NFO"

#Login
def login_client(userID, password, TOTP, vendorCode, apikey):

    body = {
  "userId": str(userID),
  "password": str(password),
  "TOTP": str(TOTP),
  "vendorCode": str(vendorCode),
  "apiKey": str(apikey)
}

    head = {

    'Content-Type' : 'application/json'

 }

    url = BASE_URL + routes['user.login']

    res = requests.post(url, json=body, headers=head)

    print(res.json()['data']['userName'])

    token = res.json()['data']['susertoken']
    
    print(token)

    return token


#Place Order
def place_order(auth_token,userID, tsym,orderside,ordertype, qty,exchange="NFO", producttype="M", limitprice=0, stopprice=0):

    body = {
  "userId": userID,
  "exchange": exchange,
  "tradingSymbol": tsym,
  "quantity": qty,
  "price": limitprice,
  "product": producttype,
  "transactionType": orderside,
  "priceType": ordertype,
  "retention": "DAY",
  "triggerPrice": stopprice,
  "remarks": "ALGO",
  "jKey": auth_token
    }

    head = {
        'Content-Type' : 'application/json'
    }

   
    url = BASE_URL + routes['order.place']

    res = requests.post(url, json=body, headers=head)

    print(res.json())

    return res.json()['data']['orderNumber']


def order_history(auth_token, userID, orderID):
    body = {
  "userId": userID,
  "jKey": auth_token,
  "orderNumber": orderID
}

    head = {
        'Content-Type' : 'application/json'
    }

    url = BASE_URL + routes['order.history']

    res = requests.post(url, json=body, headers=head)

    print(res.json())

    return res.json()

def position_book(auth_token, userID):

    body = {
  "userId": userID,
  "jKey": auth_token
}

    head = {
        'Content-Type' : 'application/json'
    }

    url = BASE_URL + routes['order.position_book']

    res = requests.post(url, json=body, headers=head)

    print(res.json()['data'])

    return res.json()['data']


def option_greeks(auth_token, expiryDate, strikePrice, spotPrice, initRate, vol, optionType):
    body = {
  "expiryDate": expiryDate,
  "strikePrice": strikePrice,
  "spotPrice": spotPrice,
  "initRate": initRate,
  "volatility": vol,
  "optionType": optionType,
  "jKey": auth_token
}
    head = {
        'Content-Type' : 'application/json'
    }

    url = BASE_URL + routes['order.optiongreeks']

    res = requests.post(url, json=body, headers=head)

    print(res.json())

    return res.json()



#Market Connect

def get_quote(auth_token,userID, token, exchange="NFO"):

    body = {
  "userId": "string",
  "exchange": "string",
  "token": "string",
  "jKey": "string"
}

    head = {
        'Content-Type' : 'application/json'
    }

def intraday_ohlc():
    
    body = {
  "userId": "string",
  "exchange": "string",
  "token": "string",
  "endtime": "string",
  "starttime": "string",
  "intrv": "string",
  "jKey": "string"
}

    head = {
        'Content-Type' : 'application/json'
    }

    url = BASE_URL + routes['market.ohlc_data']

    res = requests.post(url, json=body, headers=head)

    print(res.json())

    return res.json()








    


    

    


