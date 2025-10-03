import sqlite3
import pandas as pd

    
def showdb():    
    # Connexion à la base de données
    conn = sqlite3.connect("../db/movies.db")

    # Voir les tables disponibles
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
    print("Tables dans la DB :", tables)

    # Lire le contenu de la table 'movies'
    df = pd.read_sql("SELECT * FROM movies LIMIT 1000;", conn)  # Affiche les 10 premières lignes
    print(df)

    conn.close()

if __name__ == "__main__":
    showdb()
