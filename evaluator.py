from config_loader import APP_CONFIG

#TODO: Convert variables in evaluator over to appconfig

def evaluate_currency_prices(symbol, price):
    """Check whether cryptocurrency price has fallen below set floor price or risen above set ceiling price"""

    if (float(price) > APP_CONFIG['watchlist'].get(symbol)['ceiling_target_price'] and APP_CONFIG['watchlist'].get(symbol)['alert_sent'] == 0):
        APP_CONFIG['watchlist'].get(symbol)['alert_sent'] = 1
        return "Ceiling", APP_CONFIG['watchlist'].get(symbol)['alert_sent']
    elif (float(price) < APP_CONFIG['watchlist'].get(symbol)['floor_target_price'] and APP_CONFIG['watchlist'].get(symbol)['alert_sent'] == 0):
        APP_CONFIG['watchlist'].get(symbol)['alert_sent'] = 1
        return "Floor", APP_CONFIG['watchlist'].get(symbol)['alert_sent']
    else:
        return "None", 0
        
