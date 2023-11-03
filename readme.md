# Broker House API

Developed in Python. This broker house API project accepts commands and arguments to maintain a database for an imaginary real estate broker. Three database tables are created by the application. The first one a database of available houses. The second one a database of the details after selling a house. The third a database of loans for the remaining balance after the sale of a house. A series of unit tests were developed using pytest. 

The backend database is sqlite3 and interfaced via ORM using SQLalchemy.

## Installation
It is recommented to install the packages in a virtual environment (venv)
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the below packages.
The program was developed under the following versions:
>Python3 3.11.0
>SQLAlchemy 2.0.22 Released: Oct 13, 2023
>pytest 7.4.3 Released: Oct 25, 2023


```
pip install SQLAlchemy
pip install pytest
```
Pull the latest version from the GitHub repository.

There are three python files comprising the application with the tests in a subdirectory called 'tests'. 
 **housing_ui.py** contains the UI elements and is responsible for interacting with the user. It parses the commands from the user and prompts the user for more input as required.
**housing_application.py** contains the business logic and interfaces between the UI and ORM. It contains the logic for processing the commands from the UI and also checks for invalid queries.
**housing\_orm.py** contains the ORM code for interacting with the sqlite3 database. housing_orm.py assumes that the arguments being passed are valid and correct.

