import pandas as pd

def mais_x_por_album(dataframe, coluna):
    try:
        lista_albums = []
        albums= pd.unique(dataframe["album"]) # lista com o nome dos albums 
        for album in albums:
            musicas = dataframe.loc[(dataframe["album"] == album)] #pega as linhas com músicas do album
            musicas_ordenadas = musicas.sort_values(by=coluna, ascending=False)["song"] # ordena pela coluna
            dt = pd.DataFrame(data=musicas_ordenadas) # transforma em DataFrame
            dt.reset_index(inplace=True) # Tira o index do dataframe antigo
            del dt['index']
            lista_albums.append(dt)
        return lista_albums

    except TypeError:
        print("te")
    except KeyError:
        print("ke")
    except Exception as error:
        return error


def mais_x_da_banda(dataframe, coluna):
    try:
        dataframe.sort_values(by=coluna, ascending=False, inplace=True)
        return dataframe[["song", coluna]]

    except AttributeError:
        print("ae")
    except KeyError:
        print("ke")
    except Exception as error:
        return error


def mais_premiados_album(dataframe, coluna):
    try:
        dataframe= dataframe.loc[:, ('album', coluna)]
        dataframe.drop_duplicates(inplace=True)
        dataframe.sort_values(by=coluna, ascending=False, inplace=True)
        dataframe.reset_index(inplace=True)
        del dataframe['index']
        return dataframe

    except KeyError:
        print("Ke")
    except AttributeError:
        print("Ae")
    except Exception as error:
        return error

def mais_ouvidas_album(dataframe, coluna):
    lista_albums = []
    albums= pd.unique(dataframe["album"])
    for album in albums:
        serie = dataframe.loc[(dataframe["album"] == album)]
        serie["musica"].sort_values(by=coluna, ascending=False, inplace=True)
        lista_albums.append(serie)

    return lista_albums