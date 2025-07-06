import random

leaderboard = {}

while True:
    players = []
    num_players = int(input("Please enter the number of players?\n>> "))

    for i in range(num_players):
        name = input(f"Please enter player's name {i + 1}:\n>> ")
        players.append(name)
        if name not in leaderboard:
            leaderboard[name] = 0

    round_scores = {}

    print("\nWe roll the dice...\n")
    for player in players:
        roll = random.randint(1, 6)
        round_scores[player] = roll
        print(f"{player} threw out a number: {roll}")

    max_score = max(round_scores.values())
    winners = [player for player, score in round_scores.items() if score == max_score]

    if len(winners) == 1:
        winner = winners[0]
        print(f"\nThe winner of the round: {winner}!\n")
        leaderboard[winner] += 1
    else:
        print(f"\nA draw between: {', '.join(winners)}!\n")
        for w in winners:
            leaderboard[w] += 1

    print("Leaderboard:")
    for player, score in leaderboard.items():
        print(f"{player}: {score} wins")

    again = input("\nShould you play it again? Please answer yes or no: ")
    if again.lower() != "yes":
        print("\nThanks for playing!")
        break