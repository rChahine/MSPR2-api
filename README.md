# MSPR2-API

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg?style=flat)
![FastAPI](https://img.shields.io/badge/fastapi-v0.62-yellow.svg?style=flat)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-v1.3-red.svg?style=flat)
![PostgreSQL](https://img.shields.io/badge/postgresql-v13-red.svg?style=flat)
![Uvicorn](https://img.shields.io/badge/uvicorn-v0.13-green.svg?style=flat)

## Environnement virtuel

Cette API utilise [Poetry]("https://python-poetry.org/docs/#installation") pour gérer les dépendances et les environnements virtuels.

**commandes utiles :** 

```bash
    poetry install # installe les dépendances de pyproject.toml et installe le projet
    poetry add <nom du package> # ajoute au projet une dépendance
    poetry remove <nom du package> # supprime une dépendance 
```


## Base de données

Cette API utilise le driver psycopg2 pour se connecter à une base de données PostgresSQL

## Documentations

1. [Installation](documentation/code-architecture.md)

Une modification pour déclencher le build sur jenkins.
