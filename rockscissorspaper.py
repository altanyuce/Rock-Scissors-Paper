import random
game = ["Rock", "Scissors", "Paper"]
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Scissors and 2 for Paper.\n"))
game1 = int(len(game)) - 1
game2 = random.randint(0, game1)
game3 = game[game2]
game4 = game[player_choose]
if player_choose == 0 and game2 == 1:
    print(f'''You chose {game4}.\nComputer chose {game3}. You win!''')
elif player_choose == 1 and game2 == 2:
    print(f"You chose {game4}.\nComputer chose {game3}. You win!")
elif player_choose == 2 and game2 == 0:
    print(f"You chose {game4}.\nComputer chose {game3}. You win!")
elif player_choose == game2:
    print(f"You chose {game4}.\nComputer chose {game3}. Draw!")
else:
    print(f"You chose {game4}.\nComputer chose {game3}. You lost.")


