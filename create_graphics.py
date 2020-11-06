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

        filename = "images/graphs/repartition_nombre_activites.png"
        if os.path.exists(filename):
            os.remove(filename)


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
            colors.remove(colors[0])

        if nb_running == 0:
            sports.remove("Running")
            sizes.remove(nb_running)
            colors.remove(colors[0])

        if nb_natation == 0:
            sports.remove("Natation")
            sizes.remove(nb_natation)
            colors.remove(colors[0])

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
        plt.savefig(filename, dpi=800, bbox_inches='tight')
        plt.close()
    
    def distance_sharing(self, date):
        """
        Générer un graphique camembert sur la répartition générale des sports
        par rapport à la distance parcourue
        """

        filename = "images/graphs/repartition_distance.png"
        if os.path.exists(filename):
            os.remove(filename)

        distance_cycling = self._stats.total_distance(date=date,
                                                      sport="cyclisme")
        distance_running = self._stats.total_distance(date=date,
                                                      sport="running")
        distance_natation = self._stats.total_distance(date=date,
                                                       sport="natation")

        sports = [ "Cyclisme ({} km)".format(distance_cycling),
                   "Running ({} km)".format(distance_running),
                   "Natation ({} km)".format(distance_natation) ]

        sizes = [ distance_cycling, distance_running, distance_natation ]

        colors = ['#ff9999','#66b3ff','#99ff99']

        # Ne pas afficher les valeurs à 0
        if distance_cycling == 0:
            sports.remove("Cyclisme ({} km)".format(distance_cycling))
            sizes.remove(distance_cycling)
            colors.remove(colors[0])

        if distance_running == 0:
            sports.remove("Running ({} km)".format(distance_running))
            sizes.remove(distance_running)
            colors.remove(colors[0])

        if distance_natation == 0:
            sports.remove("Natation ({} km)".format(distance_natation))
            sizes.remove(distance_natation)
            colors.remove(colors[0])

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
        plt.savefig(filename, dpi=800, bbox_inches='tight')
        plt.close()

    def time_sharing(self, date):
        """
        Générer un graphique camembert sur la répartition générale des sports
        par rapport au temps passé pour chaque sport
        """

        filename = "images/graphs/repartition_temps.png"
        if os.path.exists(filename):
            os.remove(filename)

        time_cycling = self._stats.activities_duration(date=date,
                                                       sport="cyclisme")
        time_running = self._stats.activities_duration(date=date,
                                                       sport="running")
        time_natation = self._stats.activities_duration(date=date,
                                                        sport="natation")
        time_renfo = self._stats.activities_duration(date=date,
                                                     sport="renfo")

        sports = [ "Cyclisme ({})".format(time_cycling),
                   "Running ({})".format(time_running),
                   "Natation ({})".format(time_natation),
                   "Renfo ({})".format(time_renfo) ]

        time_cycling_seconds = time_cycling.total_seconds()
        time_natation_seconds = time_natation.total_seconds()
        time_renfo_seconds = time_renfo.total_seconds()
        time_running_seconds = time_running.total_seconds()

        sizes = [ time_cycling_seconds,
                  time_running_seconds,
                  time_natation_seconds,
                  time_renfo_seconds ]

        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        
        # Ne pas afficher les valeurs à 0
        if time_cycling_seconds == 0:
            sports.remove("Cyclisme ({})".format(time_cycling))
            sizes.remove(time_cycling_seconds)
            colors.remove(colors[0])

        if time_running_seconds == 0:
            sports.remove("Running ({})".format(time_running))
            sizes.remove(time_running_seconds)
            colors.remove(colors[0])

        if time_natation_seconds == 0:
            sports.remove("Natation ({})".format(time_natation))
            sizes.remove(time_natation_seconds)
            colors.remove(colors[0])

        if time_renfo_seconds == 0:
            sports.remove("Renfo ({})".format(time_renfo))
            sizes.remove(time_renfo_seconds)
            colors.remove(colors[0])

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
        plt.savefig(filename, dpi=800, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":

	graphs = Create_graphics(activities_file="activities/activities.csv")

	graphs.distance_sharing(date="2020-01")
