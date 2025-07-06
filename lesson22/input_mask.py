# def mask_username(username: str) -> str:
#     firstname, lastname = username.split()
#     masked_name = f"{firstname[0]}*** {lastname[0]}***"
#     return masked_name
# result = mask_username("Alice Veliyeva")
# print(result)



def mask_username(username: str) -> str:
    username_parts = username.title().split()

    if len(username_parts) == 2:
        masked_name = f"{username_parts[0][0]}*** {username_parts[1][0]}***"
        return masked_name
    
    elif len(username_parts) == 3:
        masked_name = f"{username_parts[0][0]}*** {username_parts[1][0]}*** {username_parts[2][0]}***"
        return masked_name
    
    else:
        return "A name cannot consist of four words." 
    
username = input("Please enter your fullname:\n>> ")
result = mask_username(username)
print(result)
    
