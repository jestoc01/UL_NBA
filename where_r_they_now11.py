""" Provide information about previous University of Louisville basketball players now playing in the NBA"""

import json
import pandas as pd



def load_current_players_dict(filename):
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

	
def order_alltime_players_dataframe(filename):
	""" sort all UL players ever to play in NBA by field goal percentage
	"""
	ul_nba_players=pd.read_csv(filename)
	current_ul_nba_fgp_list = []
	FGP=ul_nba_players.sort_values(by=['FG%'], ascending=[False])
	FGP2=FGP.reset_index(drop=True)
	for i in current_ul_nba_list:
		field_goal_rank = FGP2[FGP2['Player']==i].index[0]
		current_ul_nba_fgp_list.append(field_goal_rank + 1)
	return current_ul_nba_fgp_list


# opens file with error checking and its contents are loaded into a dictionary of former University of Louisville players CURRENTLY in the NBA matched with their team and updated from file ul_nba_current.json.
current_ul_nba_dict = load_current_players_dict('ul_nba_current.json')

# Here is a dictionary printout utilizing a key-tracking list  	
current_ul_nba_list = load_current_players_list()

# Here are all the UofL players who ever played in the NBA ordered by field goal percentage
current_ul_nba_fgp_list=order_alltime_players_dataframe('ul_nba_players.csv')





print('\n---------------------------------------------------------------------------------------------------------------')
print("\nWelcome to 'Where R They Now'")
print("---The program to help you find and follow University of Louisville basketball players currently in the NBA")
print("\nThe former UofL players currently playing in the NBA are :\n")

while True:
	player_choice = ''
# Prints from dictionary imported from updatable file
	print_current_players()
	try:
		player_choice = input('\n\nPlease choose #1-6 to find out more about former UofL players currently in the NBA  or press "q" to quit:  ')
		if player_choice.lower() == 'q':
			print('\nHave a nice day!')
			break
		elif int(player_choice) > 0 and (int(player_choice) <= len(current_ul_nba_list)):
			print("\n\n", current_ul_nba_list[int(player_choice)-1], "plays for the", current_ul_nba_dict.get(current_ul_nba_list[int(player_choice) -1], "\n\n"))
			list_item = int(player_choice)-1
			print("\n He ranks #", current_ul_nba_fgp_list[list_item], " in field goal percentage among all UofL players who ever played in the NBA.")
			
		elif int(player_choice) <= 0:
			print("\n\nUofL's not that bad!")
		elif int(player_choice) > len(current_ul_nba_list):
			print("\n\nUofL's good, but they don't have that many players in the NBA!")
	except ValueError:
		print("\n\nPlease enter only one of the following integers\n\n")

	


