# UL_NBA
University of Louisville basketball players and the NBA
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jestoc01/UL_NBA.git/master)
.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/jestoc01/UL_NBA.git/master
 This project utilizes Python to gain insight on University of Louisville basketball players who went on to play in the NBA. It includes the following Code Louisville portfolio project requirements:
 1) Implement a 'master loop' console application where the user can repeatedly enter commands, including choosing to exit. --- where_r_they_nowll.py contains a master loop that presents the user with a choice of players and an exit option. Once a player is selected the program returns that player's current NBA team and again presents the user with the menu of players.
 2) Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in the program -- where_r_they_nowll.py reads data from ul_nba_current.json and uses it to create a dictionary (current_ul_nba_dict). This dictionary is used to print out the menu choices and to determine the team on which a selected player currently plays. This dictionary is also used to create the list, current_ul_nba_list. This list is then used to locate the player name when an integer menu selection is made by the user.
 3) Read data from an external file, such as text, JSON, or CSV and use that data in the program -- where_r_they_nowll.py reads data from ul_nba_current.json and uses it to create the dictionary (current_ul_nba_dict)
 4) Create and call at least 3 functions or methods, at least one of which must return a value that is used in the code.-- where_r_they_now11.py utilizes the 3 functions: load_current_players_dict(), load_current_players_list(), and print_current_players().
 5) Create 3 or more unit test for the applicaton (see tests.py) -- test_ulnbacurrentjsonfile(), test_ulnbacurrentlist(), test_priintcurrentplayers()
 6) "Stretch Features": Use pandas to perform a data analysis. -- where_r_they_now11.py uses pandas to read csv file containing data for all UL players ever to play in the NBA, sort them by field goal percentage, and rank current players relative to all UL players.
