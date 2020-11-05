#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.2"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"


import sys
from statistics import mean
from datetime import timedelta

from parse_csv_activities import Parse_csv_activities

class Make_statistics:
    """
    Classe effectuant des statistiques à partir des données remontées par la
    lecture du fichier CSV dans parse_csv_activities.py
    """

    def __init__(self, activities_file):
        self._activities_file = activities_file
        self._activities = Parse_csv_activities(activities_file)

    def average_heart_rate(self, date, sport):
        """
        Calcul de la moyenne du rythme cardiaque
        """

        list_hr = self._activities.get_average_heart_rate_list(date=date,
                                                               sport=sport)

        if len(list_hr) == 0:
            average_heart_rate = "Aucune donnée"

        else:
            # Conversion des str en int
            list_hr = list(map(int, list_hr))
            # Calcul moyenne
            average_heart_rate = mean(list_hr)
            average_heart_rate = round(average_heart_rate)

        return average_heart_rate

    def average_max_heart_rate(self, date, sport):
        """
        Calcul de la moyenne du rythme cardiaque maximale enregistré
        pendant les activités
        """

        list_max_hr = self._activities.get_max_heart_rate_list(date=date,
                                                               sport=sport)

        # Conversion des str en int
        list_max_hr = list(map(int, list_max_hr))
        # Calcul moyenne
        average_max_heart_rate = mean(list_max_hr)

        return average_max_heart_rate
    
    def max_heart_rate(self, date, sport):
        """
        Calcul du rythme cardiaque maximal enregistré
        """

        list_max_hr = self._activities.get_max_heart_rate_list(date=date,
                                                               sport=sport)
        
        # Conversion des str en int
        list_max_hr = list(map(int, list_max_hr))
        # Calcul de la valeur maximale dans la liste
        max_heart_rate = max(list_max_hr)

        return max_heart_rate
    
    def number_activities_per_day(self, date, sport):
        """Calculer le nombre de jours dans un mois"""
        # TODO : gérer les années bissextiles

        type_date = self._activities.verify_date(date=date)
        
        # Gérer le fait que la fonction ne retourne pas de liste
        # si on cherche "all-time"
        if type_date != "all-time":
            type_date = self._activities.verify_date(date=date)[0]
        
        number_days_month =	{
            "01": 31,
            "02": 29,
            "03": 31,
            "04": 30,
            "05": 31,
            "06": 30,
            "07": 31,
            "08": 31,
            "09": 30,
            "10": 31,
            "11": 30,
            "12": 31
        }

        if type_date == "all-time":
            print("Il n'est pas encore possible de calculer le ratio pour " \
                  "la période 'all-time'.")
            sys.exit(1)
        elif type_date == "year":
            days = 365
        elif type_date == "month":
            month = date[5:]
            days = number_days_month[month]
        
        number_activities = self._activities.get_number_activities(date=date, sport=sport)
        activities_per_day = number_activities / days
        activities_per_day = round(activities_per_day, 2)
        
        return activities_per_day
    
    def total_distance(self, date, sport):
        """Calcul du total de distance"""

        total_distance = 0
        list_distances = self._activities.get_distances_list(date=date, sport=sport)
        
        for i in list_distances:
            total_distance += i

        total_distance = round(total_distance, 2)
        return total_distance

    def average_speed(self, date, sport):
        """Calcul de la vitesse moyenne en km/h"""

        list_speed = self._activities.get_speed_list(date=date, sport=sport)
        average_speed = round(mean(list_speed), 2)

        return average_speed
    
    def activities_duration(self, date, sport):
        """Calculer des sommes de temps d'activités"""

        total_duration = timedelta(hours=0, minutes=0, seconds=0)
        list_duration = self._activities.get_duration_list(date=date, sport=sport)

        for duration in list_duration:
            hours = int(duration[:2])
            minutes = int(duration[3:5])
            seconds = int(duration[6:8])

            total_duration += timedelta(hours=hours, minutes=minutes, seconds=seconds)
        
        return total_duration
    
if __name__ == "__main__":

	stats = Make_statistics("activities/activities.csv")

	print(stats.activities_duration(date="2020", sport="running"))
