#acts as UI and application layer





def validate_input(user_command: int) -> bool:
    user_command = int(user_command)
    match user_command:
        case 1 | 2 | 3 | 4 | 5 | 6:
            return True
        case _:
            raise ValueError("Invalid Command")

def process_command(user_command):
    match user_command:
        case 1:
            pass
        case 2:
            pass

def help_command():
    print("The following commands are available:")
    print("1. Add House")
    print("2. Update House")
    print("3. Reserve House")
    print("4. Check House Price")
    print("5. Remove House")
    print("6. Sell House")

if __name__ == '__main__':
    user_command = int(input("Enter the # Command:"))
    validate_input(user_command)

