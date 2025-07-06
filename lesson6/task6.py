from random import*
# passcode = "5579"
# user_code = input("Enter your code:\n>>")
# if passcode == user_code:
#     print("It is correct passcode"),
# else:
#     print("Passcode uncorrect")


# speed = 65
# limit = 70
# if speed > limit:
#     print("fine")
# else:
#     print("Have a nice day!")


a = randint(0, 100)
if a % 2 == 0:
    print("It is number was even!")
else:  
    print("The number was odd!")


temperature = [24.4, 29.6, 23.5, 22.2]
orifmetik = sum(temperature)/len(temperature)
round = round(orifmetik, 2)
print(round)