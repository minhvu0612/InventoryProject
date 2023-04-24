from api.db_manager import products, catogories, con
from sqlalchemy import and_

# Lấy dữ liệu sản phẩm
def get_all_product():
    try:
        ins = products.select()
        result = con.execute(ins)
        return result
    except:
        return "error"

# Thêm một sản phẩm vào cơ sở dữ liệu
def create_product(product):
    try:
        ins = products.insert().values(
            name = product.name, 
            buy_price = product.buy_price, 
            sell_price = product.sell_price, 
            description = product.description,
            catogory_id = product.catogory_id
        )
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Cập nhật thông tin sản phẩm
def update_product(product, id):
    try:
        ins = products.update().where(products.c.id == id).values(
            name = product.name, 
            buy_price = product.buy_price, 
            sell_price = product.sell_price, 
            description = product.description,
            catogory_id = product.catogory_id
        )
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Xóa sản phẩm
def delete_product(id):
    try:
        ins = products.delete().where(products.c.id == id)
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Lấy dữ liệu loại sản phẩm
def get_all_catogory():
    try:
        ins = catogories.select()
        result = con.execute(ins)
        return result
    except:
        return "error"