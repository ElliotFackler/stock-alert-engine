# Global variables
PRICE_DICT = {'BTC-USD': 60000, 'ETH-USD': 2000}
GOAL_DICT = {'BTC-USD': False, 'ETH-USD': False}

def evaluator(symbol, price):
    global PRICE_DICT
    global GOAL_DICT

    if (float(price) > PRICE_DICT.get(symbol) and GOAL_DICT[symbol] == False):
        GOAL_DICT[symbol] = True
        return GOAL_DICT.get(symbol)
    return False
        
