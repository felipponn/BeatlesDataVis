import pandas as pd
import collections

def palavras_comuns_albuns(dataframe):
    """Esta função seleciona os álbuns do dataframe e transforma numa lista de
    strings com as palavras de todos os álbuns. Depois conta a frequência de cada
    palavra.

    :param dataframe: Base de dados
    :type dataframe: pd.DataFrame
    :return: Retorna as palavras mais comuns nos títulos dos álbuns
    :rtype: list
    """
    
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            albuns = dataframe.index.get_level_values(0) # Seleciona todos os albuns do dataframe
            lista_albuns = list(dict.fromkeys(albuns)) # Organiza-os em uma lista (cada album é uma string)
            lista_palavras = []
            for album in lista_albuns: # Transforma cada string de album em uma lista de palavras
                titulo = album.split()
                for palavra in titulo: # Adiciona cada palavra dos títulos dos albuns em uma lista criada
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras) # Verifica a quantidade de vezes que cada palavra aparece na lista
            palavras_comuns = quantidade_palavra.most_common(100) # Seleciona as palavras mais comuns da lista
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns
 
###############################################################################

def palavras_comuns_musicas(dataframe):
    """Esta função seleciona as músicas do dataframe e transforma numa lista de
    strings com as palavras de todas as músicas. Depois conta a frequência de cada
    palavra.

    :param dataframe: Base de dados
    :type dataframe: pd.DataFrame
    :return: Retorna as palavras mais comuns nos títulos das músicas
    :rtype: list
    """
    
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            musicas = dataframe.index.get_level_values(1) # Seleciona todos as músicas do dataframe
            lista_musicas = list(dict.fromkeys(musicas)) # Organiza as músicas em uma lista (cada música é uma string)
            lista_palavras = []
            for musica in lista_musicas: # Transforma cada string de música em uma lista de palavras
                titulo = musica.split()
                for palavra in titulo: # Adiciona cada palavra dos títulos das músicas em uma lista criada
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras) # Verifica a quantidade de vezes que cada palavra aparece na lista
            palavras_comuns = quantidade_palavra.most_common(100) # Seleciona as palavras mais comuns da lista
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns

###############################################################################

def palavras_comuns_letras_disco(dataframe):
    """Esta função seleciona as letras das músicas do dataframe e transforma numa lista de
    strings com as palavras nas letras de todas as músicas. Depois conta a frequência de cada
    palavra.

    :param dataframe: Base de dados
    :type dataframe: pd.DataFrame
    :return: Retorna as palavras mais comuns nas letras das músicas, em toda a discografia
    :rtype: list
    """
    
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            letras = dataframe["lyrics"] # Seleciona todas as letras das músicas de toda a discografia
            lista_letras = list(dict.fromkeys(letras)) # Organiza as letras em uma lista (cada letra é uma string)
            lista_palavras = []
            for letra in lista_letras: # Transforma cada string de letra em uma lista de palavras
                if isinstance(letra, type(1.0)):
                    continue
                palavras = letra.split()
                for palavra in palavras: # Adiciona cada palavra das letras das músicas em uma lista criada
                    lista_palavras.append(palavra)
            quantidade_palavra = collections.Counter(lista_palavras) # Verifica a quantidade de vezes que cada palavra aparece na lista
            palavras_comuns = quantidade_palavra.most_common(100) # Seleciona as palavras mais comuns da lista
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return palavras_comuns
 
###############################################################################

def palavras_comuns_letras_albuns(dataframe):
    """Esta função seleciona as letras das músicas do dataframe e transforma numa lista de
    strings com as palavras nas letras de todas as músicas, agrupadas por álbum. Depois conta a frequência de cada
    palavra.

    :param dataframe: Base de dados
    :type dataframe: pd.DataFrame
    :return: Retorna as palavras mais comuns nas letras das músicas, agrupadas por álbum
    :rtype: pd.core.series.Series
    """
    
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            album_data = dataframe.groupby("album").apply(palavras_comuns_letras_disco)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return album_data
 
 ###############################################################################

def titulo_album_letras(dataframe):
    """Esta função seleciona todos os álbuns únicos do dataframe e transforma numa série,
    seleciona todas as letras das músicas e também transforma numa série, e depois verifica 
    a recorrência de cada álbum nas letras, como dicionário.

    :param dataframe: Base de dados
    :type dataframe: pd.DataFrame
    :return: Retorna a recorrência dos álbuns nas letras
    :rtype: pd.core.series.Series
    """
    
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            albuns = dataframe.index.get_level_values(0) # Seleciona todos os albuns do dataframe
            serie_albuns = pd.Series(albuns).str.lower() # Cria uma série de álbuns 
            array_albuns = serie_albuns.unique() # Elimina as repetições de álbuns
            letras = dataframe["lyrics"] # Seleciona todas as letras do dataframe
            serie_letras = pd.Series(letras).str.lower() # Cria uma série de letras 
            array_letras = serie_letras.unique() # Elimina as repetições de letras
            dicio_relacao = {}
            for album in array_albuns: # Verifica se os álbuns da série têm relação com as letras da série
                dicio_relacao[album] = 0
                for letra in array_letras:
                    if isinstance(letra, type(1.0)):
                        continue
                    relacionamento = letra.count(album)
                    dicio_relacao[album] += relacionamento # Adiciona a relação álbum/letra em um dicionário
                    relacao = pd.Series(dicio_relacao)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return relacao
 
###############################################################################

def titulo_musica_letras(dataframe):
    """Esta função seleciona todas as músicas do dataframe e transforma numa série,
    seleciona todas as letras das músicas e também transforma numa série, e depois verifica 
    a recorrência de cada múscia nas letras, como dicionário.
    
    :param dataframe: Base de dados
    :type dataframe: pd.DataFrame
    :return: Retorna a recorrência das músicas nas letras
    :rtype: pd.core.series.Series
    """
    
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            musicas = dataframe.index.get_level_values(1) # Seleciona todos as músicas do dataframe
            serie_musicas = pd.Series(musicas).str.lower() # Cria uma série de músicas
            array_musicas = serie_musicas.unique() # Elimina as repetições de músicas
            letras = dataframe["lyrics"] # Seleciona todas as letras do dataframe
            serie_letras = pd.Series(letras).str.lower() # Cria uma série de letras
            array_letras = serie_letras.unique() # Elimina as repetições de letras
            dicio_relacao = {} 
            for musica in array_musicas: # Verifica se as músicas da série têm relação com as letras da série
                dicio_relacao[musica] = 0
                for letra in array_letras:
                    if isinstance(letra, type(1.0)):
                        continue
                    relacionamento = letra.count(musica)
                    dicio_relacao[musica] += relacionamento # Adiciona a relação música/letra em um dicionário
                    relacao = pd.Series(dicio_relacao)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")
    
    return relacao