import os
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.pool import NullPool
from sqlalchemy.inspection import inspect

DBFILE = "example.db"
engine = create_engine("sqlite+pysqlite:///" + DBFILE , echo=False, poolclass=NullPool)

class Base(DeclarativeBase):
    pass

class HouseList(Base):
    __tablename__ = "Houses"
    id_of_house: Mapped[int] = mapped_column(primary_key=True)
    location_city: Mapped[str] = mapped_column(String(30))
    developer: Mapped[str] = mapped_column(String(30))
    price: Mapped[int]
    Reserved: Mapped[Optional[str]]
    Sold: Mapped[Optional[str]] 
    Sold_Houses: Mapped[List["SoldHouses"]] = relationship(back_populates="House")


class SoldHouses(Base):
    __tablename__ = "SoldHouses"
    transaction_id: Mapped[int] = mapped_column(primary_key=True)
    id_of_house = mapped_column(ForeignKey("Houses.id_of_house"))
    broker_name : Mapped[Optional[str]]
    commission_percent : Mapped[Optional[int]]
    downpayment_amount : Mapped[Optional[int]]
    financing_option : Mapped[str]
    House: Mapped[List["HouseList"]] = relationship(back_populates="Sold_Houses")

# if not os.path.exists(DBFILE):
#     database_commands.table_init()

def table_initialize(database_name):
    DBFILE = database_name
    engine = create_engine("sqlite+pysqlite:///" + DBFILE , echo=False, poolclass=NullPool)
    Base.metadata.create_all(engine)


class DatabaseCommands():
       
    @staticmethod
    def insert(houses_object: HouseList, *dbname) -> None:
        """dbname added for pytesting"""
        if dbname:
            database_name, engine = dbname
        else:
            database_name = DBFILE
            engine = create_engine("sqlite+pysqlite:///" + DBFILE , echo=False, poolclass=NullPool)


        if not os.path.exists(database_name):
            table_initialize(database_name)

        with Session(engine) as session:
            session.add(houses_object)
            session.commit()


    @staticmethod
    def update(table_class, table_object, engine_object, *updated_fields) -> None:
        """takes updated table object and pushes to update database entry"""        """implementation is bad and just a workaround"""
        primary_id_name = inspect(type(table_object)).primary_key[0].name
        primary_id = getattr(table_object,primary_id_name)
        #print(inspect(table_object).primary_key[0].name)


            
        with Session(engine_object) as session:
            data = session.get(table_class, primary_id)
            for fields in updated_fields:
                setattr(data, fields, getattr(table_object,fields))
            session.commit()


    @staticmethod
    def delete(table_to_get_data_from, primary_id, *engine_object) -> None:
        for data in engine_object:
            engine = data
        
        with Session(engine) as session:
            data = session.get(table_to_get_data_from, primary_id)
            session.delete(data)
            session.commit()


    @staticmethod
    def get(table_to_get_data_from, primary_id, *engine_object) -> HouseList:
        """*arg is work around for pytest"""
        
        for data in engine_object:
            engine = data

        with Session(engine) as session:
            data = session.get(table_to_get_data_from, primary_id)
            return data


# if __name__ == "__main__":
#     houses_object = HouseList(location_city="Makati City", developer = "SMDC", price = 50000)
#     with Session(engine) as session:
#         houses_object = HouseList(location_city="Makati City", developer = "SMDC", price = 50000)
#         houses_object1 = session.get(HouseList,1)
#         print(houses_object.developer)
#         print(houses_object1.developer)
#         houses_object1.developer = houses_object.developer


#         #houses_object.developer = "RLC"
#         session.flush()
#         session.commit()
#         print(houses_object.id_of_house)
#         primary_id = inspect(type(houses_object)).primary_key[0].name
#         print(primary_id)
    # DatabaseCommands.update(houses_object)
# if __name__ == "__main__":
#     with Session(engine) as session:
#         data = session.get(HouseList, 5)
#         print(data)
#         data.location_city = "Cavite"
#         data.price = 90000
#         DatabaseCommands.update(HouseList, data, engine, "price", "location_city")
    
#     pass
