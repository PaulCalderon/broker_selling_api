import pytest
import os
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, NullPool
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from housing_orm import HouseList, SoldHouses, table_initialize
from housing_orm import DatabaseCommands


DBFILE = "testhouselist.db"
engine = create_engine("sqlite+pysqlite:///" + DBFILE , echo=False, poolclass=NullPool)

class Base(DeclarativeBase):
    pass

# class HouseList(Base):
#     __tablename__ = "Houses"
#     id_of_house: Mapped[int] = mapped_column(primary_key=True)
#     location_city: Mapped[str] = mapped_column(String(30))
#     developer: Mapped[str] = mapped_column(String(30))
#     price: Mapped[int]
#     Reserved: Mapped[Optional[str]]
#     Sold: Mapped[Optional[str]] 
#     Sold_Houses: Mapped[List["SoldHouses"]] = relationship(back_populates="House")


# class SoldHouses(Base):
#     __tablename__ = "SoldHouses"
#     transaction_id: Mapped[int] = mapped_column(primary_key=True)
#     id_of_house = mapped_column(ForeignKey("Houses.id_of_house"))
#     broker_name : Mapped[Optional[str]]
#     commission_percent : Mapped[Optional[int]]
#     downpayment_amount : Mapped[Optional[int]]
#     financing_option : Mapped[str]
#     House: Mapped[List["HouseList"]] = relationship(back_populates="Sold_Houses")

class TestORMOfHousing:
    """Class for grouping tests"""
    def test_ORM_can_create_database_if_it_does_not_exist_yet(self):
        
        if os.path.exists(DBFILE):
            os.remove(DBFILE)

        #assert os.path.exists(DBFILE) == False
        table_initialize(DBFILE)
        assert os.path.exists(DBFILE)

        if os.path.exists(DBFILE):
            os.remove(DBFILE) #cleanup

    def test_ORM_should_create_database_after_insert_command(self):

        if os.path.exists(DBFILE):
            os.remove(DBFILE)

        houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
        DatabaseCommands.insert(houses_object, DBFILE, engine)
        assert os.path.exists(DBFILE)

        if os.path.exists(DBFILE):
            os.remove(DBFILE)


        
    def test_ORM_should_be_able_to_add_new_data(self):

        if os.path.exists(DBFILE):
            os.remove(DBFILE)
        houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
        DatabaseCommands.insert(houses_object, DBFILE, engine)
        data1 = DatabaseCommands.get(HouseList,1,engine)
        houses_object = HouseList(location_city="Makati City", developer = "SMDC", price = 50000)
        DatabaseCommands.insert(houses_object, DBFILE, engine)
        data2 = DatabaseCommands.get(HouseList,2,engine)
        assert data1.price == 10000
        assert data2.location_city == "Makati City"
        assert data2.price == 50000


        if os.path.exists(DBFILE):
            os.remove(DBFILE)




    # def test_ORM_should_be_able_to_retrieve_data(self):
    #     pass

    # def test_ORM_should_be_able_to_update_data(self):

    #     if os.path.exists(DBFILE):
    #         os.remove(DBFILE)
    #     houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
    #     DatabaseCommands.insert(houses_object)
    #     houses_object = HouseList(id_of_house=1, price = 20000)
    #     DatabaseCommands.update(houses_object)
    #     data = DatabaseCommands.get(1)
    #     assert data.price == 20000

    #     if os.path.exists(DBFILE):
    #         os.remove(DBFILE)



    # def test_ORM_should_be_able_to_delete_data(self):
    #     pass

# houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
# DatabaseCommands.insert(houses_object, DBFILE)
# houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
# DatabaseCommands.insert(houses_object, DBFILE, engine)