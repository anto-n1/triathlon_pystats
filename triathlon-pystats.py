#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__version = "0.2"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

import argparse

from generate_pdf import Generate_pdf

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-g", "--generate", help="increase output verbosity")
    parser.add_argument("-t", "--type", help="increase output verbosity") # pdf simple ou avec évolution diagramme batons

    args = parser.parse_args()

    if args.verbosity:
        print("verbosity turned on")


    pdf = Generate_pdf(activities_file="activities.csv")