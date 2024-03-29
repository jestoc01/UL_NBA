# UL_NBA
University of Louisville basketball players and the NBA

This project utilizes Python to gain insight on University of Louisville basketball players who went on to play in the NBA. It includes the following Code Louisville portfolio project requirements:
 1) Implement a 'master loop' console application where the user can repeatedly enter commands, including choosing to exit. --- where_r_they_nowll.py contains a master loop that presents the user with a choice of players and an exit option. Once a player is selected the program returns that player's current NBA team and again presents the user with the menu of players.
 2) Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in the program -- where_r_they_nowll.py reads data from ul_nba_current.json and uses it to create a dictionary (current_ul_nba_dict). This dictionary is used to print out the menu choices and to determine the team on which a selected player currently plays. This dictionary is also used to create the list, current_ul_nba_list. This list is then used to locate the player name when an integer menu selection is made by the user.
 3) Read data from an external file, such as text, JSON, or CSV and use that data in the program -- where_r_they_nowll.py reads data from ul_nba_current.json and uses it to create the dictionary (current_ul_nba_dict)
 4) Create and call at least 3 functions or methods, at least one of which must return a value that is used in the code.-- where_r_they_now11.py utilizes the 3 functions: load_current_players_dict(), load_current_players_list(), and print_current_players().
 5) Create 3 or more unit test for the applicaton (see tests.py) -- test_ulnbacurrentjsonfile(), test_ulnbacurrentlist(), test_printcurrentplayers()
 6) "Stretch Features": Use pandas to perform a data analysis. -- where_r_they_now11.py uses pandas to read a csv file containing data for all UL players ever to play in the NBA and sort them by field goal percentage. Where_R_They_Now__Jupyter_Notebook_Version2 also uses pandas and Seaborn to provide a clearer view of field goal percentage and other data such as free throw percentage and three point percentage for these players and their ranking relative to all other UL players.

 In addition to the command line programs(where_r_they_now11.py and tests.py) and the Jupyter Notebook(Where_R_They_Now__Jupyter_Notebook_Version2.ipynb) discussed above this repository includes:
 2 Excel files(NworaNewMinus.xlsx and NworaNone.xlsx), a csv file(Ul_nba_player.csv), and a json file(ul_nba_current.json).

 A requirements.txt file is also included.
