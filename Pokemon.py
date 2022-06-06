import random as r
pokemon_list = ["charjabug", "charmander", "bulbasaur", "pikachu", "blastoise", "ekans", "sandslash", "clefairy", "jigglypuff", "diglett", "growlithe", "machamp", "eevee", "mewtwo", "articuno", "ninetails", "onix", "starmie", "gloom", "raichu", "zamazenta", "palkia", "bayleef", "umbreon", "zekrom", "azelf", "lunala", "morpeko", "regice", "sceptile", "groudon", "dreepy", "primarina", "goodra", "grimmsnarl", "drednaw", "yamper", "togekiss", "staravia", "drifblim", "monferno", "muk", "scorbunny", "zeraora", "gyarados", "greninja", "ampharos", "necrozma", "mudkip", "morelull", "mienshao", "metagross", "medicham", "mawile", "lycanroc", "luxray", "lucario", "ludicolo", "liepard", "lapars", "kommo-o", "kingdra"]
# pokemon_list.sort()
# print(len(pokemon_list), pokemon_list)

player_1 = pokemon_list[r.randint(0,len(pokemon_list)-1)]
player_2 = pokemon_list[r.randint(0,len(pokemon_list)-1)]
# print(a.format(str(b)))
# print("Darren is a " + c + ".")
print("Total score: Darren 1 vs 1 Ji\nRound 3")
print(f"Darren sents out {player_1.title()} vs " + f"Ling sents out {player_2.title()}.")
# test git push