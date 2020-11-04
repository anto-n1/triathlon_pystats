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

    def __init__(self, activities_file="activities/activities.csv"):
        self._activities_file = activities_file
        self._activities = Parse_csv_activities(self._activities_file)
        self._stats = Make_statistics(self._activities_file)
        if not os.path.exists("images/graphs"):
            os.mkdir("images/graphs")

    def activities_sharing(self, month):
        """
        Générer un graphique camembert sur la répartition générale
        des sports
        
        Générer un mois :
        graphs.activities_sharing(month="2020-10")
        
        Générer toutes les activitités :
        graphs.activities_sharing(month="All")
        """

        sports = ["Cyclisme", "Running", "Natation", "Renfo"]

        sizes = [ self._activities.get_number_activities(month=month, sport="Cyclisme"), 
                    self._activities.get_number_activities(month=month, sport="Running"),
                    self._activities.get_number_activities(month=month, sport="Natation"),
                    self._activities.get_number_activities(month=month, sport="Renfo") ]
        
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

        plt.pie(sizes, labels=sports, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')

        #plt.show()
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
        #plt.show()
        plt.savefig("images/graphs/repartition_distance.png")


if __name__ == "__main__":

	graphs = Create_graphics(activities_file="activities/activities.csv")

	graphs.sharing_distance(month="2020-11")