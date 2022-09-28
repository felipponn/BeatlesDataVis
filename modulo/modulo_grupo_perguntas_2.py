import pandas as pd
import collections

def palavras_comuns_albuns(dataframe):
    albuns = dataframe.index.get_level_values(1)
    lista_albuns = list(dict.fromkeys(albuns))
    lista_palavras = []
    for album in lista_albuns:
        titulo = album.split()
        for palavra in titulo:
            lista_palavras.append(palavra)
    quantidade_palavra = collections.Counter(lista_palavras)
    palavras_comuns = quantidade_palavra.most_common(3)
    
    return palavras_comuns

def palavras_comuns_musica(dataframe):
    musicas = dataframe.index.get_level_values(1)
    lista_musicas = list(dict.fromkeys(musicas))
    lista_palavras = []
    for musica in lista_musicas:
        titulo = musica.split()
        for palavra in titulo:
            lista_palavras.append(palavra)
    quantidade_palavra = collections.Counter(lista_palavras)
    palavras_comuns = quantidade_palavra.most_common(3)
    
    return palavras_comuns

def palavras_comuns_letras_alb(dataframe):
    letras = dataframe["lyrics"].groupby(["album"])
    lista_letras = list(dict.fromkeys(letras))
    lista_palavras = []
    for letra in lista_letras:
        palavras = letra.split()
        for palavra in palavras:
            lista_palavras.append(palavra)
    quantidade_palavra = collections.Counter(lista_palavras)
    palavras_comuns = quantidade_palavra.most_common(3)
    
    return palavras_comuns

def palavras_comuns_letras_disc(dataframe):
    letras = dataframe["lyrics"]
    lista_letras = list(dict.fromkeys(letras))
    lista_palavras = []
    for letra in lista_letras:
        palavras = letra.split()
        for palavra in palavras:
            lista_palavras.append(palavra)
    quantidade_palavra = collections.Counter(lista_palavras)
    palavras_comuns = quantidade_palavra.most_common(3)
    
    return palavras_comuns