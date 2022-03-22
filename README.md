[![Logo](./logo.png)](https://bitmart.com)

BitMart-Python-SDK-API
=========================
<p align="left">
    <a href='#'><img src='https://travis-ci.org/meolu/walle-web.svg?branch=master' alt="Build Status"></a>  
</p>

Python client for the [BitMart Cloud API](http://developer-pro.bitmart.com).

Installation
=========================

* 1.Python 3.6+ support

* 2.Clone
```git
git clone https://github.com/bitmartexchange/bitmart-python-sdk-api.git
pip3 install -r requirements.txt
```

* 3.Run 
```bash
sudo python3 getTokenPairLastPrice.py
```


Usage
=========================
* An example of a spot trade API
* Replace it with your own API KEY
* Run

#### API Example
```python
from bitmart.api_spot import APISpot

if __name__ == '__main__':

    api_key = "Your API KEY"
    secret_key = "Your Secret KEY"
    memo = "Your Memo"

    spotAPI = APISpot(api_key, secret_key, memo, timeout=(3, 10))

    spotAPI.post_submit_limit_buy_order('BTC_USDT', size='0.01', price='8800')
```



#### WebSocket Public Channel Example
```python

from bitmart import cloud_consts
from bitmart.cloud_ws_client import CloudWSClient
from bitmart.ws_spot import create_channel, create_spot_subscribe_params


class WSTest(CloudWSClient):

    def on_message(self, message):
        print(f'[ReceiveServerMessage]-------->{message}')


if __name__ == '__main__':
    ws = WSTest(cloud_consts.WS_URL, "", "", "")
    ws.set_debug(True)
    channels = [
        # public channel
        create_channel(cloud_consts.WS_PUBLIC_SPOT_TICKER, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_KLINE_1M, 'BTC_USDT'),
        create_channel(cloud_consts.WS_PUBLIC_SPOT_DEPTH5, 'BTC_USDT')
    ]

    ws.spot_subscribe_without_login(create_spot_subscribe_params(channels))

```
