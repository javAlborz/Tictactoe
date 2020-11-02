import itertools
from colorama import Fore, Back, Style, init 
init()

def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
	#hori
	for row in game:
		if all_same(row):
			print(f"winner {row[0]} is the winner horisontally")
			return True
				
	#verti		
	for col in range(len(game)):
		check = [] 
		for row in game:
			check.append(row[col])
		if all_same(check):
			print(f"winner {row[0]} is the winner vertically")
			return True

	#diag1			
	diags = []
	for i in range(len(game)):
		diags.append(game[i][i])
	if all_same(diags):
		print(f"winner {diags[0]} is the winner diagonally(/)")
		return True

	#diag2
	diags= []
	cols = list(reversed(range(len(game))))
	rows = list(range(len(game)))

	for col, row, in zip(cols,rows):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"winner {diags[0]} is the winner diagonally(\\)")
		return True



def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:

			if player == 1:
				op_player = 2
			else: op_player = 1
			print(f"Denne plassen er tatt av {op_player}. Velg en annen") #prøv å legge inn hvem den er tatt av
			return game_map, False

		s = " "
		for i in range(len(game_map)):
			s += "  "+str(i)
		print(s)	

		if not just_display:
			game_map[row][column] = player

		for count, row in enumerate(game_map):
			colored_row = ""
			for item in row:
				if item == 0:
					colored_row += "   "
				elif item == 1:
					colored_row += Fore.MAGENTA + ' X ' + Style.RESET_ALL
				elif item == 2:
					colored_row += Fore.GREEN + ' O ' + Style.RESET_ALL

			print(count, colored_row)


		return game_map, True

	except IndexError as e:
		print("Tall må være fra 0 til 2", e)
		return game_map, False

	except Exception as e:	
		print("Noe gikk galt, vet ikke hva", e)
		return game_map, False


play = True
players = [1, 2]


while play:


	game = []

	game_size = 3
	for i in range(game_size):
		row = []
		for i in range(game_size):
			row.append(0)
		game.append(row)


	game_won = False 
	game, _ = game_board(game, just_display=True)
	player_choice = itertools.cycle([1,2])

	while not game_won:
		current_player = next(player_choice)
		print(f"Spiller: {current_player}")
		played = False

		while not played:			
			column_choice =int(input("Hvilken kolonne? (0,1,2): "))
			row_choice = int(input("Hvilken rad? (0,1,2): "))
			game, played = game_board(game, current_player, row_choice, column_choice)
			
			
		#needinput = True
		#while needinput:
			if win(game):  
				game_won = True
				again = input("Wanna go for another round? (y/n) ")
				if again.lower() == "y":
					print("Restarting")
					
				elif again.lower() == "n":
					print ("Game over")
					play = False
					#break
				else: 
					print("Not a valid input") 
					play = False
					#needinput =False
				
				
