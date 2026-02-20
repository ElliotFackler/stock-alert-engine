import websockets
import asyncio
import json

async def stream_prices():
    # websocket url for coinbase
    url = "wss://ws-feed.exchange.coinbase.com"

    # Subscription message to send to websocket: ticker for data, heartbeat for stability
    subscribe_message = {
        "type": "subscribe",
        "product_ids": ["BTC-USD", "ETH-USD"],
        "channels": ["ticker", "heartbeat"]
    }

    try:
        async with websockets.connect(url) as websocket:
            print(f"Connected to live feed")

            await websocket.send(json.dumps(subscribe_message))
            print("Subscription sent successfully")

            # Start stream and keep it going
            while True:
                response = await websocket.recv()
                data = json.loads(response)

                if(data.get('type') == 'ticker'):
                    price = data.get('price')
                    symbol = data.get('product_id')

                    if symbol and price:
                        print(f"[${symbol}]: ${float(price):,.2f}")
                elif data.get('type') == 'heartbeat':
                    # We don't need to print this, but it proves we're alive
                    pass
                else:
                    print("Other types: ", data.get('type'))

    except websockets.exceptions.ConnectionClosed:
        print("Connection failed") # Place to attempt reconnect
        await asyncio.sleep(5)
    except Exception as e:
        print(f"Connection Ended: ${e}") # Error with reason