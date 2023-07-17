from fastapi import APIRouter
from schema.schema import ServerRequest, CalculatePriceSchema
from model.model import Insurance
from decimal import Decimal
router = APIRouter()

@router.post("/update_rate/")
async def update_rate(*, data: ServerRequest):
    for k, v in data.items():
        for rate in v:
            await Insurance.create(date=k, type=rate.cargo_type, rate=float(rate.rate))

@router.post("/calculate/")
async def calculate(*, data: CalculatePriceSchema):
    rate = await Insurance.filter(date=data.date, type=data.cargo_type).first()
    if rate is None:
        rate = await Insurance.filter(date=data.date, type="Other").first()
    return (Decimal(rate.rate)*data.price)