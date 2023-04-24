# schema.py
from pydantic import BaseModel,  Field
from typing import Union

# model về các thông tin của sản phẩm

class Product(BaseModel):
    name: str = Field(example = "Bàn học gấp")
    buy_price: str = Field(example = "40000")
    sell_price: str = Field(example = "60000")
    description: str = Field(example = "Kích thước 30x60x40 cm, phủ nhựa cao cấp")
    catogory_id: int = Field(example = 1)

# model về các thông tin bán hàng

class Sell(BaseModel):
    name: str = Field(example = "Đồ gỗ")
    description: str = Field(example = "Đồ gỗ")