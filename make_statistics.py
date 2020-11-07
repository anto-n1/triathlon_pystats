#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__version = "0.2"
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

        if len(list_max_hr) == 0:
            average_max_heart_rate = "Aucune donnée."

        else:
            # Conversion des str en int
            list_max_hr = list(map(int, list_max_hr))
            # Calcul moyenne
            average_max_heart_rate = mean(list_max_hr)

        return average_max_heart_rate
    
    def max_heart_rate(self, date, sport):
        """Calcul du rythme cardiaque maximal enregistré"""

        list_max_hr = self._activities.get_max_heart_rate_list(date=date,
                                                               sport=sport)

        if len(list_max_hr) == 0:
            max_heart_rate = "Aucune donnée."
        
        else:
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
            
            days_list = self._activities.get_date_activities_list(
                date=date,
                sport=sport
            )

            max_year = max(days_list[:4])
            max_month = max(days_list[5:7])
            max_day = max(days_list[8:10])

            for day in days_list:
                min_year = 
            
            

            #days = len(days_list)

        elif type_date == "year":
            days = 365
        
        elif type_date == "month":
            month = date[5:]
            days = number_days_month[month]
        
        elif type_date == "day":
            days = 1
        
        number_activities = self._activities.get_number_activities(
            date=date,
            sport=sport)

        activities_per_day = number_activities / days
        activities_per_day = round(activities_per_day, 2)
        
        return activities_per_day


    def total_distance(self, date, sport):
        """Calcul du total de distance"""

        total_distance = 0
        list_distances = self._activities.get_distances_list(date=date,
                                                             sport=sport)
        
        for i in list_distances:
            total_distance += i

        total_distance = round(total_distance, 2)
        return total_distance


    def average_speed(self, date, sport):
        """Calcul de la vitesse moyenne en km/h"""

        list_speed = self._activities.get_speed_list(date=date, sport=sport)

        if len(list_speed) == 0:
            average_speed = "Aucune donnée"

        else:
            average_speed = round(mean(list_speed), 2)

        return average_speed
    

    def average_vo2max(self, date, sport):
        """Calcul de la VO2max moyenne"""

        list_vo2max = self._activities.get_vo2max_list(date=date, sport=sport)

        if len(list_vo2max) == 0:
            average_vo2max = "Aucune donnée"

        else:
            list_vo2max = list(map(float, list_vo2max))
            average_vo2max = round(mean(list_vo2max), 1)

        return average_vo2max
    

    def max_vo2max(self, date, sport):
        """Calcul de la vo2max maximale enregistré"""

        list_vo2max = self._activities.get_vo2max_list(date=date, sport=sport)

        if len(list_vo2max) == 0:
            max_vo2max = "Aucune donnée."
        
        else:
            # Calcul de la valeur maximale dans la liste
            max_vo2max = max(list_vo2max)

        return max_vo2max
    

    def max_elevation(self, date, sport):
        """Calcul du dénivelé maximal enregistré"""

        list_elevation = self._activities.get_elevation_list(date=date,
                                                             sport=sport)

        if len(list_elevation) == 0:
            max_elevation = "Aucune donnée."
        
        else:
            # Calcul de la valeur maximale dans la liste
            max_elevation = max(list_elevation)

        return max_elevation


    def total_elevation(self, date, sport):
        """Calcul du dénivelé total enregistré"""

        list_elevation = self._activities.get_elevation_list(date=date,
                                                             sport=sport)

        total_elevation = 0

        if len(list_elevation) == 0:
            total_elevation = "Aucune donnée"

        else:
            list_elevation = list(map(float, list_elevation))
            for item in list_elevation:
                total_elevation += item
        
            total_elevation = round(total_elevation)
            
        return total_elevation
    

    def activities_duration(self, date, sport):
        """Calculer des sommes de temps d'activités"""

        total_duration = timedelta(hours=0, minutes=0, seconds=0)
        list_duration = self._activities.get_duration_list(date=date,
                                                           sport=sport)

        for duration in list_duration:
            hours = int(duration[:2])
            minutes = int(duration[3:5])
            seconds = int(duration[6:8])

            total_duration += timedelta(hours=hours,
                                        minutes=minutes,
                                        seconds=seconds)
        
        return total_duration


    def activities_location(self, date, sport):
        """
        Calculer le nombre d'activités effectuées dans différents lieux
        Retourne un dictionnaire
        """

        location_list = self._activities.get_location_list(date=date,
                                                           sport=sport)

        location_1 = "La Haie-Fouassière"
        location_2 = "Angers"
        location_3 = "Cholet"
        location_4 = "Autre"

        location_dict = {
            location_1 : 0,
            location_2 : 0,
            location_3 : 0,
            location_4 : 0
        }

        for location in location_list:

            if location == location_1:
                location_dict[location_1] += 1
            
            elif location == location_2:
                location_dict[location_2] += 1

            elif location == location_3:
                location_dict[location_3] += 1
        
            else:
                location_dict[location_4] += 1

        return location_dict

if __name__ == "__main__":

	stats = Make_statistics("activities/activities.csv")

	print(stats.number_activities_per_day(date="all-time", sport="all"))
