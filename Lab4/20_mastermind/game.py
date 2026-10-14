import random
from logic import feedback


class Mastermind:
    def __init__(self, difficulty="medium"):
        settings = {
            "easy": {"length": 3, "max_symbol": 4, "turns": 10},
            "medium": {"length": 4, "max_symbol": 6, "turns": 8},
            "hard": {"length": 5, "max_symbol": 8, "turns": 6},
        }

        self.difficulty = difficulty
        config = settings[difficulty]

        self.length = config["length"]
        self.max_symbol = config["max_symbol"]
        self.turns = config["turns"]

        self.code = [
            str(random.randint(1, self.max_symbol))
            for _ in range(self.length)
        ]

        self.history = []
        self.game_over = False

    def run(self):
        print(f"\nMastermind - {self.difficulty.title()} difficulty")
        print(
            f"Enter {self.length} digits from 1 to "
            f"{self.max_symbol}."
        )

        while self.turns > 0 and not self.game_over:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.game_over = True
                print("Game ended.")
                return

            if (
                len(raw) != self.length
                or any(
                    ch not in "123456789"[:self.max_symbol]
                    for ch in raw
                )
            ):
                print(
                    f"Enter exactly {self.length} digits "
                    f"from 1 to {self.max_symbol}."
                )
                continue

            guess = list(raw)

            exact, partial = feedback(self.code, guess)

            self.history.append((raw, exact, partial))
            self.turns -= 1

            print("Exact:", exact, "Partial:", partial)

            if exact == self.length:
                self.game_over = True
                print("Cracked the code!")
                self.show_history()
                return

        self.game_over = True
        print("The code was", "".join(self.code))
        self.show_history()

    def show_history(self):
        print("\nGuess History")
        print("-" * 35)

        if not self.history:
            print("No guesses made.")
            return

        for number, (guess, exact, partial) in enumerate(
            self.history, 1
        ):
            print(
                f"{number}. {guess} -> "
                f"Exact: {exact}, Partial: {partial}"
            )