# Triathlon-pystats

Programme python permettant de réaliser des statistiques à partir de données récoltées sur Garmin Connect.

Programme basé sur le script python [garmin-connect-export](https://github.com/pe-st/garmin-connect-export) sur Github.

Récupération des activités :

```bash
git clone https://github.com/pe-st/garmin-connect-export.git
cd garmin-connect-export
python gcexport.py --username antonin.info@protonmail.com -d ../activities --count all
# Si une seule activité à récupérer :
python gcexport.py --username antonin.info@protonmail.com -d ../activities --count 1
```

Python 3.8 utilisé pour les développements.

# TODO :

* https://medium.com/@azholud/analysis-and-visualization-of-activities-from-garmin-connect-b3e021c62472
