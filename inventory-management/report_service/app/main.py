# api.py (v1.0.0)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# import package
from api.db_manager import con
from api.schemas import Report
from api.reports import *

# init application
app = FastAPI(
    title = "REPORT MANAGEMENT",
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

# api lấy tất cả dữ liệu báo cáo
@app.get("/api/report")
def get_report():
    result = get_all_report()
    data = []
    if result != "error":
        for row in result:
            data.append({
                "id": row.id, 
                "file": row.file, 
                "date": row.date,
            })
        return {
            "message": "success",
            "report": data,
        }
    return {"message": "error"}

# api thêm mới một dữ liệu báo cáo
@app.post("/api/report")
def create_new_report(item: Report):
    result = create_report(item)
    result = "success"
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# api xóa dữ liệu báo cáo
@app.delete("/api/delete/{id}")
def delete_report_by_id(id: int):
    result = delete_report(id)
    if result == "success":
        return {"message": "success"}
    else:
        return {"message": "error"}

# running
if __name__ == "__main__":
    uvicorn.run(app, port = 9002)