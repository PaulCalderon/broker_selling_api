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

    def test_ORM_should_be_able_to_update_data(self):

        if os.path.exists(DBFILE):
            os.remove(DBFILE)
        houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
        DatabaseCommands.insert(houses_object, DBFILE, engine)

        houses_object = DatabaseCommands.get(HouseList, 1, engine)
        houses_object.price = 7000
        DatabaseCommands.update(HouseList, houses_object, engine, "price")

        data = DatabaseCommands.get(HouseList, 1, engine,)
        assert data.price == 7000
        if os.path.exists(DBFILE):
            os.remove(DBFILE)
