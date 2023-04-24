from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Tạp connect đến phpmyadmin
engine = create_engine('mysql+pymysql://root@localhost:3306/account')
meta = MetaData()
con = engine.connect()

# Định nghĩa dữ liệu về tài khoản user
accounts = Table(
   'user', meta, 
   Column('id', Integer, primary_key = True, autoincrement = True),
   Column('name', String(255)), 
   Column('username', String(255)), 
   Column('password', String(255)),
   Column('password', String(255)),
   Column('avatar', String(255)),
   Column('group_id', Integer),
)

# Định nghĩa dữ liệu về nhóm user
groups = Table(
   'group', meta, 
   Column('id', Integer, primary_key = True),
   Column('group_name', String(255)), 
   Column('group_level', String(255)),
)
# meta.create_all(engine)