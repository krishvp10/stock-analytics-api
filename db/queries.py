import db.connection as db
import yfinance as yf
def insert_data(conn,symbol,df):
    cursor = conn.cursor()
    Date =[]
    for i in range(len(df["Date"])):
        Date.append(df["Date"][i])
    Open = []
    for i in range(len(df["Open"])):
        Open.append(df["Open"][i])
    High = []
    for i in range(len(df["High"])):
        High.append(df["High"][i])
    Low = []
    for i in range(len(df["Low"])):
        Low.append(df["Low"][i])
    Close = []
    for i in range(len(df["Close"])):
        Close.append(df["Close"][i])
    Volume = []
    for i in range(len(df["Volume"])):
        Volume.append(df["Volume"][i])
    for i in range(len(Date)):
        cursor.execute("INSERT INTO stock_data (symbol, date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (symbol, Date[i], Open[i], High[i], Low[i], Close[i], Volume[i]))
    conn.commit()
    cursor.close()
    