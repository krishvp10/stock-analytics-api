from fastapi import APIRouter, HTTPException
from schemas import FetchRequest, SMAResponse, EMAResponse, RSIResponse, SummaryResponse
import services.stock as service
import db.connection as dc
import db.queries as dq

router = APIRouter()

@router.post("/stock/{symbol}/fetch")
def fetch_stock(symbol: str, request: FetchRequest):
    conn = dc.get_connection()
    try:
        records = service.fetch_and_store(conn, symbol, request.period)
        if records == 0:
            raise HTTPException(status_code=404, detail="No data found for this symbol")
        return {"message": "Data fetched successfully", "symbol": symbol, "records_stored": records}
    finally:
        conn.close()

@router.get("/stock/{symbol}/sma", response_model=SMAResponse)
def get_sma(symbol: str, period: int = 14):
    conn = dc.get_connection()
    try:
        sma_value = service.calculate_sma(conn, symbol, period)
        if sma_value is None:
            raise HTTPException(status_code=404, detail="SMA not found for this symbol and period")
        return SMAResponse(symbol=symbol, period=period, sma=sma_value)
    finally:
        conn.close()

@router.get("/stock/{symbol}/ema", response_model=EMAResponse)
def get_ema(symbol: str, period: int = 14):
    conn = dc.get_connection()
    try:
        ema_value = service.calculate_ema(conn, symbol, period)
        if ema_value is None:
            raise HTTPException(status_code=404, detail="EMA not found for this symbol and period")
        return EMAResponse(symbol=symbol, period=period, ema=ema_value)
    finally:
        conn.close()

@router.get("/stock/{symbol}/rsi", response_model=RSIResponse)
def get_rsi(symbol: str):
    conn = dc.get_connection()
    try:
        rsi_value, signal = service.calculate_rsi(conn, symbol, 14)
        if rsi_value is None or signal is None:
            raise HTTPException(status_code=404, detail="RSI not found for this symbol")
        return RSIResponse(symbol=symbol, rsi=rsi_value, signal=signal)
    finally:
        conn.close()

@router.get("/stock/{symbol}/summary", response_model=SummaryResponse)
def get_summary(symbol: str):
    conn = dc.get_connection()
    try:
        summary = service.get_summary(conn, symbol)
        return summary
    finally:
        conn.close()

@router.get("/stock/compare")
def compare_stocks(s1: str, s2: str):
    conn = dc.get_connection()
    try:
        data1 = service.get_summary(conn, s1)
        data2 = service.get_summary(conn, s2)
        if not data1 or not data2:
            raise HTTPException(status_code=404, detail="No data found for one or both symbols")
        return {"symbol1": s1, "data1": data1, "symbol2": s2, "data2": data2}
    finally:
        conn.close()          

@router.get("/stock/{symbol}")
def get_stock(symbol: str):
    conn = dc.get_connection()
    try:
        data = dq.get_stock(conn, symbol)
        if not data:
            raise HTTPException(status_code=404, detail="No data found for this symbol")
        return {"symbol": symbol, "data": data}
    finally:
        conn.close()

      