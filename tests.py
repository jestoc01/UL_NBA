import unittest
from unittest.mock import patch
from io import StringIO
from where_r_they_now11 import load_current_players_dict
from where_r_they_now11 import load_current_players_list
from where_r_they_now11 import print_current_players

class JsonFilesTestCase(unittest.TestCase):
	def test_ulnbacurrentjsonfile(self):
		""" Does the file 'ul_nba_current.json' work"""
		current_players_dict = load_current_players_dict("ul_nba_current.json")
		self.assertEqual(current_players_dict,  {"Gorgui Dieng":"Grizzlies", "Montrezl Harrell":"Lakers", "Damion Lee":"Warriors", "Donovan Mitchell":"Jazz", "Jordan Nwora":"Bucks", "Terry Rozier":"Hornets"} )

	def test_ulnbacurrentlist(self):
		current_ul_nba_list = load_current_players_list()
		self.assertIn("Gorgui Dieng", current_ul_nba_list)

	def test_printcurrentplayers(self):
		with patch('sys.stdout', new = StringIO()) as fake_out:
			print_current_players()
			self.assertIn("Gorgui Dieng", fake_out.getvalue())


if __name__ =='__main__':
	unittest.main()