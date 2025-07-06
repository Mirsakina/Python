# try:
#     a = 1
#     print(a)
# except TypeError:
#     print("tipi sehvdir")
# else:
#     print("salam")
# finally:
#     a = "hello"  #bomba qosanda istifade
#     print("finally")


# class PhoneNumberError(Exception):
#     pass

# phone_number = input("944: ")
# if True:
#     raise PhoneNumberError("PHONE NUMBER IS NOT VALID")

# my_set = set()
# my_set.remove("Tuntun")

# try:
#     year = 2025
#     birth_year = int(input(">>"))
#     print(year - birth_year)
# except Exception:
#     print("YAZ DUZ")
# finally:
#     print("Thanks")


# money = 500

# def subtract_money():
#     global money 
#     money = 400
#     print(money)

# subtract_money()
# print(money)



def email_adress():
    email = input("Please enter your email adress:\n>> ")
    print(email.split("@"))

email_adress()


# set mena