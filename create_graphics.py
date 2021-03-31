#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__uri__ = "https://git.antonin.io/projets_personnels/triathlon-pystats"

import os
from datetime import timedelta

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd

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

        nb_cycling = self._activities.get_number_activities(date=date,
                                                            sport="cyclisme")
        nb_running = self._activities.get_number_activities(date=date,
                                                            sport="running")
        nb_natation = self._activities.get_number_activities(date=date,
                                                             sport="natation")
        nb_renfo = self._activities.get_number_activities(date=date,
                                                          sport="renfo")

        sports = [ "Cyclisme\n{} activité(s)".format(nb_cycling),
                   "Running\n{} activité(s)".format(nb_running),
                   "Natation\n{} activité(s)".format(nb_natation),
                   "Renfo\n{} activité(s)".format(nb_renfo) ]
        
        sizes = [ nb_cycling, nb_running, nb_natation, nb_renfo ]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

        # Ne pas afficher les valeurs à 0
        if nb_cycling == 0:
            sports.remove("Cyclisme\n{} activité(s)".format(nb_cycling))
            sizes.remove(nb_cycling)
            colors.remove(colors[0])

        if nb_running == 0:
            sports.remove("Running\n{} activité(s)".format(nb_running))
            sizes.remove(nb_running)
            colors.remove(colors[0])

        if nb_natation == 0:
            sports.remove("Natation\n{} activité(s)".format(nb_natation))
            sizes.remove(nb_natation)
            colors.remove(colors[0])

        if nb_renfo == 0:
            sports.remove("Renfo\n{} activité(s)".format(nb_renfo))
            sizes.remove(nb_renfo)
            colors.remove(colors[0])

        plt.pie(sizes,
                colors=colors,
                labels=sports,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85)

        centre_circle = plt.Circle((0, 0), 0.70, fc="white")
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis("equal")  
        plt.tight_layout()
        #plt.show()
        plt.savefig(filename, dpi=800, bbox_inches="tight")
        plt.close()
    
    def distance_sharing(self, date):
        """
        Générer un graphique camembert sur la répartition générale des sports
        par rapport à la distance parcourue
        """

        filename = "images/graphs/repartition_distance.png"
        if os.path.exists(filename):
            os.remove(filename)

        distance_cycling = self._stats.total_distance(
            date=date,
            sport="cyclisme")

        distance_running = self._stats.total_distance(date=date,
                                                      sport="running")
        distance_natation = self._stats.total_distance(date=date,
                                                       sport="natation")

        sports = [ "Cyclisme\n{} km".format(distance_cycling),
                   "Running\n{} km".format(distance_running),
                   "Natation\n{} km".format(distance_natation) ]

        sizes = [ distance_cycling, distance_running, distance_natation ]

        colors = ['#ff9999','#66b3ff','#99ff99']

        # Ne pas afficher les valeurs à 0
        if distance_cycling == 0:
            sports.remove("Cyclisme\n{} km".format(distance_cycling))
            sizes.remove(distance_cycling)
            colors.remove(colors[0])

        if distance_running == 0:
            sports.remove("Running\n{} km".format(distance_running))
            sizes.remove(distance_running)
            colors.remove(colors[0])

        if distance_natation == 0:
            sports.remove("Natation\n{} km".format(distance_natation))
            sizes.remove(distance_natation)
            colors.remove(colors[0])

        plt.pie(sizes,
                colors=colors,
                labels=sports,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85)

        centre_circle = plt.Circle((0, 0), 0.70, fc="white")
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis("equal")  
        plt.tight_layout()
        #plt.show()
        plt.savefig(filename, dpi=800, bbox_inches="tight")
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

        sports = [ "Cyclisme\n{}".format(time_cycling),
                   "Running\n{}".format(time_running),
                   "Natation\n{}".format(time_natation),
                   "Renfo\n{}".format(time_renfo) ]

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
            sports.remove("Cyclisme\n{}".format(time_cycling))
            sizes.remove(time_cycling_seconds)
            colors.remove(colors[0])

        if time_running_seconds == 0:
            sports.remove("Running\n{}".format(time_running))
            sizes.remove(time_running_seconds)
            colors.remove(colors[0])

        if time_natation_seconds == 0:
            sports.remove("Natation\n{}".format(time_natation))
            sizes.remove(time_natation_seconds)
            colors.remove(colors[0])

        if time_renfo_seconds == 0:
            sports.remove("Renfo\n{}".format(time_renfo))
            sizes.remove(time_renfo_seconds)
            colors.remove(colors[0])

        plt.pie(sizes,
                colors=colors,
                labels=sports,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85)

        centre_circle = plt.Circle((0, 0), 0.70, fc="white")
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis("equal")  
        plt.tight_layout()
        #plt.show()
        plt.savefig(filename, dpi=800, bbox_inches="tight")
        plt.close()

    def location_sharing_all_sports(self, date):
        """
        Générer un graphique camembert sur la répartition générale des sports
        par rapport au lieu
        """

        filename = "images/graphs/repartition_place.png"
        if os.path.exists(filename):
            os.remove(filename)

        location_1 = "La Haie-Fouassière"
        location_2 = "Angers"
        location_3 = "Cholet"
        location_4 = "Autre"

        location_cycling_dict = self._stats.activities_location(
            date=date,
            sport="cyclisme"
        )
        
        location_running_dict = self._stats.activities_location(
            date=date,
            sport="running"
        )

        nb_location_1 = location_cycling_dict[location_1] + location_running_dict[location_1]
        nb_location_2 = location_cycling_dict[location_2] + location_running_dict[location_2]
        nb_location_3 = location_cycling_dict[location_3] + location_running_dict[location_3]
        nb_location_4 = location_cycling_dict[location_4] + location_running_dict[location_4]

        sports = [ "{}\n{} fois".format(location_1, nb_location_1),
                   "{}\n{} fois".format(location_2, nb_location_2),
                   "{}\n{} fois".format(location_3, nb_location_3),
                   "{}\n{} fois".format(location_4, nb_location_4) ]

        sizes = [ nb_location_1, nb_location_2, nb_location_3, nb_location_4 ]

        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

        # Ne pas afficher les valeurs à 0
        if nb_location_1 == 0:
            sports.remove("{}\n{} fois".format(location_1, nb_location_1))
            sizes.remove(nb_location_1)
            colors.remove(colors[0])

        if nb_location_2 == 0:
            sports.remove("{}\n{} fois".format(location_2, nb_location_2))
            sizes.remove(nb_location_2)
            colors.remove(colors[0])

        if nb_location_3 == 0:
            sports.remove("{}\n{} fois".format(location_3, nb_location_3))
            sizes.remove(nb_location_3)
            colors.remove(colors[0])
        
        if nb_location_4 == 0:
            sports.remove("{}\n{} fois".format(location_4, nb_location_4))
            sizes.remove(nb_location_4)
            colors.remove(colors[0])

        plt.pie(sizes,
                colors=colors,
                labels=sports,
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85)

        centre_circle = plt.Circle((0, 0), 0.70, fc="white")
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis("equal")  
        plt.tight_layout()
        #plt.show()
        plt.savefig(filename, dpi=800, bbox_inches="tight")
        plt.close()

    def distance_history(self, date):
        """Graphique permettant de visualiser l'historique
        des distances parcourues mensuellement"""

        #if len(date) == 4:

        x = np.arange(12)

        distance = self._activities.get_distances_list(date=date, sport="all")

        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(distance)
        plt.bar(x, distance)
        plt.xticks(x, ('Jan', 'Fev', 'Mar', 'Avr', "Mai", "Juin", "Jui", "Aou", "Sep", "Oct", "Nov", "Dec"))
        plt.show()
        
    def distribution_ht_road(self, date):
        """Graphique permettant de visualiser la répartition des km
        réalisés sur route et sur home trainer en vélo"""

        filename = "images/graphs/repartition_distances_velo.png"
        if os.path.exists(filename):
            os.remove(filename)

        km_ht = self._stats.total_distance(date=date,sport="home_trainer")
        km_total = self._stats.total_distance(date=date,sport="cyclisme")
        km_road = km_total - km_ht
        km_road = round(km_road, 2)

        ## Default
        df_bar = pd.DataFrame([km_road, km_ht], index=['Route', 'Home trainer'], columns=['growth'])
        df_bar.plot(kind='barh')

        # 1. Delete legend legend=False
        # 2. Tighten the space between bars width=0.8
        width = 0.8
        fig, ax = plt.subplots(figsize=(6, 3))
        df_bar.plot(kind='barh', legend=False, ax=ax, width=width)
        # 3. Re-order the y-axis
        ax.invert_yaxis()

        # 4. Delete the square spines
        [spine.set_visible(False) for spine in ax.spines.values()]

        # 5. Delete ticks for x and y axis
        # 6. Delete tick label for x axis
        ax.tick_params(bottom=False, left=False, labelbottom=False)

        # 7. Increase the size of the label for y axis
        ax.tick_params(axis='y', labelsize='x-large')

        # 8. Display each value next to the bar
        vmax = df_bar['growth'].max()

        for i, value in enumerate(df_bar['growth']):
            ax.text(value+vmax*0.02, i, f'{value:,}', fontsize='x-large', va='center', color='C0')

        plt.savefig(filename, dpi=800, bbox_inches="tight")
        plt.close()

    def distribution_trail_running(self, date):
        """Graphique permettant de visualiser la répartition des km
        réalisés sur route et en trail en course à pied"""

        filename = "images/graphs/repartition_distances_cap.png"
        if os.path.exists(filename):
            os.remove(filename)

        km_trail = self._stats.total_distance(date=date,sport="trail")
        km_total = self._stats.total_distance(date=date,sport="running")
        km_road = km_total - km_trail
        km_road = round(km_road, 2)

        ## Default
        df_bar = pd.DataFrame([km_road, km_trail], index=['Route', 'Trail'], columns=['growth'])
        df_bar.plot(kind='barh')

        # 1. Delete legend legend=False
        # 2. Tighten the space between bars width=0.8
        width = 0.8
        fig, ax = plt.subplots(figsize=(6, 3))
        df_bar.plot(kind='barh', legend=False, ax=ax, width=width)
        # 3. Re-order the y-axis
        ax.invert_yaxis()

        # 4. Delete the square spines
        [spine.set_visible(False) for spine in ax.spines.values()]

        # 5. Delete ticks for x and y axis
        # 6. Delete tick label for x axis
        ax.tick_params(bottom=False, left=False, labelbottom=False)

        # 7. Increase the size of the label for y axis
        ax.tick_params(axis='y', labelsize='x-large')

        # 8. Display each value next to the bar
        vmax = df_bar['growth'].max()

        for i, value in enumerate(df_bar['growth']):
            ax.text(value+vmax*0.02, i, f'{value:,}', fontsize='x-large', va='center', color='C0')

        plt.savefig(filename, dpi=800, bbox_inches="tight")
        plt.close()

if __name__ == "__main__":

	graphs = Create_graphics(activities_file="activities/activities.csv")

	graphs.distribution_ht_road(date="2021")
