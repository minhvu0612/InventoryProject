from api.db_manager import sells, con
from sqlalchemy import and_

# Lấy dữ liệu dữ liệu bán hàng
def get_all_sell():
    try:
        ins = sells.select()
        result = con.execute(ins)
        return result
    except:
        return "error"

# Thêm một dữ liệu bán hàng vào cơ sở dữ liệu
def create_sell(sell):
    try:
        ins = sells.insert().values(
            sell_count = sell.sell_count, 
            date = sell.date,
            product_id = sell.product_id
        )
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Cập nhật thông tin dữ liệu bán hàng
def update_sell(sell, id):
    try:
        ins = sells.update().where(sells.c.id == id).values(
            sell_count = sell.sell_count, 
            date = sell.date,
            product_id = sell.product_id
        )
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Xóa dữ liệu bán hàng
def delete_sell(id):
    try:
        ins = sells.delete().where(sells.c.id == id)
        result = con.execute(ins)
        return "success"
    except:
        return "error"