# Stucture du projet

```
├── documentation  # Liste des documentations en markdown
|
├── jenkins
|   └── build.groovy  # pipeline pour build l'application
|   └── tests.groovy  # pipeline pour run les tests l'application
|
├── migrations
|   ├── version  # Contient les fichiers de version de bases de données
|
├── tests  # Contient les fichiers de tests de l'application
|
├── api
    └── __init__.py  # point d'entrée de l'application
│   └── databases.py  # Défini la fonction de session de base de données
│   └── settings.py  # Traitement des variables d'environnements
|
│   ├── Des dossier par fonctionnalité (Authentication, Upload ...) #
│       └── depends.py   # Déclaration de fonctions de dépendances
│       └── models.py    # Déclaration des models de base de données (modifier ses objets altères la base de données)
│       └── routes.py    # Déclaration des routes de l'API ( GET, POST, PUT, DELETE )
│       └── schemas.py   # Déclaration de schémas de données
│       
└── .gitignore
└── .env # Fichier de configuration, ne doit pas être poussé sur git
└── .env.example # Template pour créer un fichier .env conforme
└── pyproject.toml # Fichier de dépendances
```
