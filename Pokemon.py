'''import random as r
pokemon_list = ["charjabug", "charmander", "bulbasaur", "pikachu", "blastoise", "ekans", "sandslash", "clefairy", "jigglypuff", "diglett", "growlithe", "machamp", "eevee", "mewtwo", "articuno", "ninetails", "onix", "starmie", "gloom", "raichu", "zamazenta", "palkia", "bayleef", "umbreon", "zekrom", "azelf", "lunala", "morpeko", "regice", "sceptile", "groudon", "dreepy", "primarina", "goodra", "grimmsnarl", "drednaw", "yamper", "togekiss", "staravia", "drifblim", "monferno", "muk", "scorbunny", "zeraora", "gyarados", "greninja", "ampharos", "necrozma", "mudkip", "morelull", "mienshao", "metagross", "medicham", "mawile", "lycanroc", "luxray", "lucario", "ludicolo", "liepard", "lapars", "kommo-o", "kingdra"]
# pokemon_list.sort()
# print(len(pokemon_list), pokemon_list)

player_1 = pokemon_list[r.randint(0,len(pokemon_list)-1)]
player_2 = pokemon_list[r.randint(0,len(pokemon_list)-1)]
# print(a.format(str(b)))
# print("Darren is a " + c + ".")
print(f"Darren sents out {player_1.title()} vs " + f"Ling sents out {player_2.title()}.")
'''

import random as r
pokemon_list = ["charjabug", "charmander", "bulbasaur", "pikachu", "blastoise", "ekans", "sandslash", "clefairy", "jigglypuff", "diglett", "growlithe", "machamp", "eevee", "mewtwo", "articuno", "ninetails", "onix", "starmie", "gloom", "raichu", "zamazenta", "palkia", "bayleef", "umbreon", "zekrom", "azelf", "lunala", "morpeko", "regice", "sceptile", "groudon", "dreepy", "primarina", "goodra", "grimmsnarl", "drednaw", "yamper", "togekiss", "staravia", "drifblim", "monferno", "muk", "scorbunny", "zeraora", "gyarados", "greninja", "ampharos", "necrozma", "mudkip", "morelull", "mienshao", "metagross", "medicham", "mawile", "lycanroc", "luxray", "lucario", "ludicolo", "liepard", "lapars", "kommo-o", "kingdra"]
# pokemon_list.sort()
# print(len(pokemon_list), pokemon_list)

# Define function of poekmon_battle
def pokemon_battle(player1_name, player2_name):
	player1_num = 0
	player2_num = 0
	while player1_num < 6 and player2_num < 6:
		player1_pokemon = pokemon_list[r.randint(0,len(pokemon_list)-1)]
		player2_pokemon = pokemon_list[r.randint(0,len(pokemon_list)-1)]
		print(f"{player1_name} sents out {player1_pokemon.title()} vs {player2_name} sents out {player2_pokemon.title()}.")
		winner = input(f"Who wins? (if {player1_name} wins input 1, if {player2_name} wins input 2, if no winner input 0): ")
		if winner == "1":
			player1_num += 1
			print(f"{player1_name} {player1_num} vs {player2_name} {player2_num}")
		elif winner == "2":
			player2_num += 1
			print(f"{player1_name} {player1_num} vs {player2_name} {player2_num}")
		elif winner == "0":
			print(f"{player1_name} {player1_num} vs {player2_name} {player2_num}")
			continue
		else:
			print("Please input 0, 1 or 2.")
	if player1_num > player2_num:
		print(f"The winner is {player1_name}!")
	else:
		print(f"The winner is {player2_name}!")


print("Pokemon Battle!\nThe one who wins 6 times firstly will be the winner.")

player1_name = input("Please input the name of Player 1: ")
player2_name = input("Please input the name of Player 2: ")

game_continue = input("\nAre you ready to start? (yes/no): ")

while game_continue == "yes":
	pokemon_battle(player1_name, player2_name)
	game_continue = input("\nDo you want to play again? (yes/no): ")

print("The battle is finished. Have a good day!")



