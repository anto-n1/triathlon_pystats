#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

from shutil import copyfile
import re

from create_graphics import Create_graphics
from make_statistics import Make_statistics
from parse_csv_activities import Parse_csv_activities

class Generate_pdf:
    """
    Générer des PDF à partir des fichiers templates LaTeX
    """

    def __init__(self, activities_file):
        self._graphs = Create_graphics(activities_file=activities_file)
        self._activities = Parse_csv_activities(activities_file=activities_file)
        self._statistics = Make_statistics(activities_file=activities_file)

    def generate_month_report(self, month):
        """
        Générer rapport mensuel
        month -> 2020-11
        """

        # Générer :
        # - nombre d'entrainements total
        # - nombre d'entrainement par sport
        # - graph camembert pourcentage par sport

        # Remplacer les termes dans le template

        self._graphs.activities_sharing(month=month)

        # Nombre d'entrainements total du mois
        training_number_all = self._activities.get_number_activities(month=month, sport="All")
        
        # Nombre d'entrainements cyclisme, natation, running et renfo
        training_number_cycling = self._activities.get_number_activities(month=month, sport="Cyclisme")
        training_number_swimming = self._activities.get_number_activities(month=month, sport="Natation")
        training_number_running = self._activities.get_number_activities(month=month, sport="Running")
        training_number_strength = self._activities.get_number_activities(month=month, sport="Renfo")

        # Fréquence cardiaque moyenne du mois
        average_hr_all = self._statistics.average_heart_rate(month=month, sport="All")

        # Fréquences cardiaques moyenne pour chaque sport
        average_hr_cycling = self._statistics.average_heart_rate(month=month, sport="Cyclisme")
        average_hr_running = self._statistics.average_heart_rate(month=month, sport="Running")
        average_hr_strength = self._statistics.average_heart_rate(month=month, sport="Renfo")

        report_file_name = "rapport-triathlon-{}.tex".format(month)
        copyfile("template_month.tex", report_file_name)

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub('rapport', 'test', text)
            text = re.sub('Se', 'ouaiiiis', text)
            text = re.sub('école', 'camarche', text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()


    def compile_latex_pdf(self, pdf_name):
        """
        Compiler le fichier .tex
        """
        pass

if __name__ == "__main__":

    pdf = Generate_pdf(activities_file="activities/activities.csv")
    pdf.generate_month_report(month="2020-10")
