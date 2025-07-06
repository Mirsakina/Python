# def greet():
#     name = input("Please enter your name:\n>> ")

# def welcome():
#     name = input("Please enter your name:\n>> ")
    
# def hello():
#     name = input("Please enter your name:\n>> ")

# def salute():
#     name = input("Please enter your name:\n>> ")

# def greet(name):
#     print(f"Hello, {name}")

# greet("Riad")

# def complete_name(name, surname):
#     print(f"Hello: {name} {surname}")

# complete_name("Mirsakina", "Xankishiyeva")


# def e_mail_address(mail):
#     print(f"Your e-mail: {mail}")

# mail = input("Please enter your e-mail:\n>> ")
# e_mail_address(mail)


# def square(num):
#     print(num**2)

# square(4)
# square(5)


# def complete_gmail(name = "anonim", gmail="gmail.com"):
#     print(f"Hello {name} {gmail}")

# name = input("Plaese enter your name\n>> ")
# gmail = input("Plaese enter your e-mail\n>> ")

# complete_gmail()



# def calculate(m = 9, n = 6):
#     print(f"{m + n}")

# calculate(4, 5)
# calculate(4)
# calculate()


# def give_a_voice(age="I don't now your AGE"):
#     if age >=18:
#         print("Get take a voice!")
#     else:
#         print("You haven't grown up yet!")

# age = int(input("Plaese enter your age:\n>> "))
# give_a_voice(age)



# def hello(count=3):
#     for i in range(count):
#         print("Hello world!")

# count = int(input("Plaese enter the count of hello:\n>> "))
# hello(count)

# import secrets
# import string

# def generate_OTP_code(length=4):
#     otp_code = "".join(secrets.choice(string.digits)
#                        for x in range(length))
#     print(otp_code)
# generate_OTP_code(5)



# def main():
#     total = 25
#     return True

# print(main())



# def calculate(m, n):
#     return m + n

# print(calculate(6, 5))
    


# def calculate(a: int, b: int) -> int:
#     return a + b

# calculate(3, 5)



# def count_name(name: str, number: int) -> str:
#     result = " "
#     for i in range(number,result):
#         result += name 
#     return result

# count_print = count_name("Jon", 3)
# print(count_print)



# def split_filename(filename):
#     result = []
#     split =  filename.split(".")
#     result.append(split)
#     return result
# filename = [
#     "qaymag_audio.mp3",
#     "resum.pdf",
#     "image.jpg",
#     "virus.exe"
# ]

# output = split_filename(filename)
# print(output)


