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
	des données brutes propres pour make_statistics.py
	"""

	def __init__(self, activities_file):
		self._activities_file = Path(activities_file)

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

	def get_list_heart_rate(self, month, sport):
		"""
		Retourner une liste comprenant tous les integers des moyennes
		de fréquence cardiaque pour un mois choisi, et pour un sport choisi,
		ou pour tous les temps pour tous les sports

		sport accepte :
			- "All"
			- "Cyclisme"
			- "Running"
			- "Renfo"

		month accepte :
			- "All"
			- "YYYY-MM"

		Exemples : 
		get_list_heart_rate(month="All", sport="All")
		get_list_heart_rate(month="2020-07", sport="Running")
		get_list_heart_rate(month="2020-07", sport="All")
		get_list_heart_rate(month="All", sport="Cyclisme")
		get_list_heart_rate(month="All", sport="Renfo")
		"""

		if sport == "All":
			sport = ["Trail Running", "Street Running", "Road Cycling", "Mountain Biking", "Strength Training"]
		elif sport == "Cyclisme":
			sport = ["Road Cycling", "Mountain Biking"]
		elif sport == "Running":
			sport = ["Street Running", "Trail Running"]
		elif sport == "Renfo":
			sport = ["Strength Training"]
		elif sport == "Natation":
			print("Données de fréquence cardiaque indisponibles en natation.")
			sys.exit(1)
		
		list_heart_rate = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:

				heart_rate = row["Average Heart Rate (bpm)"]
				month_row = row["Start Time"][:7]
				sport_row = row["Activity Type"]

				for i in sport:
					if i == sport_row:

						if month == "All":
							if heart_rate: # Ajouter uniquement les string non vides
								list_heart_rate.append(heart_rate)

						elif month_row == month:
							if heart_rate: # Ajouter uniquement les string non vides
								list_heart_rate.append(heart_rate)

		# Conversion items de la liste string vers int 
		int_list_heart_rate = list(map(int, list_heart_rate))

		return int_list_heart_rate
		
	def get_number_activities(self, month, sport):
		"""
		Compter le nombre d'activités

		sport accepte :
			- "All"
			- "Cyclisme"
			- "Running"
			- "Renfo"

		month accepte :
			- "All"
			- "YYYY-MM"
		"""

		if sport == "All":
			sport = ["Trail Running", "Street Running", "Road Cycling", "Mountain Biking",
						"Open Water Swimming", "Pool Swimming", "Strength Training"]
		elif sport == "Cyclisme":
			sport = ["Road Cycling", "Mountain Biking"]
		elif sport == "Running":
			sport = ["Street Running", "Trail Running"]
		elif sport == "Renfo":
			sport = ["Strength Training"]
		elif sport == "Natation":
			sport = ["Open Water Swimming", "Pool Swimming"]

		number_activities = 0

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:

				month_row = row["Start Time"][:7]
				sport_row = row["Activity Type"]

				for i in sport:
					if i == sport_row:

						if month == "All":
							number_activities += 1

						elif month_row == month:
							number_activities += 1

		return number_activities

	def get_list_distances(self, month, sport):
		"""
		Connaitre une liste des distances en fonction
		des sports ou en général

		sport accepte :
			- "All"
			- "Cyclisme"
			- "Running"
			- "Natation"

		month accepte :
			- "All"
			- "YYYY-MM"
		"""
		if sport == "All":
			sport = ["Trail Running", "Street Running", "Road Cycling", "Mountain Biking",
						"Open Water Swimming", "Pool Swimming"]
		elif sport == "Cyclisme":
			sport = ["Road Cycling", "Mountain Biking"]
		elif sport == "Running":
			sport = ["Street Running", "Trail Running"]
		elif sport == "Renfo":
			print("Données de distances indisponibles en renforcement musculaire.")
			sys.exit(1)
		elif sport == "Natation":
			sport = ["Open Water Swimming", "Pool Swimming"]

		list_distances = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:

				month_row = row["Start Time"][:7]
				sport_row = row["Activity Type"]
				distance_row = row["Distance (km)"]

				for i in sport:
					if i == sport_row:

						if month == "All":
							list_distances.append(distance_row)

						elif month_row == month:
							list_distances.append(distance_row)

		# Conversion items de la liste string vers float
		float_list_distance = list(map(float, list_distances))
		return float_list_distance

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

	print(activities.get_list_heart_rate(month="2020-11", sport="Renfo"))
	print(activities.get_number_activities(month="2020-11", sport="Cyclisme"))
	print(activities.get_list_distances(month="2020-10", sport="Cyclisme"))