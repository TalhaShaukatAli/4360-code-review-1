# 4360-banking

Get Started    
    - python index.py 

User Interface
    - deposit [amount] [account_number] - deposits the amount (float number) into the account_number (integer)
    - withdraw [amount] [account_number] - withdraws the amount (float number) from the account_number (integer)
    - transfer [amount] [from_account_number] [to_account_number] - transfers the amount (float number) from the from_account_number (integer) to the to_account_number (integer)


Requirements
    - Functional Requirements
        - software takes user input for login name and password
        - login attempts will be limited to 3
        - software has a help menu
        - software shows list of accounts
        - software shows the balanace of a specific account
        - software deposits into an account
        - software withdraws money from an account
        - software transfers money between accounts
        - transfers between accounts will be limited to 3 per sesssion
        - transfers will be limited 10000 per transaction

    - Non Functional Requirements
        - CLI user interface
        - use a while true loop, instead of once and done.  This will facilitate logins better
        - no individual process should take longer than 1000ms to return the result
