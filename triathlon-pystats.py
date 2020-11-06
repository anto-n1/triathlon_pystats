#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__version = "0.2"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

import argparse
import sys

from generate_pdf import Generate_pdf

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-g", "--generate", help="Choix du pdf à générer", action="store_true",)

    parser.add_argument("-f", "--activities-file", help="Chemin du fichier contenant les activités", default="activities/activities.csv", action="store_true")

    parser.add_argument("-a", "--get-activities", help="Télécharger les activités", action="store_true")

    #parser.add_argument("-t", "--type", help="Choix du type de PDF", default="normal") # pdf simple ou avec évolution diagramme batons

    parser.add_argument("-d", "--date", help="Date pour laquelle générer un document pdf ('YYYY', 'YYYY-MM', 'YYYY-MM-DD', 'all-time')")

    args = parser.parse_args()

    pdf = Generate_pdf(activities_file=args.activities_file)

    if args.get_activities:
        print("Téléchargement des activitées indisponible actuellement.")
        sys.exit(1)

    if args.date:
        pdf.generate_report(date=args.date)
    