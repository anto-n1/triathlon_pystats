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

    def generate_report(self, date):
        """
        Générer rapport
        """
        
        self._activities.verify_date(date=date)

        # Nom du fichier
        report_file_name = "rapport-triathlon-{}.tex".format(date)
        copyfile("template.tex", report_file_name)

        # Choix de l'image à afficher sur la page de titre
        image_number = random.randrange(start=1, stop=8, step=1)
        image_name = "triathlon-{}.png".format(image_number)

        # TOUS LES SPORTS

        # Nombre d'entrainements total du mois
        training_number = str(self._activities.get_number_activities(date=date, sport="all"))
        training_per_day = str(self._stats.number_activities_per_day(date=date, sport="all"))

        # Distance totale
        total_distance = str(self._stats.total_distance(date=date, sport="all"))

        # Dénivelé
        total_elevation = str(self._stats.total_elevation(date=date, sport="all"))

        # Temps total d'activité
        total_duration = str(self._stats.activities_duration(date=date, sport="all"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date, sport="all"))
        
        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                             sport="all"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="all"))

        # VO2max moyenne
        average_vo2max = str(self._stats.average_vo2max(date=date, sport="all"))

        # VO2max max
        max_vo2max = str(self._stats.max_vo2max(date=date, sport="all"))

        # Génération des graphiques
        # Les noms des graphiques sont directement indiqués dans le template.tex
        self._graphs.activities_sharing(date=date)
        self._graphs.time_sharing(date=date)
        self._graphs.distance_sharing(date=date)
        self._graphs.location_sharing_all_sports(date=date)

        # Partie statistiques tous sports confondus
        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RDATE", date, text)
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

        # CYCLISME

        # Nombre d'entrainements total du mois
        training_number = str(self._activities.get_number_activities(date=date, sport="cyclisme"))
        training_per_day = str(self._stats.number_activities_per_day(date=date, sport="cyclisme"))

        # Distance totale
        total_distance = str(self._stats.total_distance(date=date, sport="cyclisme"))

        # Dénivelé
        total_elevation = str(self._stats.total_elevation(date=date, sport="cyclisme"))

        # Temps total d'activité
        total_duration = str(self._stats.activities_duration(date=date, sport="cyclisme"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date, sport="cyclisme"))
        
        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                             sport="cyclisme"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="cyclisme"))

        # VO2max moyenne
        average_vo2max = str(self._stats.average_vo2max(date=date, sport="cyclisme"))

        # VO2max max
        max_vo2max = str(self._stats.max_vo2max(date=date, sport="cyclisme"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RCACTIVITIES-NUMBER", training_number, text)
            text = re.sub("RCRATIO", training_per_day, text)
            text = re.sub("RCDURATION", total_duration, text)
            text = re.sub("RCTOTAL-DISTANCE", total_distance, text)
            text = re.sub("RCAVERAGE-SPEED", average_speed, text)
            text = re.sub("RCAVERAGE-HR", average_hr, text)
            text = re.sub("RCMAX-HR", max_hr, text)
            text = re.sub("RCMAX-VO2", max_vo2max, text)
            text = re.sub("RCAVERAGE-VO2", average_vo2max, text)
            text = re.sub("RCELEVATION", total_elevation, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()

        # RUNNING

        # Nombre d'entrainements total du mois
        training_number = str(self._activities.get_number_activities(date=date, sport="running"))
        training_per_day = str(self._stats.number_activities_per_day(date=date, sport="running"))

        # Distance totale
        total_distance = str(self._stats.total_distance(date=date, sport="running"))

        # Dénivelé
        total_elevation = str(self._stats.total_elevation(date=date, sport="running"))

        # Temps total d'activité
        total_duration = str(self._stats.activities_duration(date=date, sport="running"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date, sport="running"))
        
        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                             sport="running"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="running"))

        # VO2max moyenne
        average_vo2max = str(self._stats.average_vo2max(date=date, sport="running"))

        # VO2max max
        max_vo2max = str(self._stats.max_vo2max(date=date, sport="running"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RPACTIVITIES-NUMBER", training_number, text)
            text = re.sub("RPRATIO", training_per_day, text)
            text = re.sub("RPDURATION", total_duration, text)
            text = re.sub("RPTOTAL-DISTANCE", total_distance, text)
            text = re.sub("RPAVERAGE-SPEED", average_speed, text)
            text = re.sub("RPAVERAGE-HR", average_hr, text)
            text = re.sub("RPMAX-HR", max_hr, text)
            text = re.sub("RPMAX-VO2", max_vo2max, text)
            text = re.sub("RPAVERAGE-VO2", average_vo2max, text)
            text = re.sub("RPELEVATION", total_elevation, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()

        # NATATION

        # Nombre d'entrainements total du mois
        training_number = str(self._activities.get_number_activities(date=date, sport="natation"))
        training_per_day = str(self._stats.number_activities_per_day(date=date, sport="natation"))

        # Distance totale
        total_distance = str(self._stats.total_distance(date=date, sport="natation"))

        # Temps total d'activité
        total_duration = str(self._stats.activities_duration(date=date, sport="natation"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date, sport="natation"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RNACTIVITIES-NUMBER", training_number, text)
            text = re.sub("RNRATIO", training_per_day, text)
            text = re.sub("RNDURATION", total_duration, text)
            text = re.sub("RNTOTAL-DISTANCE", total_distance, text)
            text = re.sub("RNAVERAGE-SPEED", average_speed, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()

        # RENFO

        # Nombre d'entrainements total du mois
        training_number = str(self._activities.get_number_activities(date=date, sport="renfo"))
        training_per_day = str(self._stats.number_activities_per_day(date=date, sport="renfo"))

        # Temps total d'activité
        total_duration = str(self._stats.activities_duration(date=date, sport="renfo"))
        
        # Fréquence cardiaque moyenne
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                             sport="renfo"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="renfo"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RMACTIVITIES-NUMBER", training_number, text)
            text = re.sub("RMRATIO", training_per_day, text)
            text = re.sub("RMDURATION", total_duration, text)
            text = re.sub("RMAVERAGE-HR", average_hr, text)
            text = re.sub("RMMAX-HR", max_hr, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()
        
        # Compilation fichier tex
        self.compile_latex_pdf(report_file_name)

        print("\nFichier généré dans {}.".format(report_file_name.replace("tex", "pdf")))

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

    pdf.generate_report(date="2020-11")
