from config_loader import APP_CONFIG
# Global variables
CEILING_DICT = {'BTC-USD': 60000, 'ETH-USD': 2000}
FLOOR_DICT = {'BTC-USD': 55000, 'ETH-USD': 1500}
CEILING_GOAL_DICT = {'BTC-USD': False, 'ETH-USD': False}
FLOOR_GOAL_DICT = {'BTC-USD': False, 'ETH-USD': False}

def evaluate_currency_prices(symbol, price):
    """Check whether cryptocurrency price has fallen below set floor price or risen above set ceiling price"""
    global CEILING_DICT
    global CEILING_GOAL_DICT
    global FLOOR_DICT
    global FLOOR_GOAL_DICT

    #print("HERE")
    #print(APP_CONFIG[symbol])

    if (float(price) > CEILING_DICT.get(symbol) and CEILING_GOAL_DICT[symbol] == False):
        CEILING_GOAL_DICT[symbol] = True
        return "Ceiling", CEILING_GOAL_DICT.get(symbol)
    elif (float(price) < FLOOR_DICT.get(symbol) and FLOOR_GOAL_DICT[symbol] == False):
        FLOOR_GOAL_DICT[symbol] = True
        return "Floor", FLOOR_GOAL_DICT.get(symbol)
    else:
        return "None", False
        
