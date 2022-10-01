import pandas as pd

df1 = pd.read_csv("BeatlesDB.csv", sep='|')
df2 = pd.read_csv("Letras.csv", sep="|", encoding="macintosh")

lista_albuns = ["Please Please Me", "With The Beatles", "A Hard Day's Night", "Beatles for Sale", "Help!", "Rubber Soul", "Revolver", "Sgt. Pepper's Lonely Hearts Club Band", "Magical Mystery Tour", "The Beatles (white album)", "Yellow Submarine", "Abbey Road", "Let It Be"]

df2_mask = df2["album"].isin(lista_albuns)
df2 = df2[df2_mask]
df2 = df2.rename(columns={"title":"song"})
df2 = df2.drop(columns=["year"])

beatles = df1.merge(df2, left_on=("song", "album"), right_on=("song", "album")).set_index(["album", "song"]).sort_index()

beatles.to_csv('beatlesDF.csv', sep='|')
