#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

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
        explode = (0, 0.1, 0, 0)

        plt.pie(sizes, explode=explode, labels=sports, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')

        plt.savefig("images/graphs/repartition_activites.png")
        #plt.show()
        
    def activities_sharing_year(self, year):
        """Générer un graphique camembert sur la répartition générale
        des sports sur un mois choisi"""
        pass


if __name__ == "__main__":

	graphs = Create_graphics(activities_file="activities/activities.csv")

	graphs.activities_sharing(month="All")