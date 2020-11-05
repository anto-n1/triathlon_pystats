#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

import os
import matplotlib.pyplot as plt
from datetime import timedelta

from parse_csv_activities import Parse_csv_activities
from make_statistics import Make_statistics

class Create_graphics:
    """
    Générer des graphiques
    """

    def __init__(self, activities_file):
        self._activities_file = activities_file
        self._activities = Parse_csv_activities(self._activities_file)
        self._stats = Make_statistics(self._activities_file)
        if not os.path.exists("images/graphs"):
            os.mkdir("images/graphs")

    def activities_sharing(self, date):
        """
        Générer un graphique camembert sur la répartition générale des sports
        par rapport au nombre d'activités
        """

        sports = [ "Cyclisme", "Running", "Natation", "Renfo" ]

        nb_cycling = self._activities.get_number_activities(date=date,
                                                            sport="cyclisme")
        nb_running = self._activities.get_number_activities(date=date,
                                                            sport="running")
        nb_natation = self._activities.get_number_activities(date=date,
                                                             sport="natation")
        nb_renfo = self._activities.get_number_activities(date=date,
                                                          sport="renfo")
        
        sizes = [ nb_cycling, nb_running, nb_natation, nb_renfo ]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

        # Ne pas afficher les valeurs à 0
        if nb_cycling == 0:
            sports.remove("Cyclisme")
            sizes.remove(nb_cycling)
            colors.remove(colors[1])

        if nb_running == 0:
            sports.remove("Running")
            sizes.remove(nb_running)
            colors.remove(colors[1])

        if nb_natation == 0:
            sports.remove("Natation")
            sizes.remove(nb_natation)
            colors.remove(colors[1])

        if nb_renfo == 0:
            sports.remove("Renfo")
            sizes.remove(nb_renfo)
            colors.remove(colors[1])

        plt.pie(sizes,
                colors=colors,
                labels=sports,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85)
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis('equal')  
        plt.tight_layout()
        #plt.show()
        plt.savefig("images/graphs/repartition_nombre_activites.png")

    
    def distance_sharing(self, date):
        """
        Générer un graphique camembert sur la répartition générale des sports
        par rapport à la distance parcourue
        """
        
        sports = [ "Cyclisme", "Running", "Natation" ]

        distance_cycling = self._stats.total_distance(date=date,
                                                      sport="cyclisme")
        distance_running = self._stats.total_distance(date=date,
                                                      sport="running")
        distance_natation = self._stats.total_distance(date=date,
                                                       sport="natation")
        
        sizes = [ distance_cycling, distance_running, distance_natation ]
        colors = ['#ff9999','#66b3ff','#99ff99']

        # Ne pas afficher les valeurs à 0
        if distance_cycling == 0:
            sports.remove("Cyclisme")
            sizes.remove(distance_cycling)
            colors.remove(colors[1])

        if distance_running == 0:
            sports.remove("Running")
            sizes.remove(distance_running)
            colors.remove(colors[1])

        if distance_natation == 0:
            sports.remove("Natation")
            sizes.remove(distance_natation)
            colors.remove(colors[1])

        plt.pie(sizes,
                colors=colors,
                labels=sports,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85)

        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis('equal')  
        plt.tight_layout()
        #plt.show()
        plt.savefig("images/graphs/repartition_distance.png")

    def time_sharing(self, date):
        """
        Générer un graphique camembert sur la répartition générale des sports
        par rapport au temps passé pour chaque sport
        """
        sports = [ "Cyclisme", "Running", "Natation", "Renfo" ]

        time_cycling = self._stats.activities_duration(date=date,
                                                       sport="cyclisme")
        time_running = self._stats.activities_duration(date=date,
                                                       sport="running")
        time_natation = self._stats.activities_duration(date=date,
                                                        sport="natation")
        time_renfo = self._stats.activities_duration(date=date,
                                                     sport="renfo")

        time_cycling = time_cycling.total_seconds()
        time_natation = time_natation.total_seconds()
        time_renfo = time_renfo.total_seconds()
        time_running = time_running.total_seconds()

        sizes = [ time_cycling, time_running, time_natation, time_renfo ]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        
        # Ne pas afficher les valeurs à 0
        if time_cycling == 0:
            sports.remove("Cyclisme")
            sizes.remove(time_cycling)
            colors.remove(colors[1])

        if time_running == 0:
            sports.remove("Running")
            sizes.remove(time_running)
            colors.remove(colors[1])

        if time_natation == 0:
            sports.remove("Natation")
            sizes.remove(time_natation)
            colors.remove(colors[1])

        if time_renfo == 0:
            sports.remove("Renfo")
            sizes.remove(time_renfo)
            colors.remove(colors[1])

        plt.pie(sizes,
                colors=colors,
                labels=sports,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85)

        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis('equal')  
        plt.tight_layout()
        #plt.show()
        plt.savefig("images/graphs/repartition_temps.png", dpi=800)

if __name__ == "__main__":

	graphs = Create_graphics(activities_file="activities/activities.csv")

	graphs.time_sharing(date="2020-11")