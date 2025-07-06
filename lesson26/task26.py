list = [
    [f"{x+y}" for y in range(3)]for x in range(1, 9, 3)
]
print(list)

for i in list:
    print("|".join(i)) 

TURN = "X"
while True:
    player_turn = int(input("Please enter where is your X:\n>> "))
    row = (player_turn - 1) % 3
    column = player_turn // 3
    list[row][column] == "X"

# 1 [0][0]
# 2 [0][1]
# 3 [0][2]
# 4 [1][0]
# 5 [1][1]
# 6 [1][2]
# 7 [2][0]
# 8 [2][1]
# 9 [2][2]
