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

        if not os.path.exists(database_name):
            table_initialize(database_name)

        with Session(engine) as session:
            session.add(houses_object)
            session.commit()


    @staticmethod
    def update() -> None:
        pass

    @staticmethod
    def delete() -> None:
        pass

    @staticmethod
    def get(table_to_get_data_from, house_id, *engine_object) -> HouseList:
        
        for data in engine_object:
            engine = data

        with Session(engine) as session:
            data = session.get(table_to_get_data_from, house_id)
            return data

        