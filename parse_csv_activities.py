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
	Parser les informations d'un fichier activities.csv et proposer
	des données brutes et propres pour les autres classes
	"""

	def __init__(self, activities_file):
		self._activities_file = activities_file
		self._sports = ["Trail Running", "Street Running", "Road Cycling", "Mountain Biking",
						"Open Water Swimming", "Pool Swimming", "Strength Training"]
		self.verify_csv()

	def verify_csv(self):
		"""
		Vérifier que le fichier csv est de qualité :
		- les types d'activités ne doivent pas être génériques (cela permet d'affiner les stats)
		- les types d'activités doivent être connus
		"""

		good_names_activities = self._sports
		bad_activities_types = ['Swimming', 'Running', 'Cycling']

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
			
				activity_type = row["Activity Type"]
				activity_date = row["Start Time"][:10]

				if activity_type in bad_activities_types:
					print("le type d'activité  {} daté du {} n'est pas accepté.".format(activity_type, activity_date))
					print("Les types d'activités acceptés sont : {}.".format(str(good_names_activities)))
					print("Arrêt du programme.")
					sys.exit(1)
				
				if activity_type not in good_names_activities:
					print("Le type d'activité {} daté du {} dans le fichier csv qui n'est pas reconnu.".format(activity_type, activity_date))
					print("Arrêt du programme.")
					sys.exit(1)

	def get_list_average_heart_rate(self, month, sport):
		"""
		Retourner une liste comprenant tous les integers des moyennes
		de fréquence cardiaque pour un mois choisi, et pour un sport choisi,
		ou pour tous les temps pour tous les sports

		month accepte :
			- "All"
			- "YYYY-MM"

		Exemples : 
		get_list_heart_rate(month="All", sport="All")
		get_list_heart_rate(month="2020-07", sport="Running")
		"""

		sport = self.sport_list(sport=sport, sport_type="heart_rate")
		
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

	def get_max_heart_rate(self, month, sport):
		"""Connaitre la fréquence cardiaque maximale atteinte"""

		sport = self.sport_list(sport=sport, sport_type="heart_rate")
		
		max_heart_rate = 0

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:

				max_heart_rate_row = row["Max. Heart Rate (bpm)"]
				month_row = row["Start Time"][:7]
				sport_row = row["Activity Type"]

				for i in sport:
					if i == sport_row:

						if month == "All":
							if max_heart_rate_row: # Ajouter uniquement les string non vides
								if int(max_heart_rate_row) > max_heart_rate:
									max_heart_rate = int(max_heart_rate_row)

						elif month_row == month:
							if max_heart_rate_row: # Ajouter uniquement les string non vides
								if int(max_heart_rate_row) > max_heart_rate:
									max_heart_rate = int(max_heart_rate_row)
		return max_heart_rate
		
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

		sport = self.sport_list(sport=sport)

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
		"""Récupérer une liste comprenant les distances des activités"""
		
		sport = self.sport_list(sport=sport, sport_type="speed_distance")

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

	def get_speed_list(self, month, sport):
		"""Récupérer une liste comprenant les vitesses des activités"""

		sport = self.sport_list(sport=sport, sport_type="speed_distance")

		speed_list = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:

				month_row = row["Start Time"][:7]
				sport_row = row["Activity Type"]
				speed_row = row["Average Speed (km/h)"]

				for i in sport:
					if i == sport_row:

						if month == "All":
							speed_list.append(speed_row)

						elif month_row == month:
							speed_list.append(speed_row)

		# Conversion items de la liste string vers float
		float_speed_list = list(map(float, speed_list))
		return float_speed_list

	def get_duration_list(self, month, sport):
		"""Récupérer une liste comprenant le temps des activités"""

		sport = self.sport_list(sport=sport)

		duration_list = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:

				month_row = row["Start Time"][:7]
				sport_row = row["Activity Type"]

				duration_row = row["Duration (h:m:s)"]

				for i in sport:
					if i == sport_row:

						if month == "All":
							duration_list.append(duration_row)

						elif month_row == month:
							duration_list.append(duration_row)

		return duration_list

	def sport_list(self, sport, sport_type=None):
		"""
		Connaître la liste des sports en fonction des activités :
		- supprimer la natation pour les activités demandant une FC
		- supprimer le renfo pour les activités demandant une distance/vitesse
		"""

		accepted_sports = ["All", "Cyclisme", "Running", "Natation", "Renfo"]
		
		if sport not in accepted_sports:
			print("Le sport {} n'est pas reconnu.".format(sport))
			print("Les sports acceptés sont : {}.".format(str(accepted_sports)))
			print("Arrêt du programme.")
			sys.exit(1)

		not_heart_rate_sports = ["Open Water Swimming", "Pool Swimming"]
		not_speed_distance_sports = ["Strength Training"]

		if sport == "All":
			sports = self._sports
		elif sport == "Cyclisme":
			sports = ["Road Cycling", "Mountain Biking"]
		elif sport == "Running":
			sports = ["Street Running", "Trail Running"]
		elif sport == "Renfo":
			sports = ["Strength Training"]
		elif sport == "Natation":
			sports = ["Open Water Swimming", "Pool Swimming"]
		
		if sport_type == "heart_rate":
			for item in not_heart_rate_sports:
				if item in sports:
					sports.remove(item)

		elif sport_type == "speed_distance":
			for item in not_speed_distance_sports:
				if item in sports:
					sports.remove(item)

		return sports

	"""Getters and setters"""

	def _get_activities_file(self):
		return self._activities_file

	def _set_activities_file(self, activities_file):
		self._activities_file = activities_file

	activities_file = property(_get_activities_file, _set_activities_file)

	def _get_sports(self):
		return self._sports

	def _set_sports(self, sports):
		self._sports = sports

	sports = property(_get_sports, _set_sports)

if __name__ == "__main__":

	activities = Parse_csv_activities("activities/activities.csv")

	print(activities.get_list_distances(month="2020-09", sport="Cyclisme"))