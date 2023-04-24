# api.py (v1.0.0)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# import package
from api.db_manager import con
from api.schemas import Sell
from api.sells import *

# init application
app = FastAPI(
    title = "SELL MANAGEMENT",
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

# api lấy tất cả dữ liệu bán hàng
@app.get("/api/sell")
def get_sell():
    result = get_all_sell()
    data = []
    if result != "error":
        for row in result:
            data.append({
                "id": row.id, 
                "sell_count": row.sell_count, 
                "date": row.date,
                "product_id": row.product_id
            })
        return {
            "message": "success",
            "sell": data,
        }
    return {"message": "error"}

# api thêm mới một dữ liệu bán hàng
@app.post("/api/sell")
def create_new_sell(item: Sell):
    result = create_sell(item)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# api cập nhật dữ liệu bán hàng
@app.put("/api/sell/{id}")
def update_sell_by_id(item: Sell, id: int):
    result = update_sell(item, id)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# api xóa dữ liệu bán hàng
@app.delete("/api/delete/{id}")
def delete_sell_by_id(id: int):
    result = delete_sell(id)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# running
if __name__ == "__main__":
    uvicorn.run(app, port = 9003)