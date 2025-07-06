# # def hello():
# #     print("Hello world!")
# # hello()

# # for x in range(3):
# #     hello()
# import random

# def adress():
#     adress = input("Please enter your adress:")
# adress()

# def random_num():
#     print(random.randint(1, 100))
# random_num()

def round_up():
    data = {
        "potato": 750,
        "tomato": 340
    }
    data["potato"] = data["potato"] * 1.2
    data["tomato"] = data["tomato"] * 1.2
    data["potato"] = round(data["potato"])
    data["tomato"] = round(data["tomato"])
    print(data["potato"] + data["tomato"])
round_up()