[![](https://mermaid.ink/img/pako:eNp1kttqwzAMhl_F6Dp9gTAGY73ZxaCwu2Eoqq00ZrFlfGCMLu8-59AuzTLfONYvfb8idAHFmqAG1WGMe4PngFY6UU7LORp3PmYjHr53u8frG73vjMJk2N0nLoSp4qZwWDFLYE7ZY8ITRpIzbOxj4X2ZwsN5cYlCg4qi-DSpFTlS-FWflCKfojDO5zSF--naAi96XTgcAhd6pJkimsB2ZXPAUfcYImmh2Fp0OorEf3-23zIu6qbhjTR6_jvrrTno1QjvfK_zXZg-s0toXGkaT12BFNuRMVdDBZaCRaPLWoxlElJLliTU5VNj-JAg3ZCHOfHbl1NQp5CpguwLh-YtgrrBLpYoaZM4vM57NlwVeHTvzHYq7H8AtRXZmQ?type=png)](https://mermaid.live/edit#pako:eNp1kttqwzAMhl_F6Dp9gTAGY73ZxaCwu2Eoqq00ZrFlfGCMLu8-59AuzTLfONYvfb8idAHFmqAG1WGMe4PngFY6UU7LORp3PmYjHr53u8frG73vjMJk2N0nLoSp4qZwWDFLYE7ZY8ITRpIzbOxj4X2ZwsN5cYlCg4qi-DSpFTlS-FWflCKfojDO5zSF--naAi96XTgcAhd6pJkimsB2ZXPAUfcYImmh2Fp0OorEf3-23zIu6qbhjTR6_jvrrTno1QjvfK_zXZg-s0toXGkaT12BFNuRMVdDBZaCRaPLWoxlElJLliTU5VNj-JAg3ZCHOfHbl1NQp5CpguwLh-YtgrrBLpYoaZM4vM57NlwVeHTvzHYq7H8AtRXZmQ)
HousingAPI commands can accept an engine object to change the name of the database

## Usage

After installing the pre-requisites (in your virtual environment), run the command in your terminal



**Call from IDE/Terminal**
```
python housing_api.py
```
This will start the python script and ask for input from the user.
Alternatively, you can run the file from your IDE. 
Enter the number of the command you want to execute.



### **Available commands**
> **1. Add House** 
Input: Location, Developer, Price
Creates a database entry on the Houses table. 

> **2. Update House Price**  
Input: House ID, Price
Updates the price for the specified house id 

> **3. Reserve House**
Input: House ID 
Sets the reserve status of the House ID to 'True"

> **4. Check House Price** 
Input: House ID
Returns and displays the price of the specified House ID

> **5. Remove House**  
Input: House ID
Removes the database entry for the specified House ID 

> **6. Sell House** 
Input: House ID, Broker Name, Commission Percent, Downpayment Amount, Financing Option
Sets the sell status of the House ID to 'True'
Creates an entry for the **SoldHouses** table and **LoanTable** table



### Table Schema 

[![](https://mermaid.ink/img/pako:eNqFVF1v2jAU_SuWnzqUVA0f7YimSi1RNTTWotG9TEjWbewGi8RGdtIupfz3-SOQwFbNLwnnnnvuufeabHEqKcMxTnPQOuGQKSiWApnzVVaaafTlPQyv0ULm1APdYDiRRQGCahSG79doJkE8wlPO_hI45XvCge859idpGc5Rk7j1CfZMEyKfiYNRb654AapG31jdaykzmULJpRHjZY1aPGEvLJcbplrICKSsw4CSEYeRGeiS_NxQg9CW8INppl66iJ1MU2O3FHvb7bw61h8VCA2pszZNjt33PujwTirGM-E5nV5ulVwzRe6h6Ni3w-NaW_05UykTZRu74wJEykVGHjbWATqbgF4F6BbEOkBzyPgTz4J2Rp86U5GvYgN1YfTITSGrvWyn38Mqt-1qP-rxv_09KJ4ZtzmxKh6aVErZ8h7pFD65WE35G0p9BJ3tL0OntcCvvenQ77ihuwA6myYBumevR7xm9XvdadLgkxVL16fph5xC_iNlwfLcgx47GSQ56WYOtcO9L7cBelTcBV2mX4_t2s3fauMAF0wVwKn5mzvFJS5XzNwbHJtXCmq9xJ4HVSkXtUhxXKqKBbhyo2m-Cjh-hlwbdAMCx1v8G8f9_ufzaDgaX40uotF4EPWHAa5xHEbD8wt7RoPoajy8vIwGuwC_SWk0ogAzykupvjffHftwmr9c3NXY_QFqFXQ4?type=png)](https://mermaid.live/edit#pako:eNqFVF1v2jAU_SuWnzqUVA0f7YimSi1RNTTWotG9TEjWbewGi8RGdtIupfz3-SOQwFbNLwnnnnvuufeabHEqKcMxTnPQOuGQKSiWApnzVVaaafTlPQyv0ULm1APdYDiRRQGCahSG79doJkE8wlPO_hI45XvCge859idpGc5Rk7j1CfZMEyKfiYNRb654AapG31jdaykzmULJpRHjZY1aPGEvLJcbplrICKSsw4CSEYeRGeiS_NxQg9CW8INppl66iJ1MU2O3FHvb7bw61h8VCA2pszZNjt33PujwTirGM-E5nV5ulVwzRe6h6Ni3w-NaW_05UykTZRu74wJEykVGHjbWATqbgF4F6BbEOkBzyPgTz4J2Rp86U5GvYgN1YfTITSGrvWyn38Mqt-1qP-rxv_09KJ4ZtzmxKh6aVErZ8h7pFD65WE35G0p9BJ3tL0OntcCvvenQ77ihuwA6myYBumevR7xm9XvdadLgkxVL16fph5xC_iNlwfLcgx47GSQ56WYOtcO9L7cBelTcBV2mX4_t2s3fauMAF0wVwKn5mzvFJS5XzNwbHJtXCmq9xJ4HVSkXtUhxXKqKBbhyo2m-Cjh-hlwbdAMCx1v8G8f9_ufzaDgaX40uotF4EPWHAa5xHEbD8wt7RoPoajy8vIwGuwC_SWk0ogAzykupvjffHftwmr9c3NXY_QFqFXQ4)

##### Houses
- Table of houses for sale
1. id\_of_house (Primary Key)
2. location_city
3. developer
4. price
5. Reserved
6. Sold

##### SoldHouses 
- Table of houses sold
1. transaction_id (Primary Key)
2. id\_of_house (Foreign Key)
3. broker_name 
4. commission_percent
5. downpayment_amount
6. financing_option 

##### LoanTable 
- Table of remaining balance after sale of house
1. loan_id (Primary Key)
2. id\_of_house (Foreign Key)
3. original_loan
4. current_loan


## Testing
The tests were developed using pytest and located at subfolder 'tests'
The package **pytest** should be installed in the environment
The tests can be run by entering either lines in the console:
```
pytest
python -m pytest
```
while in the root directory of the program
Running the tests will create a temporary database file named **testhouselist.db**
The following files contain the testing codes
```
test_housing_application.py
test_housing_orm.py
test_housing_ui.py
````

## To be Implemented 
A CLI program that can interface with the LoanTable table to emulate accepting and processing payment for the loan
### Commands
```
Pay Loan
Check Loan
```


