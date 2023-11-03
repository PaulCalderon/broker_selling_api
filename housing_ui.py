#acts as UI and application layer
from housing_application import HousingAPI




def validate_input(user_command: int) -> bool:

    user_command = int(user_command)
    match user_command:
        case 1 | 2 | 3 | 4 | 5 | 6:
            
            return True
        case _:
            raise ValueError("Invalid Command")

def process_command(user_command): #can give feedback about command by getting data from database and outputing
    match user_command:
        case 1:
            print("Adding a house to the database")
            location = input("Enter city name: ")
            developer = input("Enter developer name: ")
            price = int(input("Enter price of house: "))
            HousingAPI.add_house(location, developer, price)
            print("House entry created")

        case 2:
            print("Updating house price")
            house_id = int(input("Enter house id to be updated: "))
            new_price = int(input("Enter new price: "))
            HousingAPI.update_house_price(house_id, new_price)
            print("House price updated")
        
        case 3:
            print("Reserving house")
            house_id = int(input("Enter house id to reserve: "))
            HousingAPI.reserve_house(house_id)
            print("House listing reserved")

        case 4: 
            print("Checking house price")
            house_id = int(input("Enter house id to check: "))
            checked_price = HousingAPI.check_house_price(house_id)
            print(f"The price of the house is {checked_price}")
        
        case 5:
            print("Removing house")
            house_id = int(input("Enter house id to remove: "))
            HousingAPI.remove_house(house_id)
        
        case 6:
            print("Selling House")
            house_id = int(input("Enter house id to sell: "))
            broker_name = input("Enter name of broker: ")
            commission_percent = float(input("Enter commission percent: "))
            downpayment_amount = float(input("Enter downpayment amount: "))
            financing_option = input("Enter financing option: ")
            HousingAPI.sell_house(house_id, financing_option, downpayment_amount, broker_name, commission_percent)


def help_command():
    print("The following commands are available:")
    print("1. Add House")
    print("2. Update House Price")
    print("3. Reserve House")
    print("4. Check House Price")
    print("5. Remove House")
    print("6. Sell House")

if __name__ == '__main__':
    help_command()
    user_command = int(input("Enter the # Command: "))
    validate_input(user_command)
    process_command(user_command)
