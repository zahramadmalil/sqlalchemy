from sqlalchemy import create_engine, Column, INTEGER, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///CarData.db', echo=True)
engine.connect()

Base = declarative_base()

class Car(Base):
    __tablename__ = 'carsinfo'

    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(Float)
    quantity = Column(INTEGER)

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    mobile = Column(INTEGER)
    price = Column(Float)


Base.metadata.create_all(engine)
###################################################

session = sessionmaker(bind=engine)
sessionlocal = session()
###################################################

custom1 = Customer(name = 'hiwonda', address = 'ahvaz', mobile = 9918783558, price = 3500)
custom2 = Customer(name = 'hiwonda1400', address = 'shiraz', mobile = 9918784242, price = 4000)

# car1 = Car(brand = 'Benz', model = 'G class', price = 2000, quantity =5)
# car2 = Car(brand = 'BMW', model = 'AMG', price = 1500, quantity =10)

sessionlocal.add_all([custom1, custom2])
sessionlocal.commit()
####################################################

# cars_obj = sessionlocal.query(Car).all() #list of car object
# #print(cars_obj)
# for item in cars_obj:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)

######################################################
# car1 = sessionlocal.query(Car).filter_by(id = 1).first() #object
# print(car1.brand) 
# print(car1.model)
# print(car1.price)   
################################
# car_bmw = sessionlocal.query(Car).filter_by(brand = 'BMW').all() #list of car object
# for item in car_bmw:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)
##############################################
# car_bmw = sessionlocal.query(Car).filter_by(price = 1500).all() #list of car object
# for item in car_bmw:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)
###############################################
#car_temp = sessionlocal.query(Car).filter(Car.price > 1500).all()
# for item in car_temp:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)
#########################
# car_temp = sessionlocal.query(Car).filter(Car.model.like('AMG%')).all()
# for item in car_temp:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)
#######################################################
# car_temp = sessionlocal.query(Car).filter(Car.model.like('AMG%')).first()

# car_temp.brand = 'AUDI'
# sessionlocal.commit()

# if car_temp != None:
#     sessionlocal.delete(car_temp)
#     sessionlocal.commit()