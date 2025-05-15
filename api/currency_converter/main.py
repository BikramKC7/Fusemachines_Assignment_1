from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

API_KEY = "your_real_api_key_here"
API_URL = f"https://api.exchangerate-api.com/v4/latest/USD"  # example API

valid_currencies = set()

class ConvertRequest(BaseModel):
    amount: float
    from_currency: str
    to_currency: str

@app.on_event("startup")
async def load_currencies():
    global valid_currencies
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            valid_currencies = set(data["rates"].keys())
        else:
            print("Failed to fetch currency rates on startup")

@app.post("/convert")
async def convert_currency(req: ConvertRequest):
    if req.from_currency not in valid_currencies or req.to_currency not in valid_currencies:
        raise HTTPException(status_code=400, detail="Invalid currency code or request")

    # Get latest rates relative to from_currency (you may need to call API with base=req.from_currency)
    async with httpx.AsyncClient() as client:
        url = f"https://api.exchangerate-api.com/v4/latest/{req.from_currency}"
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch conversion rates")

        rates = response.json()["rates"]
        rate = rates.get(req.to_currency)
        if rate is None:
            raise HTTPException(status_code=400, detail="Invalid currency code or request")

        converted_amount = req.amount * rate
        return {"converted_amount": converted_amount, "rate": rate}
