# schema.py
from pydantic import BaseModel,  Field
from typing import Union

# model về thông tin báo cáo

class Report(BaseModel):
    file: str = Field(example = "binary_encode")
    date: str = Field(example = "2023-01-01")