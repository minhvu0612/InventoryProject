from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Tạp connect đến phpmyadmin
engine = create_engine('mysql+pymysql://root@localhost:3306/report')
meta = MetaData()
con = engine.connect()

# Định nghĩa dữ liệu về báo cáo
reports = Table(
   'report', meta, 
   Column('id', Integer, primary_key = True, autoincrement = True),
   Column('file', String(255)),
   Column('date', String(255)),
)
# meta.create_all(engine)