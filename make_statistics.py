#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

from statistics import mean
from parse_csv_activities import Parse_csv_activities

class Make_statistics:
    """
    Classe effectuant des statistiques à partir des données
    brutes remontées par la lecture du fichier CSV dans parse_csv_activities.py
    """

    def __init__(self, activities_file):
        self._activities_file = activities_file
        self._activities = Parse_csv_activities(activities_file)

    def average_heart_rate_all_time(self, month, sport):
        """Calcul de la moyenne du rythme cardiaque"""

        average_heart_rate = mean(self._activities.get_list_heart_rate(month=month, sport=sport))
        rouded_average_heart_rate = round(average_heart_rate) # Pas de virgule

        return rouded_average_heart_rate
    
if __name__ == "__main__":

	activities = Make_statistics("activities/activities.csv")

	print(activities.average_heart_rate_all_time(month="2020-10", sport="All"))