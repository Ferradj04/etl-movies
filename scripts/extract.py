import pandas as pd

def extract():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    df.to_csv("../data/movies.csv", index=False)
    print("✅ Extraction terminée, données sauvegardées dans data/movies.csv")
    return df

if __name__ == "__main__":
    extract()
