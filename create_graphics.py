#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

import os
import matplotlib.pyplot as plt

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
        """

        sports = ["Cyclisme", "Running", "Natation", "Renfo"]

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
        #explode = (0.05 ,0.05 ,0.05 ,0.05)

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

        #https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f

        plt.pie(sizes, colors = colors, labels=sports, autopct='%1.1f%%', startangle=90, pctdistance=0.85)#draw circle
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)# Equal aspect ratio ensures that pie is drawn as a circle
        plt.axis('equal')  
        plt.tight_layout()
        plt.show()
        plt.savefig("images/graphs/repartition_temps.png")

    
    def sharing_distance(self, month):
        """Générer un diagramme camember sur la répartition des distances"""

        sports = ["Cyclisme", "Running", "Natation"]

        sizes = [ self._stats.total_distance(month=month, sport="Cyclisme"), 
                    self._stats.total_distance(month=month, sport="Running"),
                    self._stats.total_distance(month=month, sport="Natation")]

        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

        plt.pie(sizes, labels=sports, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')
        plt.show()
        #plt.savefig("images/graphs/repartition_distance.png")


if __name__ == "__main__":

	graphs = Create_graphics(activities_file="activities/activities.csv")

	graphs.activities_sharing(date="2020-11")