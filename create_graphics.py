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

class Create_graph:
    """
    Générer des graphiques
    """

    def __init__(self, activities_file="activities/activities.csv"):
        self._activities_file = activities_file
        self._activities = Parse_csv_activities(self._activities_file)
        self._stats = Make_statistics(self._activities_file)

    def activities_sharing_all_time(self):
        """Générer un graphique camembert sur la répartition générale
        des sports"""

        sports = ["Running", "Vélo", "Natation", "Renfo"]

        sizes = [ self._activities.number_running_activities(), self._activities.number_cycling_activities(),
            self._activities.number_swimming_activities(), self._activities.number_strength_training_activities() ]
        
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        explode = (0, 0.1, 0, 0)

        plt.pie(sizes, explode=explode, labels=sports, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')

        plt.savefig('PieChart02.png')
        plt.show()
        
    def activities_sharing_one_month(self, month="2020-11"):
        """Générer un graphique camembert sur la répartition générale
        des sports sur un mois choisi"""


if __name__ == "__main__":

	graphs = Create_graph(activities_file="activities/activities.csv")

	graphs.activities_sharing_all_time()