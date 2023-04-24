from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Tạp connect đến phpmyadmin
engine = create_engine('mysql+pymysql://root@localhost:3306/product')
meta = MetaData()
con = engine.connect()

# Định nghĩa dữ liệu về nhóm sản phẩm
catogories = Table(
   'category', meta, 
   Column('id', Integer, primary_key = True, autoincrement = True),
   Column('name', String(255)), 
   Column('description', String(255)),
)

# Định nghĩa dữ liệu về sản phẩm
products = Table(
   'product', meta, 
   Column('id', Integer, primary_key = True, autoincrement = True),
   Column('name', String(255)), 
   Column('buy_price', String(255)), 
   Column('sell_price', String(255)),
   Column('description', String(255)),
   Column('catogory_id', Integer),
)
# meta.create_all(engine)