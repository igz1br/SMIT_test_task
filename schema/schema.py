from pydantic import BaseModel, RootModel, model_validator
from datetime import datetime
from decimal import Decimal

class RateSchema(BaseModel):
    cargo_type: str
    rate: str

class DictRequest(RootModel):
    root: dict[str, list[RateSchema]]


    def __getitem__(self, item):
        return self.root[item]
    
    def __iter__(self):
        return iter(self.root)

    def items(self):
        return self.root.items()    

class ServerRequest(DictRequest):
    pass
    
class CalculatePriceSchema(BaseModel):
    date: str
    cargo_type: str
    price: Decimal  # В работе с финансами принято использовать Decimal для избежагия ошибок округления.

