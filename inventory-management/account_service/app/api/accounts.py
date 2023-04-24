from api.db_manager import accounts, con
from sqlalchemy import and_

# Lấy dữ liệu user đăng nhập qua tên và mật khẩu
def get_user(username, password):
    try:
        ins = accounts.select().where(
            and_(
                accounts.c.username == username,
                accounts.c.password == password
            )
        )
        result = con.execute(ins)
        return result
    except:
        return "error"

# Thêm một user vào cơ sở dữ liệu
def create_user(user):
    try:
        ins = accounts.insert().values(name = user.name, username = user.username, password = user.password, avatar = user.avatar, group_id = user.group_id)
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Cập nhật thông tin user
def update_user(user, id):
    try:
        ins = accounts.update().where(accounts.c.id == id).values(name = user.name, username = user.username, password = user.password, avatar = user.avatar, group_id = user.group_id)
        result = con.execute(ins)
        return "success"
    except:
        return "error"

# Xóa tài khoản của user
def delete_user(id):
    try:
        ins = accounts.delete().where(accounts.c.id == id)
        result = con.execute(ins)
        return "success"
    except:
        return "error"
