# schema.py
from pydantic import BaseModel,  Field
from typing import Union

# model về các thông tin của user

class User(BaseModel):
    name: str = Field(example = "Vu Ngoc Minh")
    username: str = Field(example = "vnm0612")
    password: str = Field(example = "vnm0612")
    avatar: str = Field(example = "path_to_image")
    group_id: int = Field(example = 1)