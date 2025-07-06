# import faker 
# fake = faker.Faker()

# print(fake.name())


# fake = faker.Faker()
# for i in range (1000):
#     print(fake.country())


# from faker import Faker
# fake = Faker()


# def dict_app(num):
#     data = { }
    
#     for i in range(1, num + 1):
#       data[f"user_number_{num}"] = fake.image_url()

#       return data
    
# num = int(input("Please enter any number:\n>> "))
# print(dict_app(num)) 




def main(birth_year, age):
    age = 2025 - birth_year
    return age >= 18
