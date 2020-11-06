# Triathlon-pystats

## Objectifs du programme Triathlon-pystats

L'objectif du programme est de générer des PDF contenant des statistiques
écrites, et sous formes de graphiques. Il est possible de générer des PDF
pour des périodes mensuelles. Les périodes annuelles et "tous les temps"
sont prévues.

Exemple du rendu PDF :

![Exemple rendu PDF](images/example.png)

## Fonctionnement

La réalisation de statistiques se base sur un fichier "activities.csv",
obtenu à partir de l'API Garmin Connect (Polar non compatible). Pour
obtenir le fichier, il faut utiliser le script python
[garmin-connect-export](https://github.com/pe-st/garmin-connect-export) sur
Github.

Commande pour récupérer les activités et le fichier activities.csv :

```bash
git clone https://github.com/pe-st/garmin-connect-export.git
cd garmin-connect-export

# Récupérer toutes les activités
python gcexport.py --username <email> -d ../activities --count all

# Récupérer la dernière activité
python gcexport.py --username <email> -d ../activities --count 1
```

Commandes pour générer les PDF :

```bash
en cours de rédaction...
```

## Informations

* Version python : 3.8
* Génération des PDF basée sur [LaTeX](https://www.latex-project.org)
* Génération des graphiques basée sur [Matplotlib](https://matplotlib.org)

## TODO :

* Génération de PDF anuelles et tous les temps
* Ajouter des graphiques sur différents lieux : [atricle Medium](https://medium.com/@azholud/analysis-and-visualization-of-activities-from-garmin-connect-b3e021c62472)
* Expliquer fonctionnement de la génération des PDF sur le Readme
