#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__version__ = "0.2"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

from shutil import copyfile
import re
import os
import random
import sys

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
        self._stats = Make_statistics(activities_file=activities_file)

    def generate_month_report(self, month):
        """
        Générer rapport mensuel
        """

        if len(month) != 7:
            print("Impossible de générer un rapport mensuel pour la date " \
                  "renseignée.")
            print("Le format de mois accepté est : 'YYYY-MM'")
            sys.exit(1)

        # Nombre d'entrainements total du mois
        training_number = str(self._activities.get_number_activities(date=month, sport="all"))
        training_per_day = str(self._stats.number_activities_per_day(date=month, sport="all"))

        # Distance totale
        total_distance = str(self._stats.total_distance(date=month, sport="all"))

        # Dénivelé
        total_elevation = str(self._stats.total_elevation(date=month, sport="all"))

        # Temps total d'activité
        total_duration = str(self._stats.activities_duration(date=month, sport="all"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=month, sport="all"))
        
        # Nombre d'entrainements cyclisme, natation, running et renfo
        #training_number_cycling = str(self._activities.get_number_activities(date=month, sport="cyclisme"))
        #training_number_swimming = str(self._activities.get_number_activities(date=month, sport="natation"))
        #training_number_running = str(self._activities.get_number_activities(date=month, sport="running"))
        #training_number_strength = str(self._activities.get_number_activities(date=month, sport="renfo"))

        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._stats.average_heart_rate(date=month,
                                                             sport="all"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=month, sport="all"))

        # VO2max moyenne
        average_vo2max = str(self._stats.average_vo2max(date=month, sport="all"))
        # VO2max max
        max_vo2max = str(self._stats.max_vo2max(date=month, sport="all"))

        # Fréquences cardiaques moyenne pour chaque sport
       # average_hr_cycling = self._stats.average_heart_rate(date=month, sport="cyclisme")
       # average_hr_running = self._stats.average_heart_rate(date=month, sport="running")   
       # average_hr_strength = self._stats.average_heart_rate(date=month, sport="renfo")

        report_file_name = "rapport-triathlon-{}.tex".format(month)
        copyfile("template_month.tex", report_file_name)

        image_number = random.randrange(start=1, stop=8, step=1)
        image_name = "triathlon-{}.png".format(image_number)

        # Génération des graphiques
        # Les noms des graphiques sont directement indiqués dans le template.tex
        #self._graphs.activities_sharing(date=month)
        self._graphs.time_sharing(date=month)
        self._graphs.distance_sharing(date=month)

        # Partie statistiques tous sports confondus
        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RMONTH", month, text)
            text = re.sub("RNAME", "Antonin", text)
            text = re.sub("RIMAGE", image_name, text)
            text = re.sub("RACTIVITIES-NUMBER", training_number, text)
            text = re.sub("RRATIO", training_per_day, text)
            text = re.sub("RDURATION", total_duration, text)
            text = re.sub("RTOTAL-DISTANCE", total_distance, text)
            text = re.sub("RAVERAGE-SPEED", average_speed, text)
            text = re.sub("RAVERAGE-HR", average_hr, text)
            text = re.sub("RMAX-HR", max_hr, text)
            text = re.sub("RMAX-VO2", max_vo2max, text)
            text = re.sub("RAVERAGE-VO2", average_vo2max, text)
            text = re.sub("RELEVATION", total_elevation, text)
            
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()
        
        self.compile_latex_pdf(report_file_name)

    def compile_latex_pdf(self, tex_filename):
        """
        Compiler le fichier .tex et supprimer les fichiers inutiles
        """

        extensions_to_delete = ["aux", "bcf", "fls", "log", "out", "run.xml",
                                "fdb_latexmk", "synctex.gz", "toc" ]

        os.system("pdflatex {}".format(tex_filename))
        
        dir = os.listdir("./")
        for item in dir:
            for extension in extensions_to_delete:
                if item.endswith(extension):
                    os.remove(os.path.join(item))

        os.remove(tex_filename)

if __name__ == "__main__":

    pdf = Generate_pdf(activities_file="activities/activities.csv")
    pdf.generate_month_report(month="2020-11")
