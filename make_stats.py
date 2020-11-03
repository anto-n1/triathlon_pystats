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

    def __init__(self, activities_file):
        self._activities_file = activities_file
        self._activities = Parse_csv_activities(activities_file)

    def average_heart_rate_all_time(self):
        """Calcul de la moyenne du rythme cardiaque toute activités
        et tout temps confondu"""

        average_heart_rate = mean(self._activities.get_list_heart_rate())
        rouded_average_heart_rate = round(average_heart_rate) # Pas de virgule
        return rouded_average_heart_rate
    
if __name__ == "__main__":

	activities = Make_statistics("activities/activities.csv")

	print(activities.average_heart_rate_all_time())