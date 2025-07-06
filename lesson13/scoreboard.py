from questions import questions

high_scores = {}

def start_quiz():
    while True:
        name = input("Please enter your name:\n>> ")
        if name.isalpha():
            break
        else:
            print("Name should contain only letters. Please try again.")

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        while True:
            answer = input("Please enter your answer:\n>> ").upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {q['answer']}")

    print(f"\n{name}, you scored {score} out of {len(questions)}.")
    high_scores[name] = score

def view_scores():
    if not high_scores:
        print("No scores yet.")
    else:
        print("\n--- High Scores: ---")
        for name, score in high_scores.items():
            print(f"{name}: {score} points")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Exit")

        choice = input("Please choose:\n>> ")

        if choice == "1":
            start_quiz()
        elif choice == "2":
            view_scores()
            continue
        elif choice == "3":
            exit("Terminal is closed.")
        else:
            print("Please enter 1, 2 or 3")
            continue  

main_menu()
