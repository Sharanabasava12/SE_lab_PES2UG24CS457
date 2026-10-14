from game import Mastermind


def choose_difficulty():
    print("Mastermind")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choices = {
        "1": "easy",
        "2": "medium",
        "3": "hard",
    }

    while True:
        choice = input("Choose difficulty > ").strip()

        if choice in choices:
            return choices[choice]

        print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    difficulty = choose_difficulty()
    Mastermind(difficulty).run()