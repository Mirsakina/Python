PIN_CODE = "1505"
balance = 500


logged_in = False 

print("""Welcome to JATM""")


while True:
    if not logged_in:
        user_pin = input("Enter your PIN code:\n>> ") 

    if user_pin == PIN_CODE:
        logged_in = True
        print("""
        [1] Withdraw
        [2] Deposit
        [3] Check balance
        [4] Change PIN
        [5] Exit
        """)
        user_operation = input("Enter an operation:\n>> ").strip()
    else:
        def login():
            attempts = 3
            while attempts > 0:
                entered_pin = input("Enter your 4-digit PIN: ").strip()
                if entered_pin == PIN_CODE:
                    print("Login successful.\n")
                    return True
                else:
                    attempts -= 1
                    print(f"Incorrect PIN. Attempts remaining: {attempts}")
            print("Too many incorrect attempts. Exiting.")
            return False
        login()

    if user_operation == "1":
        withdraw_amount = int(input("Enter amount to withdraw (min. 1 AZN):\n>> "))
        
        if (withdraw_amount > balance) or (withdraw_amount == balance == 0):
            print("Kredit??? yes?? go okk.. Adam kimi daxil ele.")
            continue

        balance -= withdraw_amount
        print(balance)
    elif user_operation == "2":
        deposit_amount = int(input("Enter amount to deposit (min. 1 AZN):\n>> "))

        if deposit_amount <= 0:
            print("Adam kimi daxil ele.")
            continue

        balance += deposit_amount
        print(f"{deposit_amount} AZN was added to your account.\nBalance: {balance}")
    elif user_operation == "3":
        print(balance)
    elif user_operation == "4":
        new_user_pin = input("Enter new PIN code:\n>> ") 

        is_valid = (len(new_user_pin) == 4
                    and new_user_pin.isdigit() 
                    and new_user_pin != PIN_CODE)
    
        if not is_valid:
            print("Adam kimi daxil ele.")
            continue

        PIN_CODE = new_user_pin
        logged_in = False
    elif user_operation == "5":
        exit("Terminal is closed.")
    else:
        print("No such operation. Adam kimi daxil ele.")