#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Antonin DOUILLARD"
__email__ = "antonin.info@protonmail.com"
__description__ = "Triathlon-pystats"
__VERSION__ = "0.1"
__uri__ = "https://git.antonin.io/projets/triathlon-pystats"

import matplotlib.pyplot as plt
from parse_csv_activities import Parse_csv_activities

activities = Parse_csv_activities("activities/activities.csv")

labels = 'Running', 'Vélo', 'Natation', 'Renfo'
sizes = [ activities.number_running_activities(), activities.number_cycling_activities(),
            activities.number_swimming_activities(), activities.number_strength_training_activities() ]

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.savefig('PieChart02.png')
plt.show()
