## Stock Analytics API
In this project an API server has been made which can fetch and store the live stock data using the yfinance libary. 
It can perform various stock related operations on the stock data, Data obtained is stored in POSTGRESQL using psycopg2 library
FASTapi has been used and all the endpoints can be accessed using SWAGGERUI 
## Live URL 
ingenious-dedication-production-ed26.up.railway.app/docs
## Endpoints 
1. " POST /stock/{symbol}/fetch" : used to store the stock data in database downloaded from yfinance library
2. "GET  /stock/{symbol}" : used to get all the data for a specific stock using stock symbol
3. "GET  /stock/{symbol}/sma " : used to calculate sma for the spcific stock symbol for a user defined period(by default 14)
4. "GET  /stock/{symbol}/ema " : used to calculate rolling ema for the spcific stock symbol for a user defined period(by default 14)
5. "GET  /stock/{symbol}/rsi " : used to calculate rsi for the specific stock symbol with a signal for the period of 14 days
6. "GET  /stock/{symbol}/summary" : displays all the esential data of the user input stock symbol
7. "GET  /stock/compare" : used to compare two stocks by giving the summary of both the stocks

## Tech Stack
fastapi
uvicorn
psycopg2-binary
yfinance
pydantic
pandas
## Project Structure
|   main.py
|   README.md
|   requirements.txt
|   schema.sql
|   schemas.py
|   
+---db
|   |   connection.py
|   |   queries.py
|   |   __init__.py
|   |   
|           
+---routers
|   |   stock.py
|   |   __init__.py
|   |   
|           
+---services
|   |   stock.py
|   |   __init__.py
|   |   
|   
## How to Run Locally
1. Clone the repo
   git clone https://github.com/krishvp10/stock-analytics-api.git

2. Install dependencies
   pip install -r requirements.txt

3. Create PostgreSQL database
   psql -U postgres -c "CREATE DATABASE stock;"

4. Run schema
   psql -U postgres -d stock -f schema.sql

5. Run the server
   uvicorn main:app --reload

   
