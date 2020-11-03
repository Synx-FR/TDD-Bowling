# CONFIGURATION DE PIP POUR NEXUS RTE
Pour Windows dans le fichier
`C:\Users\MONUSER\pip\pip.ini`

Pour Linux dans le répertoire
`$HOME/.pip/pip.conf`

Créer un fichier pip.ini avec le contenu suivant

```
[global]
index = https://devin-depot.rte-france.com/repository/pypi-all/pypi
index-url = https://devin-depot.rte-france.com/repository/pypi-all/simple
trusted-host = devin-depot.rte-france.com
```

Puis faire les lignes de commande suivantes:

=> `py -3 -m venv bowling_env`

activer l'environnement

=> `pip install -r ./requirements-dev.txt`

ctrl + shift + p : Python Discover Tests
(choisir Pytest)