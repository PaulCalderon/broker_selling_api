from pytest import Session
from housing_orm import DatabaseCommands
from housing_orm import HouseList, SoldHouses, LoanAmount
from sqlalchemy import NullPool, create_engine


DBFILE = "House_List.db"
engine = create_engine("sqlite+pysqlite:///" + DBFILE , echo=False, poolclass=NullPool)

class HousingAPI:

    @staticmethod
    def add_house(location, developer_name, total_price):
        house_details = HouseList(location_city=location, developer=developer_name, price = total_price )
        DatabaseCommands.insert(house_details, DBFILE, engine)

    @staticmethod
    def update_house_price(house_id, new_price, *engine_object):

        if engine_object:
            for data in engine_object:
                engine_object = data
        else:
            engine_object = engine
        if new_price > 0:
            pass
        else:
            raise ValueError('Price must be greater than 0')

        price_update_object = DatabaseCommands.get(HouseList, house_id, engine_object)
        if price_update_object is None:
            raise ValueError("House id doesn't exist")
        price_update_object.price = int(new_price)
        DatabaseCommands.update(HouseList, price_update_object, engine_object, "price")

    @staticmethod
    def reserve_house(house_id, *engine_object):
        if engine_object:
            for data in engine_object:
                engine_object = data
        else:
            engine_object = engine

        house_to_reserve = DatabaseCommands.get(HouseList, house_id, engine_object)
        if house_to_reserve is None:
            raise ValueError("House id doesn't exist")
        if house_to_reserve.Reserved is None:
            house_to_reserve.Reserved = "True"
            DatabaseCommands.update(HouseList, house_to_reserve, engine_object, "Reserved")
        else: 
            raise ValueError('House is already reserved')

    @staticmethod
    def check_house_price(house_id, *engine_object):
        if engine_object:
            for data in engine_object:
                engine_object = data
        else:
            engine_object = engine

        house_data = DatabaseCommands.get(HouseList, house_id, engine_object)
        if house_data is None:
            raise ValueError("House id doesn't exist")
        return house_data.price

    @staticmethod
    def remove_house(house_id, *engine_object):
        if engine_object:
            for data in engine_object:
                engine_object = data
        else:
            engine_object = engine

        house_data = DatabaseCommands.get(HouseList, house_id, engine_object)
        DatabaseCommands.delete(HouseList, house_id, engine_object)


    @staticmethod
    def sell_house(house_id, financing_option_input, price_paid=0, broker_name_input=None, commission_percent_input = 0,  engine_object=engine): #more arguments chec kthe mermaid

        house_data = DatabaseCommands.get(HouseList, house_id, engine_object)
        #checks if sell command is valid
        if house_data is None: #guard clause if house_id given does not exist
            raise ValueError("No matching house id")
        if  house_data.Sold == 'True':
            raise ValueError('House already sold')
        if int(price_paid) > int(house_data.price):
            raise ValueError("Payment is more than price of house")
        if not (0 <= float(commission_percent_input) <= 100):
            raise ValueError("Commission percent should be between 0 and 100")

        loan_amount = int(house_data.price) - int(price_paid)
        house_data.Sold = 'True'
        DatabaseCommands.update(HouseList, house_data, engine_object,'Sold')
        loan_data_object = SoldHouses(id_of_house = house_id, broker_name = broker_name_input, commission_percent = commission_percent_input, downpayment_amount = price_paid, financing_option = financing_option_input)
        DatabaseCommands.create_database_entry(loan_data_object, engine_object)

        if loan_amount > 0:
            create_loan_database_entry(house_id, loan_amount, engine_object)

def create_loan_database_entry(house_id, loan_amount, engine_object = engine):
    loan_entity = LoanAmount(id_of_house = house_id, original_loan = loan_amount, current_loan = loan_amount)
    DatabaseCommands.create_database_entry(loan_entity, engine_object)






# if __name__ == '__main__':
    # HousingAPI.add_house("Palawan", "Ayala", 696969)
    # HousingAPI.update_house_price(1, 44444)
    #HousingAPI.sell_house(1, "Cash")
    # data = DatabaseCommands.get(HouseList, 100, engine)
    # if data == None:
    #     print("nonetype")
    # print(type(data))
    # pass