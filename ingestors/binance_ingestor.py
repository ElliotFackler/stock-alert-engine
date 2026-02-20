import websockets
import json

async def stream_prices():
    # Binance public websocket URL for specific assets
    url = "wss://stream.binance.us:9443/ws/btcusdt@ticker/ethusdt@ticker"

    try:
        # Connect to the websocket
        async with websockets.connect(url) as websocket:
            print(f"Connected to live feed")

            # Keep connection
            while True:
                message = await websocket.recv()
                data = json.loads(message)

                # Binance returns a dictionary, grab symbols and prices
                symbol = data.get('s')
                price = data.get('c')

                # Print the symbol and its corresponding price
                if symbol and price:
                    print(f"[{symbol}] Price: ${float(price):,.2f}")
                    
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed") # Place to include reconnect attempt
    except Exception as e: # Prints reason for failure
        print(f"Connection failed: ${e}")