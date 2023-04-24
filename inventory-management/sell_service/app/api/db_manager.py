from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Tạp connect đến phpmyadmin
engine = create_engine('mysql+pymysql://root@localhost:3306/sell')
meta = MetaData()
con = engine.connect()

# Định nghĩa dữ liệu về sản phẩm
sells = Table(
   'sell', meta, 
   Column('id', Integer, primary_key = True, autoincrement = True),
   Column('sell_count', String(255)),
   Column('date', String(255)),
   Column('product_id', Integer),
)
# meta.create_all(engine)