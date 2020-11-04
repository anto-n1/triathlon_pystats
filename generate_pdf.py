#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

from shutil import copyfile
import re
import os
import random

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

        # Nombre d'entrainements total du mois
        training_number_all = str(self._activities.get_number_activities(month=month, sport="All"))
        training_per_day = str(self._statistics.number_activities_per_day(month=month, sport="All"))

        # Distance totale
        total_distance = str(self._statistics.total_distance(month=month, sport="All"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._statistics.average_speed(month=month, sport="All"))
        
        # Nombre d'entrainements cyclisme, natation, running et renfo
        training_number_cycling = str(self._activities.get_number_activities(month=month, sport="Cyclisme"))
        training_number_swimming = str(self._activities.get_number_activities(month=month, sport="Natation"))
        training_number_running = str(self._activities.get_number_activities(month=month, sport="Running"))
        training_number_strength = str(self._activities.get_number_activities(month=month, sport="Renfo"))

        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._statistics.average_heart_rate(month=month, sport="All"))
        # Fréquence cardiaque maximale
        max_hr = str(self._activities.get_max_heart_rate(month=month, sport="All"))

        # Fréquences cardiaques moyenne pour chaque sport
        average_hr_cycling = self._statistics.average_heart_rate(month=month, sport="Cyclisme")
        average_hr_running = self._statistics.average_heart_rate(month=month, sport="Running")
        # Ca existait pas en aout
        #average_hr_strength = self._statistics.average_heart_rate(month=month, sport="Renfo")

        report_file_name = "rapport-triathlon-{}.tex".format(month)
        copyfile("template_month.tex", report_file_name)

        image_number = random.randrange(start=1, stop=8, step=1)
        image_name = "triathlon-{}.png".format(image_number)

        # Génération des graphiques
        # Les noms des graphiques sont directement indiqués dans le template.tex
        self._graphs.activities_sharing(month=month)

        # Partie statistiques tous sports confondus
        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RMONTH", month, text)
            text = re.sub("RNAME", "Antonin", text)
            text = re.sub("RIMAGE", image_name, text)
            text = re.sub("RACTIVITIES-NUMBER", training_number_all, text)
            text = re.sub("RRATIO", training_per_day, text)
            text = re.sub("RTOTAL-DISTANCE", total_distance, text)
            text = re.sub("RAVERAGE-SPEED", average_speed, text)
            text = re.sub("RAVERAGE-HR", average_hr, text)
            text = re.sub("RMAX-HR", max_hr, text)
            
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()
        
        self.compile_latex_pdf(report_file_name)


    def compile_latex_pdf(self, pdf_name):
        """
        Compiler le fichier .tex et supprimer les fichiers inutiles
        """

        extensions_to_delete = ["aux", "bcf", "fls", "log", "out", "run.xml", "fdb_latexmk", "synctex.gz", "toc"]

        os.system("pdflatex {}".format(pdf_name))
        
        dir = os.listdir("./")

        for item in dir:
            for extension in extensions_to_delete:
                if item.endswith(extension):
                    os.remove(os.path.join(item))

if __name__ == "__main__":

    pdf = Generate_pdf(activities_file="activities/activities.csv")
    pdf.generate_month_report(month="2020-08")
