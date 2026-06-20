from pydantic import BaseModel

class FetchRequest(BaseModel):
    period: int = 3

class SMAResponse(BaseModel):
    symbol: str
    period: int
    sma: float

class EMAResponse(BaseModel):
    symbol: str
    period: int
    ema: float

class RSIResponse(BaseModel):
    symbol: str
    rsi: float
    signal: str

class SummaryResponse(BaseModel):
    symbol: str
    latest_price: float
    sma: float
    ema: float
    rsi: float
    signal: str            