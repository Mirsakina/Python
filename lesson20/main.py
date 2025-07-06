import random
from datetime import datetime
from menu import menu
from settings import MAX_CLIENT_BASKET_CAPACITY



def restaurant_working_hours():
    open_working_hours = 9
    close_working_hours = 21

    current_time = datetime.now().hour 
    
    if open_working_hours <= current_time < close_working_hours:
        print("Welcome to KFC!")
    else:
        print("Sorry we are closed!")
        exit()
restaurant_working_hours()

def user_name():
    while True:
        name = input("Please enter your name:\n>> ")
        
        if name.isalpha():
            return name
        else:
            print("Please enter your name correct.")  
user_name()

balance = random.randint(500, 1000)
print(f"Hello, my balance is: {balance} AZN. What can I buy?")

def print_menu():
    print("\nMenu              |               Price")
    print("=======================================")
    
    for num , food in enumerate(menu, start=1):
        print(f"{num}.{food["food_name"]}---------------{food["food_price"]}AZN")
print_menu()


client_basket = [ ]

def client_choice():
       while len(client_basket) < MAX_CLIENT_BASKET_CAPACITY:
            food_choice = input(f"\nPlease enter food number {len(client_basket)+1} you want (or type 'exit' to quit):\n>> ")
            
            if food_choice.lower() == "exit":
                    print("Exiting the restaurant...")
                    break
            
            if food_choice.isdigit():
                food_choice = int(food_choice)

                if 1 <= food_choice <= len(menu):
                    food_index = food_choice - 1
                    customer_food = menu[food_index]
                    
                    if len(client_basket) < MAX_CLIENT_BASKET_CAPACITY:
                        client_basket.append(customer_food)
                        print(f"You added: {customer_food["food_name"]}")
                        print(f"Your basket now:  {[item['food_name'] for item in client_basket]}")
                    
                    else:
                        print("Your basket is full.")
                        break
                
                else:
                    print(f"Please enter a number between 1 and {len(menu)}.")
            
            else:
                print("Try again...")
client_choice()

def print_receipt():
    print("\n========== RECEIPT ==========")
    total = 0
    for i in client_basket:
        print(f"{i['food_name']} - {i['food_price']} AZN")
        total += i['food_price']
    print("-----------------------------")
    print(f"Total: {total} AZN")
    print(f"Your remaining balance: {balance - total} AZN")
    print("Thank you for visiting KFC!")
    print("=============================")
print_receipt()








# 1. KFC Basket Inventory Management
# ==================================
# Client:
# a. balance (500-1000)
# b. maximum inventory capacity - 2
# c. inventory

# KFC:
# 1. menu (food - price)
# 2. cash

# EXTRA!!!!!!!!!!!!!! (+1)
# 2. open_working_hours
#    close_working_hours

# Result:
# 1. Receipt (Bill)

# 2.
