import pytest
import os
from sqlalchemy import NullPool, create_engine
from housing_application import HousingAPI
from housing_orm import DatabaseCommands, HouseList, SoldHouses, LoanAmount




@pytest.fixture
def setup_database():
    DBFILE = "testhouselist.db"
    engine = create_engine("sqlite+pysqlite:///" + DBFILE , echo=False, poolclass=NullPool)
    if not os.path.exists(DBFILE):
        houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 10000)
        DatabaseCommands.insert(houses_object, DBFILE, engine)
    return DBFILE, engine

class TestAPIOfHousing:


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

    def test_API_should_check_if_house_id_to_be_updated_already_exists_in_the_database(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 100 #house id doesn't exist
        new_price = 1000
        with pytest.raises(ValueError, match="House id doesn't exist"):
            HousingAPI.update_house_price(house_id, new_price, engine)

    def test_API_should_check_if_house_id_to_be_reserved_already_exists_in_the_database(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 100 #house id doesn't exist
        new_price = 1000
        with pytest.raises(ValueError, match="House id doesn't exist"):
            HousingAPI.reserve_house(house_id, engine)

    def test_API_should_check_if_house_id_to_be_removed_exists_in_the_database(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 100 #house id doesn't exist

        with pytest.raises(ValueError, match="House id doesn't exist"):
            HousingAPI.remove_house(house_id, engine)
            
    def test_house_id_to_be_price_checked_must_exist_in_the_database(self, setup_database):
        """checks if house id to be price checked exists"""
        DBFILE, engine = setup_database
        house_id = 100 #house id doesn't exist
        new_price = 1000
        with pytest.raises(ValueError, match="House id doesn't exist"):
            HousingAPI.check_house_price(house_id, engine)


    def test_API_should_properly_update_reservered_houses(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 1 

        houses_object = HouseList(location_city="Quezon City", developer = "Megaworld", price = 1777)
        DatabaseCommands.insert(houses_object, DBFILE, engine)
        HousingAPI.reserve_house(house_id, engine)
        data = DatabaseCommands.get(HouseList, house_id, engine)
        reserve_status_of_house = data.Reserved
        assert reserve_status_of_house == 'True'

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

    def test_API_should_be_able_to_retrive_house_price_from_database(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 1
        price_of_house = HousingAPI.check_house_price(house_id, engine)
        assert price_of_house == 1000

    def test_API_should_be_able_to_delete_specified_house_entry(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 2
        HousingAPI.check_house_price(house_id, engine)

    def test_API_should_check_price_of_house_if_less_than_payment(self, setup_database):
        DBFILE, engine = setup_database
        house_id = 1
        price = 2000 # price of house is only 1000.
        with pytest.raises(ValueError, match="Payment is more than price of house"):
            HousingAPI.sell_house(house_id, "cash", price_paid=price, engine_object=engine)

    def test_API_should_properly_update_sold_houses(self, setup_database):
        DBFILE, engine = setup_database
        house_id=1
        price_paid = 100 
        financing_option = "cash"
        broker_name = "Paul"
        commission_percent = 10

        HousingAPI.sell_house(house_id, financing_option, price_paid, broker_name, commission_percent, engine_object=engine)
        data = DatabaseCommands.get(HouseList, house_id, engine)
        sell_status_of_house = data.Sold
        assert sell_status_of_house == 'True'

    def test_API_should_check_and_return_error_if_house_already_sold(self, setup_database):
        DBFILE, engine = setup_database
        house_id=1
        price = 0 

        with pytest.raises(ValueError, match="House already sold"):
            HousingAPI.sell_house(house_id, price, engine_object=engine)

    def test_API_should_create_sold_houses_database_entry_after_selling_house(self, setup_database):
        """should be put after test of selling house"""
        DBFILE, engine_object = setup_database
        house_id = 1
        transaction_id = 1
        house_sold_data = DatabaseCommands.get(SoldHouses, transaction_id, engine_object)
        assert house_sold_data.id_of_house == 1
        assert house_sold_data.downpayment_amount == 100



    def test_if_downpayment_is_less_than_price_loan_database_entry_must_be_created(self, setup_database):
        DBFILE, engine_object = setup_database
        house_id = 1
        loan_data = DatabaseCommands.get(LoanAmount, house_id, engine_object)

        assert loan_data.id_of_house == 1 #not done
        assert loan_data.original_loan == 900


    def test_API_should_not_be_able_to_call_sell_house_if_house_is_not_in_database(self, setup_database):
        DBFILE, engine = setup_database
        with pytest.raises(ValueError, match="No matching house id"):
            HousingAPI.sell_house(100,"cash", engine_object=engine)
            
    #@pytest.mark.skip(reason="no way of currently testing this")
    def test_sell_house_should_raise_error_if_commission_percent_is_more_than_100_or_less_than_0(self, setup_database):
        DBFILE, engine_object = setup_database
        house_id = 2
        financing_option = "cash"
        commission_percent_over_100 = 100.1
        negative_commission_percent = -0.1
        
        with pytest.raises(ValueError, match= "Commission percent should be between 0 and 100"):

            HousingAPI.sell_house(house_id, financing_option, commission_percent_input=commission_percent_over_100, engine_object=engine_object)
        
        with pytest.raises(ValueError, match= "Commission percent should be between 0 and 100"):

            HousingAPI.sell_house(house_id, financing_option, commission_percent_input=negative_commission_percent, engine_object=engine_object)



    def test_API_should_check_if_payment_value_is_more_than_loan(self):
        pass
    def test_API_should_properly_deduct_paid_amount_to_loan(self):
        pass

    #@pytest.mark.skip(reason="no way of currently testing this")
    def test_clean_up(self):
        DBFILE = "testhouselist.db"
        if os.path.exists(DBFILE):
            os.remove(DBFILE)
