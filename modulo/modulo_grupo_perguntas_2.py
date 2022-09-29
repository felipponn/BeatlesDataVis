import pandas as pd
import collections

def palavras_comuns_albuns(dataframe):
    if isinstance(dataframe, pd.DataFrame):
        try:
            albuns = dataframe.index.get_level_values(1)
            lista_albuns = list(dict.fromkeys(albuns))
            lista_palavras = []
            for album in lista_albuns:
                titulo = album.split()
                for palavra in titulo:
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras)
            palavras_comuns = quantidade_palavra.most_common(3)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

def palavras_comuns_musicas(dataframe):
    if isinstance(dataframe, pd.DataFrame):
        try:
            musicas = dataframe.index.get_level_values(1)
            lista_musicas = list(dict.fromkeys(musicas))
            lista_palavras = []
            for musica in lista_musicas:
                titulo = musica.split()
                for palavra in titulo:
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras)
            palavras_comuns = quantidade_palavra.most_common(3)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

def palavras_comuns_letras_albuns(dataframe):
    if isinstance(dataframe, pd.DataFrame):
        try:
            letras = dataframe["lyrics"].groupby(["album"])
            lista_letras = list(dict.fromkeys(letras))
            lista_palavras = []
            for letra in lista_letras:
                palavras = letra.split()
                for palavra in palavras:
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras)
            palavras_comuns = quantidade_palavra.most_common(3)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

def palavras_comuns_letras_disco(dataframe):
    if isinstance(dataframe, pd.DataFrame):
        try:
            letras = dataframe["lyrics"]
            lista_letras = list(dict.fromkeys(letras))
            lista_palavras = []
            for letra in lista_letras:
                palavras = letra.split()
                for palavra in palavras:
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras)
            palavras_comuns = quantidade_palavra.most_common(3)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

def titulo_album_letras(dataframe):
    if isinstance(dataframe, pd.DataFrame):
        try:
            albuns = dataframe.index.get_level_values(1)
            serie_albuns = pd.Series(albuns)
            array_albuns = serie_albuns.unique()
            letras = dataframe["lyrics"]
            serie_letras = pd.Series(letras)
            array_letras = serie_letras.unique()
            dicio_relacao = {}
            for album in array_albuns:
                dicio_relacao[album] = 0
                for letra in array_letras:
                    relacionamento = letra.count(album)
                    dicio_relacao[album] += relacionamento
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return dicio_relacao

###############################################################################

def titulo_musica_letras(dataframe):
    if isinstance(dataframe, pd.DataFrame):
        try:
            musicas = dataframe.index.get_level_values(1)
            serie_musicas = pd.Series(musicas)
            array_musicas = serie_musicas.unique()
            letras = dataframe["lyrics"]
            serie_letras = pd.Series(letras)
            array_letras = serie_letras.unique()
            dicio_relacao = {}
            for musica in array_musicas:
                dicio_relacao[musica] = 0
                for letra in array_letras:
                    relacionamento = letra.count(musica)
                    dicio_relacao[musica] += relacionamento
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return dicio_relacao