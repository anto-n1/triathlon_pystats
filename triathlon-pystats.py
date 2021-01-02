#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__version = "1.0"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

import argparse
import sys
import os

from generate_pdf import Generate_pdf
from download_data import Download_data


def main():
    parser = argparse.ArgumentParser()
    
    if not os.path.exists("activities"):
        print("Aucun répertoire d'activités trouvé.")
        print("Création d'un répertoire.")
        os.mkdir("activities")

    # A l'avenir, pour génération graphiques
    #parser.add_argument("-g", "--generate", help="Choix du pdf à générer", action="store_true")

    parser.add_argument("-m", "--mail-garmin", help="Adresse mail Garmin Connect", default=False)

    parser.add_argument("-d", "--date", help="Date pour laquelle générer un document pdf ('YYYY', 'YYYY-MM', 'YYYY-MM-DD', 'all-time')")
      
    args = parser.parse_args()

    if not args.date:
        print("Merci de présicer une durée pour laquelle vous souhaitez obtenir un rapport.")
        print("Lancez la commande 'python triathlon-pystats.py --help' pour afficher l'aide.")
        sys.exit(0)

    if args.mail_garmin:
        download = Download_data(garmin_connect_mail=args.mail_garmin, number="all")
        download.dowlnoad_activities()

    pdf = Generate_pdf(activities_file="activities/activities.csv")
    pdf.generate_report(date=args.date)
    
    

if __name__ == "__main__":

    main()