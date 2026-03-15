import websockets
import asyncio
import json
from collections import deque
from config_loader import APP_CONFIG
from messenger import build_email
from evaluator import evaluate_currency_prices

async def stream_prices():
    """ Access Coinbase websocket and pull the currency data via a JSON block"""
    url = "wss://ws-feed.exchange.coinbase.com"

    #price_buffers = { 
    #    item['symbol']: deque(maxlen=300)
    #    for item in APP_CONFIG['watchlist'] 
    #} # Error: There is no watchlist currently in app_config

    while True:
        try:
            async with websockets.connect(url) as websocket:      
                print(f"Connected to live feed")

                await websocket.send(json.dumps(APP_CONFIG['subscribe_message']))
                print("Subscription sent successfully")

                # Start stream and keep it going
                while True:
                    response = await websocket.recv()
                    data = json.loads(response)

                    #print(data)

                    if(data.get('type') == 'ticker'):
                        price = data.get('price')
                        symbol = data.get('product_id')

                        # If the JSON has both the currency symbol and a price, print the data and evaluate buy option
                        if symbol and price:
                            level, value = evaluate_currency_prices(symbol, price)

                            #print(APP_CONFIG['watchlist'].get(symbol)['ceiling_target_price'])

                            #price_buffers[symbol].append(price)
                            #print(price_buffers)

                            if (value == 1):
                                build_email(symbol, price, level)

                    elif data.get('type') == 'heartbeat':
                        # We don't need to print this, but it proves we're alive
                        pass
                    else:
                        print("Other types: ", data.get('type'))

        except websockets.exceptions.ConnectionClosed:
            print("Connection failed") # Place to attempt reconnect
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Connection Ended: {e}") # Error with reason