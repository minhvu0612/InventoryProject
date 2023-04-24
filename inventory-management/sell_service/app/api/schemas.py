# schema.py
from pydantic import BaseModel,  Field
from typing import Union

# model về các thông tin bán hàng

class Sell(BaseModel):
    sell_count: int = Field(example = 50)
    date: str = Field(example = "2023-01-01")
    product_id: int = Field(example = 1)