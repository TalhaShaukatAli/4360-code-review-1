import os
from message import Message
from interface import UserInterface
from auth import Auth


def main():
    message = Message()
    ui = UserInterface()
    auth = Auth()
    
    #authenticate user
    login_attempts = 0
    failed_attempt = False
    while login_attempts < 3:
        os.system('cls')
        if failed_attempt:
            message.print("Please try again")
        else:
            message.print("Welcome to the bank of Py!")
            message.print("Please login to continue.")
        
        user_name = input("Username: ")
        password = input("Password: ")

        user = auth.login(user_name, password)
        if not user:
            login_attempts += 1
            failed_attempt = True
        else:
            break

    #register UI
    ui.register_command("deposit", user.deposit, "deposit [account_number] [amount] - deposit an amount into an account")
    ui.register_command("withdraw", user.withdraw, "withdraw [account_number] [amount] - withdraw an amount from an account")
    ui.register_command("transfer", user.transfer, " transfer [from_account_number] [to_account_number] [amount] - transfer an amount from one account to another account")

    #Main Loop
    while True:
        os.system('cls')
        message.print("What can we do for you today?")
        user.show_accounts()
        ui.show_commands()
        user_inputs = input().lower().split(" ")

        #exit check
        if(user_inputs[0] == "exit"):
            print("Good bye")
            break

        
        ui.execute_command(user_inputs[0], user_inputs[1:])
        

if __name__ == "__main__":
    main()
   

