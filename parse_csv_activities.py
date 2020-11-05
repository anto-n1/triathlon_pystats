#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.2"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

from datetime import timedelta
import csv
import sys

class Parse_csv_activities:
	"""
	Parser les informations d'un fichier activities.csv et proposer
	des données brutes pour les autres classes
	"""

	def __init__(self, activities_file):
		self._activities_file = activities_file
		self._sports = [
			"Trail Running", "Street Running",
			"Road Cycling","Mountain Biking",
			"Open Water Swimming", "Pool Swimming",
			"Strength Training"
			]
		self.verify_csv()

	def verify_csv(self):
		"""
		Vérifier que le fichier csv est de qualité.
		Les vérifications faites sont :
		- types d'activités non génériques (affinage des stats)
		- types d'activités connus (bon fonctionnement du programme)
		"""

		good_activities_names = self._sports
		bad_activities_types = ['Swimming', 'Running', 'Cycling']

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
			
				activity_type = row["Activity Type"]
				activity_date = row["Start Time"][:10]

				if activity_type in bad_activities_types:
					print("le type d'activité  {} daté du {} n'est pas accepté.".format(activity_type, activity_date))
					print("Les types d'activités acceptés sont : {}.".format(str(good_activities_names)))
					sys.exit(1)
				
				if activity_type not in good_activities_names:
					print("Le type d'activité {} daté du {} dans le fichier csv qui n'est pas reconnu.".format(activity_type, activity_date))

					sys.exit(1)

	def get_average_heart_rate_list(self, date, sport):
		"""
		Retourner une liste comprenant des fréquences cardiaques moyennes
		"""

		# Vérification date conforme et récupération type
		complete_date = self.verify_date(date=date)

		# Connaître la liste des sports
		sport = self.sport_list(sport=sport, sport_type="heart_rate")

		average_heart_rate_list = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:

				date_row = row["Start Time"][:complete_date[2]]
				sport_row = row["Activity Type"]
				average_heart_rate_row = row["Average Heart Rate (bpm)"]

				# Si string vide, on passe
				if not average_heart_rate_row:
					continue

				# Si tous les temps, alors on ajoute automatiquement
				if date == "all-time":
					average_heart_rate_list.append(average_heart_rate_row)

				# Sinon si c'est le sport souhaité et la bonne date
				elif sport_row in sport and date_row == complete_date[1]:
					average_heart_rate_list.append(average_heart_rate_row)

		return average_heart_rate_list

	def get_max_heart_rate_list(self, date, sport):
		"""
		Récupérer une liste des fréquences cardiaques maximales atteintes
		"""

		# Vérification date conforme et récupération type
		complete_date = self.verify_date(date=date)

		# Connaître la liste des sports
		sport = self.sport_list(sport=sport, sport_type="heart_rate")

		max_heart_rate_list = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:

				date_row = row["Start Time"][:complete_date[2]]
				sport_row = row["Activity Type"]
				max_heart_rate_row = row["Max. Heart Rate (bpm)"]

				# Si string vide, on passe
				if not max_heart_rate_row:
					continue

				# Si tous les temps, alors on ajoute automatiquement
				if date == "all-time":
					max_heart_rate_list.append(max_heart_rate_row)

				# Sinon si c'est le sport souhaité et la bonne date
				elif sport_row in sport and date_row == complete_date[1]:
					max_heart_rate_list.append(max_heart_rate_row)

		return max_heart_rate_list

	def get_number_activities(self, date, sport):
		"""Compter le nombre d'activités"""

		# Vérification date conforme et récupération type
		complete_date = self.verify_date(date=date)

		# Connaître la liste des sports
		sport = self.sport_list(sport=sport)

		number_activities = 0

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:

				date_row = row["Start Time"][:complete_date[2]]
				sport_row = row["Activity Type"]

				# Si tous les temps, alors on ajoute automatiquement
				if date == "all-time":
					number_activities += 1

				# Sinon si c'est le sport souhaité et la bonne date
				elif sport_row in sport and date_row == complete_date[1]:
					number_activities += 1
		
		return number_activities

	def get_distances_list(self, date, sport):
		"""Récupérer une liste comprenant les distances des activités"""

		# Vérification date conforme et récupération type
		complete_date = self.verify_date(date=date)

		# Connaître la liste des sports
		sport = self.sport_list(sport=sport, sport_type="speed_distance")

		distances_list = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:

				date_row = row["Start Time"][:complete_date[2]]
				sport_row = row["Activity Type"]
				distance_row = row["Distance (km)"]

				# Si string vide, on passe
				if not distance_row:
					continue

				# Conversion en float avec 2 chiffres après virgule
				distance_row = float(distance_row)
				distance_row = round(distance_row, 2)

				# Si tous les temps, alors on ajoute automatiquement
				if date == "all-time":
					distances_list.append(distance_row)

				# Sinon si c'est le sport souhaité et la bonne date
				elif sport_row in sport and date_row == complete_date[1]:
					distances_list.append(distance_row)

		return distances_list

	def get_speed_list(self, date, sport):
		"""Récupérer une liste comprenant les vitesses des activités"""

		# Vérification date conforme et récupération type
		complete_date = self.verify_date(date=date)

		# Connaître la liste des sports
		sport = self.sport_list(sport=sport, sport_type="speed_distance")

		speed_list = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:

				date_row = row["Start Time"][:complete_date[2]]
				sport_row = row["Activity Type"]
				speed_row = row["Average Speed (km/h)"]

				# Si string vide, on passe
				if not speed_row:
					continue

				# Conversion en float avec 2 chiffres après virgule
				speed_row = float(speed_row)
				speed_row = round(speed_row, 2)

				# Si tous les temps, alors on ajoute automatiquement
				if date == "all-time":
					speed_list.append(speed_row)

				# Sinon si c'est le sport souhaité et la bonne date
				elif sport_row in sport and date_row == complete_date[1]:
					speed_list.append(speed_row)

		return speed_list

	def get_duration_list(self, date, sport):
		"""Récupérer une liste comprenant le temps des activités"""

		# Vérification date conforme et récupération type
		complete_date = self.verify_date(date=date)

		# Connaître la liste des sports
		sport = self.sport_list(sport=sport)

		duration_list = []

		with open(self._activities_file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:

				date_row = row["Start Time"][:complete_date[2]]
				sport_row = row["Activity Type"]
				duration_row = row["Duration (h:m:s)"]

				# Si tous les temps, alors on ajoute automatiquement
				if complete_date == "all-time":
					duration_list.append(duration_row)

				# Sinon si c'est le sport souhaité et la bonne date
				elif sport_row in sport and date_row == complete_date[1]:
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
			print("Les sports acceptés sont : {}.".format(accepted_sports))
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

	def verify_date(self, date):
		"""
		Vérifier la date données, et déduire si cette date est une année,
		un mois ou un jour.

		Retourne une liste contenant le type de date et la date
		"""

		if len(date) == 4:
			# date = ["type", date, ""
			date = ["year", date, 4]

		elif len(date) == 7:
			# Mois
			date = ["month", date, 7]

		elif len(date) == 10:
			# Jour
			date = ["day", date, 10]

		elif date == "all-time":
			# Tous les temps
			date = "all-time"

		else:
			valid_dates = ["YYYY-MM-JJ", "YYYY-MM", "YYYY", "all-time"]

			print("La date {} n'est pas reconnu.".format(date))
			print("Les formats de date connus sont : {}.".format(valid_dates))
			sys.exit(1)
		
		return date

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

	print(activities.get_speed_list(date="2020-10", sport="Cyclime"))