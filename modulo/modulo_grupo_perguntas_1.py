import pandas as pd

def mais_x_por_album(dataframe, coluna):
    """
    Ordena as musicas do dataframe agrupado por album

    Args:
        dataframe : Dataframe com musicas da banda
        coluna : Coluna do Dataframe pela qual o dataframe será ordenado
    Returns:
        list: Lista com um dataframe contendo musicas por album
    """
    try:
        lista_albums = []
        albums= dataframe.index.levels[0] # lista com o nome dos albums
        for album in albums:
            musicas = dataframe.loc[album] # pega as linhas com músicas do album
            musicas_ordenadas = musicas.sort_values(by=coluna, ascending=False)[coluna] # ordena pela coluna
            lista_albums.append(musicas_ordenadas)
        return lista_albums

    except TypeError:
        print("Type Error")
    except KeyError:
        print("Key Error")
    except Exception as error:
        return error


def mais_x_da_banda(dataframe, coluna):
    """
    Ordena as musicas do dataframe sem agrupar

    Args:
        dataframe : Dataframe com musicas da banda
        coluna : Coluna do Dataframe pela qual o dataframe será ordenado
    Returns:
        dataframe: Dataframe com todas as musicas e a coluna pela qual foi ordenada
    """
    try:
        dataframe = dataframe.droplevel(0)
        dataframe.sort_values(by=coluna, ascending=False, inplace=True)
        return dataframe[coluna]
    except AttributeError:
        print("Attribute Error")
    except KeyError:
        print("Key Error")
    except Exception as error:
        return error


def mais_premiados_album(dataframe, coluna):
    """
    Ordena os albuns pelo numero de premiações

    Args:
        dataframe : Dataframe albums da banda e as respectivas premiações
        coluna : Coluna do Dataframe pela qual o dataframe será ordenado
    Returns:
        dataframe: Dataframe com albums e número de premiações ordenado  
    """
    try:
        dataframe = dataframe.sort_values(by=[coluna, "num_nominations"], ascending=False)
        dataframe = dataframe[["album",coluna, "num_nominations"]]
        dataframe.reset_index(inplace=True)       # Tira o index do dataframe antigo
        del dataframe['index']
        return dataframe
    except KeyError:
        print("Key Error")
    except AttributeError:
        print("Attribute Error")
    except Exception as error:
        return error

def correlacao(dataframe, coluna1, coluna2):
    """
    Correlação entre duas colunas de um dataframe

    Args:
        dataframe : Dataframe que contem as colunas 1 e 2
        coluna1 (string): coluna do dataframe
        coluna2 (string): coluna do dataframe

    Returns:
        float: correlação
    """
    try:
        return dataframe[coluna1].corr(dataframe[coluna2])
    except Exception as error:
        return error