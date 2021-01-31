""" Provide information about previous University of Louisville basketball players now playing in the NBA"""

import json

def load_current_players():
		""" a file is opened with error checking and its contents are loaded into a dictionary
		"""
		try:
			with open(filename) as f:
				current_ul_nba_dict = json.load(f)
		except FileNotFoundError:
			print(f"Sorry, the file {filename} does not exist.")
		return current_ul_nba_dict


def print_current_players():
		""" Here is a dictionary printout futilizing a key-tracking list
		"""
		current_ul_nba_list = []
		index = 1
		for v,k in current_ul_nba_dict.items():
			print(index,':',v)
			current_ul_nba_list.append(v)
			index += 1
		return current_ul_nba_list


print()
print('---------------------------------------------------------------------------------------------------------------')
print()
print("Welcome to 'Where R They Now'")
print("---The program to help you find and follow University of Louisville basketball players currently in the NBA")
print()
print()
print('---------------------------------------------------------------------------------------------------------------')
print()
player_choice = ''
filename = 'ul_nba_current.json'

while True:

	

# opens file with error checking and its contents are loaded into a dictionary of former University of Louisville players CURRENTLY in the NBA matched with their team and updated from file ul_nba_current.json.
	current_ul_nba_dict = load_current_players()


# Here is a dictionary printout utilizing a key-tracking list  	
	current_ul_nba_list = print_current_players()

	print()
	print()
	player_choice = input('Please choose #1-6 to find out more about former UofL players currently in the NBA  or press "q" to quit:  ')
	if player_choice.lower() == 'q':
		print()
		print('Have a nice day!')
		break
	elif int(player_choice) > 0 and (int(player_choice) <= len(current_ul_nba_list)):
		print()
		print(current_ul_nba_list[int(player_choice)-1], "plays for the", current_ul_nba_dict.get(current_ul_nba_list[int(player_choice) -1]))
		print()
		print()


	


