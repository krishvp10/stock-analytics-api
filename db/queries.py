

def insert_data(conn,symbol,df):
    cursor = conn.cursor()
    Date = list(df.index)
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
        cursor.execute("INSERT INTO stock_data (symbol, date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (symbol, date) DO NOTHING",
                       (symbol, Date[i], Open[i], High[i], Low[i], Close[i], Volume[i]))
    conn.commit()
    cursor.close()
    

def get_stock(conn,symbol):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock_data WHERE symbol = %s ORDER BY date",(symbol,))
    data = cursor.fetchall()
    cursor.close()
    return data

def latest_price(conn,symbol):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock_data WHERE symbol = %s ORDER BY date DESC LIMIT 1", (symbol,))
    data = cursor.fetchone()
    cursor.close()    
    return data

def symbol_exist(conn,symbol):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM stock_data WHERE symbol = %s",(symbol,))
    count = cursor.fetchone()
    cursor.close()
    return count[0] > 0