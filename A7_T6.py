import random

random.seed(1234)

ROCK_ART = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS_ART = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

CHOICE_NAMES = {
    1: "rock",
    2: "paper",
    3: "scissors",
}

CHOICE_ART = {
    1: ROCK_ART,
    2: PAPER_ART,
    3: SCISSORS_ART,
}

SEPARATOR_LINE = "#" * 25
BOT_NAME = "RPS-3PO"


def get_winner(player_name: str, player_choice: int, bot_choice: int) -> str:
    player_choice_name = CHOICE_NAMES[player_choice]
    bot_choice_name = CHOICE_NAMES[bot_choice]

    if (
        (player_choice == 1 and bot_choice == 3)
        or (player_choice == 2 and bot_choice == 1)
        or (player_choice == 3 and bot_choice == 2)
    ):
        return f"{player_name} {player_choice_name} beats {BOT_NAME} {bot_choice_name}."
    else:
        return f"{BOT_NAME} {bot_choice_name} beats {player_name} {player_choice_name}."


def display_round(player_name: str, player_choice: int, bot_choice: int) -> None:
    print("Rock! Paper! Scissors! Shoot!\n")

    player_choice_name = CHOICE_NAMES[player_choice]
    bot_choice_name = CHOICE_NAMES[bot_choice]

    print(SEPARATOR_LINE)
    print(f"{player_name} chose {player_choice_name}.")
    print(CHOICE_ART[player_choice])
    print(SEPARATOR_LINE)

    print(f"{BOT_NAME} chose {bot_choice_name}.")
    print(CHOICE_ART[bot_choice])
    print(SEPARATOR_LINE)
    print()


def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")

    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print(f"Your opponent is {BOT_NAME}.")
    print("Game starts...\n")

    player_wins = 0
    player_losses = 0
    player_draws = 0

    bot_wins = 0
    bot_losses = 0
    bot_draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice_str = input("Your choice: ")

        if not choice_str.isdigit():
            print("Invalid choice.\n")
            continue

        choice = int(choice_str)

        if choice == 0:
            break

        if choice not in (1, 2, 3):
            print("Invalid choice.\n")
            continue

        bot_choice = random.randint(1, 3)
        display_round(player_name, choice, bot_choice)

        if choice == bot_choice:
            print(f"Draw! Both players chose {CHOICE_NAMES[choice]}.\n")
            player_draws += 1
            bot_draws += 1
        else:
            result = get_winner(player_name, choice, bot_choice)
            print(result + "\n")

            if result.startswith(player_name):
                player_wins += 1
                bot_losses += 1
            else:
                bot_wins += 1
                player_losses += 1

    print("\nResults:")
    print(
        f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})"
    )
    print(
        f"{BOT_NAME} - wins ({bot_wins}), losses ({bot_losses}), draws ({bot_draws})"
    )

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
