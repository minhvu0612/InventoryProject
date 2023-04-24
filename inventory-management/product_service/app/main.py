# api.py (v1.0.0)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# import package
from api.db_manager import con
from api.schemas import Product
from api.products import *

# init application
app = FastAPI(
    title = "PRODUCT MANAGEMENT",
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

# api lấy tất cả sản phẩm
@app.get("/api/product")
def get_product():
    result_p = get_all_product()
    result_c = get_all_catogory()
    data = []
    cato = []
    if result_p != "error" and result_c != "error":
        for row in result_p:
            data.append({
                "id": row.id,
                "name": row.name, 
                "buy_price": row.buy_price, 
                "sell_price": row.sell_price, 
                "description": row.description,
                "catogory_id": row.catogory_id
            })
        for row in result_c:
            cato.append({
                "id": row.id,
                "name": row.name,  
                "description": row.description,
            })
        return {
            "message": "success",
            "product": data,
            "catogory": cato
        }
    return {"message": "error"}

# api thêm mới một sản phẩm
@app.post("/api/product")
def create_new_product(item: Product):
    result = create_product(item)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# api cập nhật sản phẩm
@app.put("/api/product/{id}")
def update_product_by_id(item: Product, id: int):
    result = update_product(item, id)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# api xóa sản phẩm
@app.delete("/api/delete/{id}")
def delete_product_by_id(id: int):
    result = delete_product(id)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# running
if __name__ == "__main__":
    uvicorn.run(app, port = 9001)