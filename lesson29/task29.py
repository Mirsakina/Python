girls = ["Anastasia", "Irina", "Maryana", 
         "Oksana", "Victoria", "Natasha",
         "Polina", "Alexandra", "Alla"]

def name_len(name: str):
    return len(name) >= 6

new_ls = list(filter(name_len, girls))
print(new_ls)


dt = {
    "USA":{
        "Uran_missle": 500_000,
        "B-2": 3
    },
    "Iran": {
        "Uran_missle": 25_000,
        "B-2": 0
    },
    "Israel": {
        "Uran_missle": 25_000,
        "B-2": 0
    }
}

def dt_filter(key):
    return {dt[key]["Uran_missle"] >= 500_000 and 
            bool(dt[key]["B-2"])
            }