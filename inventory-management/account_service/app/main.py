# api.py (v1.0.0)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# import package
from api.db_manager import con
from api.schemas import User
from api.accounts import *

# init application
app = FastAPI(
    title = "ACCOUNT MANAGEMENT",
    description = "This API was built with FastAPI."
)

# cors-header-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lấy thông tin user qua username và password
@app.get("/api/account/{username}/{password}")
def get_user_by_info(username: str, password: str):
    result = get_user(username, password)
    if result != "error":
        for row in result:
            print(row)
            return {
                "message": "success",
                "name": row.name,
                "username": row.username,
                "password": row.password,
                "avatar": row.avatar,
                "group_id": row.group_id
            }
    return {"message": "error"}

# Tạo user mới
@app.post("/api/account")
def create_new_user(item: User):
    result = create_user(item)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# Cập nhật user
@app.put("/api/account/{id}")
def update_user_by_id(item: User, id: int):
    result = update_user(item, id)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# Xóa user
@app.delete("/api/account/{id}")
def delete_user_by_id(id: int):
    result = delete_user(id)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# running
if __name__ == "__main__":
    uvicorn.run(app, port = 9000)