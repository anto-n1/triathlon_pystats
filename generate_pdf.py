#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__uri__ = "https://git.antonin.io/projets_personnels/triathlon-pystats"

from shutil import copyfile
import re
import os
import random
import sys
import datetime

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
        Générer rapport journalier/mensuel/annuel
        Ce rapport contient des statistiques basiques sans historique
        """
        
        verify_date = self._activities.verify_date(date=date)

        # Nom du mois et de l'année en français
        month_name = verify_date[3]

        # Nom du fichier pdf à générer
        report_file_name = "statistiques-triathlon-{}.tex".format(date)
        copyfile("template.tex", report_file_name)

        if date == "all-time":
            month_name = "Tous les temps"

            today = datetime.date.today()
            generation_date = today.strftime("%b-%d-%Y")

            date_text = month_name + " (au " + generation_date + ")"

            with open(report_file_name, 'r+') as report_file:
                text = report_file.read()

                # Remplacer les termes dans le template tex
                text = re.sub("RDATE", date_text, text)

                report_file.seek(0)
                report_file.write(text)
                report_file.truncate()


        # Choix de l'image à afficher sur la page de titre
        # Image choisie au hasard parmis les 8 disponibles
        image_number = random.randrange(start=1, stop=8, step=1)
        image_name = "triathlon-{}.png".format(image_number)

        # Page 1 : tous sports confondus

        # Nombre d'entrainements total du mois
        training_nb = str(self._activities.get_number_activities(date=date,
                                                                 sport="all"))
        training_ratio = str(self._stats.number_activities_per_day(date=date,
                                                                   sport="all"))

        # Distance totale
        distance = str(self._stats.total_distance(date=date, sport="all"))

        # Dénivelé
        total_elevation = str(self._stats.total_elevation(date=date,
                                                          sport="all"))

        # Temps total d'activité
        duration = str(self._stats.activities_duration(date=date,sport="all"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date, sport="all"))
        
        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                        sport="all"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="all"))

        # VO2max moyenne
        average_vo2max = str(self._stats.average_vo2max(date=date,
                                                        sport="all"))

        # VO2max max
        max_vo2max = str(self._stats.max_vo2max(date=date, sport="all"))

        # Génération des graphiques
        # Les noms des graphiques sont directement indiqués dans template.tex
        self._graphs.activities_sharing(date=date)
        self._graphs.time_sharing(date=date)
        self._graphs.distance_sharing(date=date)
        self._graphs.location_sharing_all_sports(date=date)
        self._graphs.distribution_ht_road(date=date)
        self._graphs.distribution_trail_running(date=date)

        # Partie statistiques tous sports confondus
        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer les termes dans le template tex
            text = re.sub("RDATE", month_name, text)
            text = re.sub("RNAME", "Antonin", text)
            text = re.sub("RIMAGE", image_name, text)
            text = re.sub("RACTIVITIES-NUMBER", training_nb, text)
            text = re.sub("RRATIO", training_ratio, text)
            text = re.sub("RDURATION", duration, text)
            text = re.sub("RTOTAL-DISTANCE", distance, text)
            text = re.sub("RAVERAGE-SPEED", average_speed, text)
            text = re.sub("RAVERAGE-HR", average_hr, text)
            text = re.sub("RMAX-HR", max_hr, text)
            text = re.sub("RMAX-VO2", max_vo2max, text)
            text = re.sub("RAVERAGE-VO2", average_vo2max, text)
            text = re.sub("RELEVATION", total_elevation, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()


        # Cyclisme

        # Nombre d'entrainements total du mois et ratio
        training_nb = str(self._activities.get_number_activities(date=date,
                                                            sport="cyclisme"))
        training_ratio = str(self._stats.number_activities_per_day(date=date,
                                                            sport="cyclisme"))

        # Nombre d'entrainements total home trainer du mois
        training_nb_ht = str(self._activities.get_number_activities(date=date,
                                                            sport="home_trainer"))

        # Distance totale
        distance = str(self._stats.total_distance(date=date,sport="cyclisme"))

        # Distance totale home trainer
        distance_ht = str(self._stats.total_distance(date=date,sport="home_trainer"))

        # Distance totale route
        distance_road = float(distance) - float(distance_ht)
        distance_road = str(round(distance_road, 2))
        
        # Dénivelé
        elevation = str(self._stats.total_elevation(date=date,
                                                    sport="cyclisme"))
                                                    
        # Dénivelé home trainer
        elevation_ht = str(self._stats.total_elevation(date=date,
                                                    sport="home_trainer"))
        
        # Dénivelé route
        elevation_road = float(elevation) - float(elevation_ht)
        elevation_road = str(round(elevation_road))

        # Temps total d'activité
        duration = str(self._stats.activities_duration(date=date,
                                                       sport="cyclisme"))

        # Temps total d'activité home trainer
        duration_ht = str(self._stats.activities_duration(date=date,
                                                       sport="home_trainer"))

        # Temps total d'activité route
        total = self._stats.activities_duration(date=date, sport="cyclisme")
        ht = self._stats.activities_duration(date=date, sport="home_trainer")
        duration_road = total - ht
        duration_road = str(duration_road)

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date,
                                                      sport="cyclisme"))
        
        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                        sport="cyclisme"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="cyclisme"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RCACTIVITIES-NUMBER", training_nb, text)
            text = re.sub("RHOMETRAINER-NUMBER", training_nb_ht, text)

            text = re.sub("RCRATIO", training_ratio, text)

            text = re.sub("RCDURATION", duration, text)
            text = re.sub("RCHTDURATION", duration_ht, text)
            text = re.sub("RCHROADDURATION", duration_road, text)

            text = re.sub("RCTOTAL-DISTANCE", distance, text)
            text = re.sub("RCTOTALHT-DISTANCE", distance_ht, text)
            text = re.sub("RCTOTALROAD-DISTANCE", distance_road, text)

            text = re.sub("RCAVERAGE-SPEED", average_speed, text)

            text = re.sub("RCAVERAGE-HR", average_hr, text)
            text = re.sub("RCMAX-HR", max_hr, text)

            text = re.sub("RCELEVATION", elevation, text)
            text = re.sub("RCELEVHT", elevation_ht, text)
            text = re.sub("RCELEVROAD", elevation_road, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()

        # Running

        # Nombre d'entrainements total du mois
        training_nb = str(self._activities.get_number_activities(date=date,
                                                            sport="running"))
        training_ratio = str(self._stats.number_activities_per_day(date=date,
                                                            sport="running"))

        # Distance totale
        distance = str(self._stats.total_distance(date=date, sport="running"))

        # Distance totale trail
        distance_trail = str(self._stats.total_distance(date=date, sport="trail"))

        # Distance totale route
        distance_road = float(distance) - float(distance_trail)
        distance_road = str(distance_road)

        # Dénivelé total
        elevation = str(self._stats.total_elevation(date=date,
                                                    sport="running"))
        # Dénivelé trail
        elevation_trail = str(self._stats.total_elevation(date=date,
                                                    sport="trail"))

        # Dénivelé route
        elevation_road = int(elevation) - int(elevation_trail)
        elevation_road = str(elevation_road)

        # Temps total d'activité
        duration = str(self._stats.activities_duration(date=date,
                                                       sport="running"))
        # Temps total d'activité trail
        duration_trail = str(self._stats.activities_duration(date=date,
                                                       sport="trail"))

        # Temps total d'activité route
        d_trail = self._stats.activities_duration(date=date, sport="trail")
        d_running = self._stats.activities_duration(date=date, sport="running")
        duration_road = d_running - d_trail
        duration_road = str(duration_road)

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date,
                                                      sport="running"))
        
        # Fréquence cardiaque moyenne du mois
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                        sport="running"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="running"))

        # VO2max moyenne
        average_vo2max = str(self._stats.average_vo2max(date=date,
                                                        sport="running"))

        # VO2max max
        max_vo2max = str(self._stats.max_vo2max(date=date, sport="running"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RPACTIVITIES-NUMBER", training_nb, text)
            text = re.sub("RPRATIO", training_ratio, text)
            
            text = re.sub("RPDURATION", duration, text)
            text = re.sub("RPTRAILDURATION", duration_trail, text)
            text = re.sub("RPROADDURATION", duration_road, text)

            text = re.sub("RPTOTAL-DISTANCE", distance, text)
            text = re.sub("RPTOTALROAD-DISTANCE", distance_road, text)
            text = re.sub("RPTOTALTRAIL-DISTANCE", distance_trail, text)
            
            text = re.sub("RPAVERAGE-SPEED", average_speed, text)
            
            text = re.sub("RPAVERAGE-HR", average_hr, text)
            text = re.sub("RPMAX-HR", max_hr, text)
            text = re.sub("RPMAX-VO2", max_vo2max, text)
            text = re.sub("RPAVERAGE-VO2", average_vo2max, text)
            
            text = re.sub("RPELEVATION", elevation, text)
            text = re.sub("RPROADELEVATION", elevation_road, text)
            text = re.sub("RPTRAILELEVATION", elevation_trail, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()

        # Natation

        # Nombre d'entrainements total du mois
        training_nb = str(self._activities.get_number_activities(date=date,
                                                            sport="natation"))
        training_ratio = str(self._stats.number_activities_per_day(date=date,
                                                            sport="natation"))

        # Distance totale
        distance = str(self._stats.total_distance(date=date,
                                                sport="natation"))

        # Temps total d'activité
        duration = str(self._stats.activities_duration(date=date,
                                                       sport="natation"))

        # Vitesse moyenne tous sports confondus
        average_speed = str(self._stats.average_speed(date=date,
                                                      sport="natation"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RNACTIVITIES-NUMBER", training_nb, text)
            text = re.sub("RNRATIO", training_ratio, text)
            text = re.sub("RNDURATION", duration, text)
            text = re.sub("RNTOTAL-DISTANCE", distance, text)
            text = re.sub("RNAVERAGE-SPEED", average_speed, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()

        # Renforcement musculaire

        # Nombre d'entrainements total du mois
        training_nb = str(self._activities.get_number_activities(date=date,
                                                            sport="renfo"))
        training_ratio = str(self._stats.number_activities_per_day(date=date,
                                                            sport="renfo"))

        # Temps total d'activité
        total_duration = str(self._stats.activities_duration(date=date,
                                                             sport="renfo"))
        
        # Fréquence cardiaque moyenne
        average_hr = str(self._stats.average_heart_rate(date=date,
                                                             sport="renfo"))

        # Fréquence cardiaque maximale
        max_hr = str(self._stats.max_heart_rate(date=date, sport="renfo"))

        with open(report_file_name, 'r+') as report_file:
            text = report_file.read()

            # Remplacer le template
            text = re.sub("RMACTIVITIES-NUMBER", training_nb, text)
            text = re.sub("RMRATIO", training_ratio, text)
            text = re.sub("RMDURATION", total_duration, text)
            text = re.sub("RMAVERAGE-HR", average_hr, text)
            text = re.sub("RMMAX-HR", max_hr, text)
            
            report_file.seek(0)
            report_file.write(text)
            report_file.truncate()
        
        # Compilation fichier tex
        self.compile_latex_pdf(report_file_name)

        print("\nFichier généré dans {}.".format(report_file_name.replace("tex", "pdf")))

    def generate_report_history(self, date):
        """
        Générer rapport annuel/tous les temps avec historique de temps
        Ce rapport contient des statistiques pour évaluer la progression
        """
        
        verify_date = self._activities.verify_date(date=date)

        # Nom du mois et de l'année en français
        month_name = verify_date[3]

        # Nom du fichier pdf à générer
        report_file_name = "statistiques-triathlon-{}.tex".format(date)
        copyfile("template.tex", report_file_name)

        if date == "all-time":
            month_name = "Tous les temps"

            today = datetime.date.today()
            generation_date = today.strftime("%b-%d-%Y")

            date_text = month_name + " (au " + generation_date + ")"

            with open(report_file_name, 'r+') as report_file:
                text = report_file.read()

                # Remplacer les termes dans le template tex
                text = re.sub("RDATE", date_text, text)

                report_file.seek(0)
                report_file.write(text)
                report_file.truncate()


        # Choix de l'image à afficher sur la page de titre
        # Image choisie au hasard parmis les 8 disponibles
        image_number = random.randrange(start=1, stop=8, step=1)
        image_name = "triathlon-{}.png".format(image_number)

        # Page 1 : tous sports confondus

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

    pdf.generate_report(date="all-time")
