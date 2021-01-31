""" Provide information about previous University of Louisville basketball players now playing in the NBA"""

import json

def load_current_players_dict():
		""" opens file with error checking and loads contents into dictionary
		"""
		try:
			with open(filename) as f:
				current_ul_nba_dict = json.load(f)
		except FileNotFoundError:
			print(f"Sorry, the file {filename} does not exist.")
		return current_ul_nba_dict

def load_current_players_list():
		""" Forms  a key-tracking list from the dictionary
		"""
		current_ul_nba_list = []
		for v,k in current_ul_nba_dict.items():
			current_ul_nba_list.append(v)
		return current_ul_nba_list

def print_current_players():
		""" Prints indexed players from dictionary for selection by user 
		"""
		index = 1
		print()
		for v,k in current_ul_nba_dict.items():
			print(index,':',v)
			index += 1


filename = 'ul_nba_current.json'

# opens file with error checking and its contents are loaded into a dictionary of former University of Louisville players CURRENTLY in the NBA matched with their team and updated from file ul_nba_current.json.
current_ul_nba_dict = load_current_players_dict()

# Here is a dictionary printout utilizing a key-tracking list  	
current_ul_nba_list = load_current_players_list()

print('\n---------------------------------------------------------------------------------------------------------------')
print("\nWelcome to 'Where R They Now'")
print("---The program to help you find and follow University of Louisville basketball players currently in the NBA")
print("\nThe former UofL players currently playing in the NBA are :\n")

while True:
	player_choice = ''
# Prints from dictionary imported from updatable file
	print_current_players()
	player_choice = input('\n\nPlease choose #1-6 to find out more about former UofL players currently in the NBA  or press "q" to quit:  ')
	if player_choice.lower() == 'q':
		print('\nHave a nice day!')
		break
	elif int(player_choice) > 0 and (int(player_choice) <= len(current_ul_nba_list)):
		print("\n\n", current_ul_nba_list[int(player_choice)-1], "plays for the", current_ul_nba_dict.get(current_ul_nba_list[int(player_choice) -1], "\n\n"))
	elif int(player_choice) <= 0:
		print("\n\nUofL's not that bad!")
	elif int(player_choice) > len(current_ul_nba_list):
		print("\n\nUofL's good, but they don't have that many players in the NBA!")


	


