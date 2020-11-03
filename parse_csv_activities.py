#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

from pathlib import Path
import csv
import sys

class Parse_csv_activities:
	"""
	Lire les infos d'un fichier activities.csv et proposer
	des données propres pour make_stats.py
	"""

	def __init__(self, activities_file="activities.csv"):
		self._activities_file = Path(activities_file)
		self._list_activities_types = self.list_activities_types()

	def list_activities_types(self):
		"""
		Vérifier que les types d'activités ne sont pas génériques
		Ex : 'Trail running' et non 'Running'
		"""

		list_activites = []
		bad_activities_types = ['Swimming', 'Running', 'Cycling']

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				list_activites.append(row['Activity Type'])
			
		for item in bad_activities_types:
			if item in list_activites:
				print("Il y a un élément {} dans les types d'activités du fichier CSV.".format(item))
				print("Arrêt du programme.")
				sys.exit(1)

		return list_activites
	
	def get_list_all_heart_rate(self):
		"""Retourner une liste de integers contenant toutes les moyennes
		des fréquence cardiaque pour toutes les activités"""
		list_heart_rate = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
					heart_rate = row['Average Heart Rate (bpm)']
					if heart_rate: # Ajouter uniquement les string non vides
						list_heart_rate.append(heart_rate)
				
		int_list_heart_rate = list(map(int, list_heart_rate))

		return int_list_heart_rate

	def get_list_heart_running_heart_rate(self):
		"""Retourner la liste des fréquences cardiaques des
		activités de running"""

		list_heart_rate = []
		running = ["Trail Running", "Street Running"]

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				sport = row['Activity Type']
				heart_rate = row['Average Heart Rate (bpm)']
				if heart_rate and sport in running: # Ajouter uniquement les string non vides
					list_heart_rate.append(heart_rate)
				
		int_list_heart_rate = list(map(int, list_heart_rate))

		return int_list_heart_rate

	def number_total_activities(self):
		"""Compter le nombre total d'activités tout sport confondu"""

		nb_activities = len(self.list_activities_types())
		return nb_activities

	def number_running_activities(self):
		"""Compter le nombre d'activités de running"""
		
		nb_activities = self.number_street_running_activities() + self.number_trail_running_activities()
		return nb_activities

	def number_trail_running_activities(self):
		"""Compter le nombre d'activités de running trail"""

		nb_trail_running = self._list_activities_types.count("Trail Running")
		return nb_trail_running

	def number_street_running_activities(self):
		"""Compter le nombre d'activités de running sur route"""

		nb_street_running = self._list_activities_types.count("Street Running")
		return nb_street_running

	def number_cycling_activities(self):
		"""Compter le nombre d'activités de vélo"""

		nb_activities = self.number_road_cycling_activities() + self.number_mountain_bike_activities()
		return nb_activities

	def number_road_cycling_activities(self):
		"""Compter le nombre d'activités de vélo de route"""
		
		nb_road_cycling = self._list_activities_types.count("Road Cycling")
		return nb_road_cycling
	
	def number_mountain_bike_activities(self):
		"""Compter le nombre d'activités de VTT"""
		
		nb_mountain_bike = self._list_activities_types.count("Mountain Biking")
		return nb_mountain_bike

	def number_swimming_activities(self):
		"""Compter le nombre d'activités de natation"""

		nb_activities = self.number_open_swimming_activities() + self.number_swimming_pool_activities()
		return nb_activities

	def number_open_swimming_activities(self):
		"""Compter le nombre d'activités de nage en eau libre"""

		nb_open_swimming = self._list_activities_types.count("Open Water Swimming")
		return nb_open_swimming
		
	def number_swimming_pool_activities(self):
		"""Compter le nombre d'activités de nage en piscine"""
		
		nb_swimming_pool = self._list_activities_types.count("Pool Swimming")
		return nb_swimming_pool

	def number_strength_training_activities(self):
		"""Compter le nombre d'activités de nage en piscine"""
		
		nb_strength_training = self._list_activities_types.count("Strength Training")
		return nb_strength_training

	"""
	Getters and setters
	"""

	def _get_activities_file(self):
		return self._activities_file

	def _set_activities_file(self, activities_file):
		self._activities_file = activities_file

	activities_file = property(_get_activities_file, _set_activities_file)

	

if __name__ == "__main__":

	activities = Parse_csv_activities("activities/activities.csv")

	print(activities.get_list_heart_rate())