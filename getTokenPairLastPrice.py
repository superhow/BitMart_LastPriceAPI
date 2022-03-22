from bitmart.api_contract import APIContract
from tests import data as data
import Aphid
import sys
import time

# contract api
contractAPI = APIContract(data.api_key, data.secret_key, data.memo, data.url)

def checkAuthenticationErrors():
    assert (contractAPI.get_ticker(contract_symbol=str(sys.argv[1]))[0]['code'] == 1000), contractAPI.get_ticker(contract_symbol=str(sys.argv[1]))[0]['message']

def print_user_data():
    APIdata = get_last_price()
    lastPrice = Aphid.findall(APIdata, "last_price")
    indexPrice = Aphid.findall(APIdata, "index_price")
    priceChangePercent24h = Aphid.findall(APIdata, "price_change_percent_24h")
    print(lastPrice, indexPrice, priceChangePercent24h)

def get_last_price():
    """Test GET https://api-cloud.bitmart.com/contract/v1/tickers"""
    checkAuthenticationErrors()
    return(contractAPI.get_ticker(contract_symbol=str(sys.argv[1]))[0])

while True:
    print_user_data()
    time.sleep(30)