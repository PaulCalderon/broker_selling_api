import pytest
import os
from sqlalchemy import NullPool, create_engine
from housing_application import HousingAPI
from housing_orm import DatabaseCommands, HouseList, SoldHouses




@pytest.fixture
def setup_database():
    DBFILE = "testhouselist.db"
    engine = create_engine("sqlite+pysqlite:///" + DBFILE , echo=False, poolclass=NullPool)
    houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
    DatabaseCommands.insert(houses_object, DBFILE, engine)
    return DBFILE, engine







class TestAPIOfHousing:

    def test_API_should_check_price_of_house_if_less_than_payment(self):
        pass

    def test_API_should_make_sure_new_price_is_not_zero_or_less(self, setup_database):
        

        with pytest.raises(ValueError, match="Price must be greater than 0"):
            DBFILE, engine = setup_database
            house_id = 1
            new_price = 0
            HousingAPI.update_house_price(house_id, new_price, engine)
        
        
    
    def test_API_should_make_sure_new_price_is_correct(self, setup_database):
            DBFILE, engine = setup_database
            house_id = 1
            new_price = 1000
            HousingAPI.update_house_price(house_id, new_price, engine)
            newly_inserted_price = DatabaseCommands.get(HouseList, house_id, engine)
            assert new_price == newly_inserted_price.price
    



    def test_API_should_create_loan_database_entry_after_selling_house(self):
        assert False

    
    def test_API_should_properly_update_sold_houses(self, setup_database):
        HousingAPI.sell_house(1)
        sell_status_of_house = False
        assert sell_status_of_house

    def test_API_should_properly_update_reservered_houses(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 1 


        houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 1777)
        DatabaseCommands.insert(houses_object, DBFILE, engine)
        HousingAPI.reserve_house(house_id, engine)
        data = DatabaseCommands.get(HouseList, house_id, engine)
        reserve_status_of_house = data.Reserved
        assert reserve_status_of_house

    def test_API_should_check_if_house_is_reserved_before_doing_reserve_action(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 1 

        with pytest.raises(ValueError, match="House is already reserved"):
            HousingAPI.reserve_house(house_id, engine)
    def test_API_should_check_info_is_complete_before_adding_house_to_database(self):


        with pytest.raises(TypeError):
            HousingAPI.add_house("Manila City", "SMDC") #missing price column info

    def test_API_should_raise_error_if_information_is_missing_when_adding_houses(self):


        with pytest.raises(TypeError):
            HousingAPI.add_house("Manila City", "SMDC") #missing price column info

    def test_API_should_be_able_to_retrive_house_price_from_database(self):
        pass







    def test_API_should_check_if_payment_value_is_more_than_loan(self):
        pass
    def test_API_should_properly_deduct_paid_amount_to_loan(self):
        pass
    

    # @pytest.mark.skip(reason="no way of currently testing this")
    # def test_clean_up(self):
    #     DBFILE = "testhouselist.db"
    #     if os.path.exists(DBFILE):
    #         os.remove(DBFILE)