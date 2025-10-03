import pandas as pd
import os

def transform():
    # Créer dossier data au niveau du projet
    os.makedirs("../data", exist_ok=True)
    
    # Lire le CSV généré par extract.py
    df = pd.read_csv("../data/movies.csv")
    
    # Nettoyage (Titanic dataset)
    df = df.dropna(subset=["Age", "Sex"])
    
    # Ajouter une colonne Age_Category
    df["Age_Category"] = df["Age"].apply(
        lambda x: "Old" if x >= 65 else "Adult" if x >= 18 else "Teenage" if x >= 13 else "Child"
    )
    
    # Sauvegarder le CSV transformé
    df.to_csv("../data/movies_clean.csv", index=False)
    print("✅ Transformation terminée, données sauvegardées dans ../data/movies_clean.csv")
    return df

if __name__ == "__main__":
    transform()
