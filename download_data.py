#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__uri__ = "https://git.antonin.io/projets_personnels/triathlon-pystats"

from git import Repo
import os
import shutil
import sys

class Download_data:
    """
    Télécharger les activités sur garming connect
    """

    def __init__(self, garmin_connect_mail, number="all"):
        self._garmin_connect_mail = garmin_connect_mail
        self._number = number

    def clone_git_repo(self):
        """
        Cloner le repo github https://github.com/pe-st/garmin-connect-export
        si non présent. Ce repo permet de télécharger les activités sur
        Garmin connect
        """

        git_url = "https://github.com/pe-st/garmin-connect-export"
        repo_dir = "garmin-connect-export"

        if not os.path.exists(repo_dir):
            Repo.clone_from(git_url, repo_dir)

    def dowlnoad_activities(self):
        """
        Télécharger les activités sur Garmin Connect
        """

        # Télécharger repo git si non existant
        self.clone_git_repo()

        if self._number == "all":
            if os.path.exists("activities"):

                print("Un répertoire d'activités est déjà présent.")
                question = "Shouaitez-vous supprimer ce répertoire et les télécharger à nouveau ? (y/n) "
                
                choice = input(question).lower()
                
                yes = {'yes','y', 'ye', ''}
                no = {'no','n'}
                
                if choice in yes:
                    shutil.rmtree("activities")
                    os.system("python garmin-connect-export/gcexport.py --username {} -d activities --count {}".format(self._garmin_connect_mail, self._number))

                elif choice in no:
                    pass

                else:
                    sys.stdout.write("Merci de répondre par 'yes' ou 'no'.")
            else:
                print("Téléchargement des activités...")
                os.system("python garmin-connect-export/gcexport.py --username {} -d activities --count {}".format(self._garmin_connect_mail, self._number))

if __name__ == "__main__":

    download = Download_data(garmin_connect_mail="mail@test.com", number="all")

    download.dowlnoad_activities()
