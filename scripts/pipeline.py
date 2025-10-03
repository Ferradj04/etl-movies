from extract import extract
from transform import transform
from load import load
from showdb import showdb

if __name__ == "__main__":
    print("🚀 Lancement du pipeline ETL")
    extract()
    transform()
    load()
    print("🎉 Pipeline terminé avec succès")
    showdb()
