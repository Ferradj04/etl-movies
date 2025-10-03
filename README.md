# ETL Movies Project 🎬

## 1. Description

Ce projet est un **pipeline ETL (Extract, Transform, Load)** qui traite un dataset de films (Titanic dataset dans cet exemple) :

1. **Extraction** : téléchargement ou lecture du CSV brut.  
2. **Transformation** : nettoyage et ajout de colonnes (ex. `Age_Category`).  
3. **Chargement** : insertion des données transformées dans une base SQLite `movies.db`.  

L’objectif est de montrer un workflow ETL simple mais fonctionnel pour l’apprentissage.

---

## 2. Arborescence du projet

etl-movies/
│
├─ data/
│ ├─ movies.csv # CSV brut extrait
│ └─ movies_clean.csv # CSV transformé
├─ db/
│ └─ movies.db # Base SQLite créée par le pipeline
├─ scripts/
│ ├─ extract.py # Script d’extraction
│ ├─ transform.py # Script de transformation
│ ├─ load.py # Script de chargement
│ └─ pipeline.py # Script principal pour lancer le pipeline
└─ README.md # Documentation du projet


---

## 3. Prérequis

- Python >= 3.10  
- Packages Python :  

```bash
pip install pandas sqlalchemy
---

## 4. Lancer le projet

cd scripts
python .\scripts\pipeline.py

---



