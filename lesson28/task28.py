# def sentences_formating(*letters):
#     return "-".join(letters)

# print(sentences_formating("", "Miran"))



# def max_temperature(*temperature):
#     return max(temperature)

# print(max_temperature(23, 783, 3883, 334))



# def last_child_name(*names):
#     if not names:
#         return "Adam yoxdu"
#     return names[-1]

# print(last_child_name())


# def all_user_information(**kwargs):
#     return kwargs

# print(all_user_information(name = "Ali", age = 24, color = "red"))


# def film(**kwargs):
#     return kwargs

# print(all_user_information(janr = "comedy", speed = 2, name = "Tom Sawyer"))


# def all_user_information(**kwargs):
#     if not "name" in kwargs:
#         return "Ad yoxdu"
#     return kwargs["name"]

# print(all_user_information())

# def process_data(**user_data):
#     return user_data.get("name", "No name")



# class Table:
#     color = "brown"
#     height = 1
#     width = 2

# print(Table.color)


class Cat:
    name = "Garfield"
    age = 2
my_cat = Cat()
print(my_cat.name)


for cat in range(10_000_000):
    some_cat = Cat()