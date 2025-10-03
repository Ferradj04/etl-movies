import pandas as pd
from sqlalchemy import create_engine
import os

def load():
    # Créer le dossier db si inexistant
    os.makedirs("../db", exist_ok=True)

    # Lire le CSV transformé
    df = pd.read_csv("../data/movies_clean.csv")

    # Créer la connexion SQLite
    engine = create_engine("sqlite:///../db/movies.db")

    # Charger le DataFrame dans SQLite
    df.to_sql("movies", engine, if_exists="replace", index=False)
    print("✅ Chargement terminé dans ../db/movies.db")

if __name__ == "__main__":
    load()
