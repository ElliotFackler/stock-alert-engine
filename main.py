import asyncio
from ingestors import binance_ingestor, coinbase_ingestor

if __name__ == "__main__":
    try:
        # Event loop to allow asynchronous run
        asyncio.run(coinbase_ingestor.stream_prices())
    except KeyboardInterrupt:
        print("Program exited by user")
