#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

from statistics import mean
from datetime import timedelta
from parse_csv_activities import Parse_csv_activities

class Make_statistics:
    """
    Classe effectuant des statistiques à partir des données
    brutes remontées par la lecture du fichier CSV dans parse_csv_activities.py
    """

    def __init__(self, activities_file):
        self._activities_file = activities_file
        self._activities = Parse_csv_activities(activities_file)

    def average_heart_rate(self, month, sport):
        """Calcul de la moyenne du rythme cardiaque"""

        average_heart_rate = mean(self._activities.get_list_average_heart_rate(month=month, sport=sport))
        rouded_average_heart_rate = round(average_heart_rate) # Pas de virgule

        return rouded_average_heart_rate
    
    def number_activities_per_day(self, month, sport):
        """Calculer le nombre de jours dans un mois"""

        days_dict =	{
            "2020-01": 31,
            "2020-02": 29,
            "2020-03": 31,
            "2020-04": 30,
            "2020-05": 31,
            "2020-06": 30,
            "2020-07": 31,
            "2020-08": 31,
            "2020-09": 30,
            "2020-10": 31,
            "2020-11": 30,
            "2020-12": 31
        }

        days = days_dict[month]
        number_activities = self._activities.get_number_activities(month=month, sport=sport)
        
        activities_per_day = number_activities / days

        rounded_activities_per_day = round(activities_per_day, 2)
        
        return rounded_activities_per_day
    
    def total_distance(self, month, sport):
        """Calcul du total de distance"""

        total_distance = 0
        list_distances = self._activities.get_list_distances(month=month, sport=sport)
        
        for i in list_distances:
            total_distance += i

        rounded_total_distance = round(total_distance, 2)
        return rounded_total_distance

    def average_speed(self, month, sport):
        """Calcul de la vitesse moyenne en km/h"""

        list_speed = self._activities.get_list_speed(month=month, sport=sport)
        average_speed = round(mean(list_speed), 2)

        return average_speed
    
    def activities_duration(self, month, sport):
        """Calculer des sommes de temps d'activités"""

        total_duration = timedelta(hours=0, minutes=0, seconds=0)
        list_duration = self._activities.get_duration_list(month=month, sport=sport)

        for duration in list_duration:
            hours = int(duration[:2])
            minutes = int(duration[3:5])
            seconds = int(duration[6:8])

            total_duration += timedelta(hours=hours, minutes=minutes, seconds=seconds)
        
        return total_duration
    
if __name__ == "__main__":

	activities = Make_statistics("activities/activities.csv")

	print(activities.total_distance(month="2020-09", sport="All"))