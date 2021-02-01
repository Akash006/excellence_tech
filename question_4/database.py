from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sales.db', echo = True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'CustomerData'

    username = Column(String, primary_key = True)
    password = Column(String)

class Address(Base):
    __tablename__ = 'CustomerAddress'

    username = Column(String, primary_key = True)
    street = Column(String)
    pincode = Column(Integer)
    country = Column(String)
    state = Column(String)
    phone_no = Column(Integer)

class Submit_data():

    def __init__(self):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind = engine, autoflush=False)
        self.session = Session()

    def user(self, userData):
        self.session.add(userData)
        self.session.commit()
        engine.dispose()

    def address(self, userAddress):
        self.session.add(userAddress)
        self.session.commit()
        engine.dispose()

    @staticmethod
    def get_userdata():
        query = "SELECT * FROM CustomerData ;"
        con = engine.connect()
        result = con.execute(query)
        engine.dispose()
        return result

    def update_address(add: list):
        query = f'''UPDATE CustomerAddress SET username={add.username},
        street={add.street},
        pincode={add.pincode},
        country={add.country},
        state={add.state},
        phone_no={add.phone_no},
        where username = {add.username}'''

        con = engine.connect()
        result = con.execute(query)
        engine.dispose()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    