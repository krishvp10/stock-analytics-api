import db.queries as db
import yfinance as yf
def fetch_and_store(conn,sym,per):
    df = yf.download(sym, period=f'{per}mo')
    db.insert_data(conn,sym,df)
    return len(df)

def calculate_sma(conn,symbol,window):
    data = db.get_stock(conn,symbol)
    close_prices = [row[6] for row in data]
    sma = sum(close_prices[-window:]) / window
    return sma

def calculate_ema(conn,symbol,window):
    previous_ema = None
    data = db.get_stock(conn,symbol)
    close_prices = [row[6] for row in data]
    alpha = 2 / (window + 1)
    for price in close_prices:
        if previous_ema is None:
            previous_ema = price
        else:
            previous_ema = (price * alpha) + (previous_ema * (1 - alpha))
    return previous_ema

def calculate_rsi(conn,symbol,window):
    data = db.get_stock(conn,symbol)
    close_prices = [row[6] for row in data]
    gains = []
    losses = []
    for i in range(1, len(close_prices)):
        change = close_prices[i] - close_prices[i - 1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(-change)
    avg_gain = sum(gains[-window:]) / window
    avg_loss = sum(losses[-window:]) / window
    if avg_loss == 0:
        return 100, "Overbought"  
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    if rsi > 70:
        signal = "Overbought"
    elif rsi < 30:
        signal = "Oversold"
    else:
        signal = "Neutral"
    return rsi, signal

def get_summary(conn,symbol):
    rsi, signal = calculate_rsi(conn, symbol, 14)
    latest_row = db.latest_price(conn, symbol)
    latest_price = latest_row[6]  
    return{
        "symbol" : symbol,
        "latest_price" : latest_price,
        "ema" : calculate_ema(conn,symbol,14),
        "sma" : calculate_sma(conn,symbol,14),
        "rsi" : rsi,
        "signal" : signal

    }