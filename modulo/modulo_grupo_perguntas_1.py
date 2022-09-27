import pandas as pd

# dt = pd.read_csv("C:/Users/otavi/Desktop/FGV/Python/A1 LP/TheBeatlesCleaned.csv")

def mais_ouvidas_album(dataframe, coluna):
    lista_albums = []
    albums= pd.unique(dataframe["album"])
    for album in albums:
        serie = dataframe.loc[(dataframe["album"] == album)]
        serie["musica"].sort_values(by=coluna, ascending=False, inplace=True)
        lista_albums.append(serie)

    return lista_albums


def mais_longas_album(dataframe, coluna):
    dataframe.sort_values(by=coluna)
    

def mais_ouvidas_banda(dataframe, coluna):
    dataframe.sort_values(by=coluna, ascending=False, inplace=True)
    return dataframe[coluna].head(10)

def mais_longas_banda(dataframe, coluna):
    dataframe.sort_values(by=coluna, ascending=False, inplace=True)
    return dataframe[["song", coluna]].head(10)

def mais_premiados_album(dataframe, coluna):
    return


# print(dt)
# print(mais_longas_banda(dt, "duration_ms"))