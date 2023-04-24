from api.db_manager import reports, con
from sqlalchemy import and_

# Lấy dữ liệu dữ liệu báo cáo
def get_all_report():
    try:
        ins = reports.select()
        result = con.execute(ins)
        return result
    except:
        return "error"

# Thêm một dữ liệu báo cáo vào cơ sở dữ liệu
def create_report(report):
    try:
        ins = reports.insert().values(
            file = report.file, 
            date = report.date,
        )
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Xóa dữ liệu báo cáo
def delete_report(id):
    try:
        ins = reports.delete().where(reports.c.id == id)
        result = con.execute(ins)
        return "success"
    except:
        return "error"