from decimal import DivisionByZero
from statistics import mean
from traceback import print_tb
import pandas as pd
import numpy as np

# 1. Como a participação dos membros numa música influenciou em sua popularidade?

# 1.a. Composição

def media_popularidade_compositor(dataframe):
    """Função que retorna dataframe da popularidade média de músicas de cada compositor.

    :param dataframe: Dataframe de dados da banda.
    :type dataframe: pd.DataFrame
    :return: popularidades médias de cada compositor
    :rtype: pd.DataFrame
    """
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            lista_compositores = dict() # Dicionário do tipo compositor -> popularidade_media
            creditos_composicao = dataframe['songwriters_parsed'] # série de compositores
            popularidades = dataframe['popularity'] # série de popularidades
            N = len(creditos_composicao) # qtd de músicas
            for indice in range(N):
                compositores_msc = creditos_composicao[indice][1:-1].split(', ')
                for compositor in compositores_msc:
                    nome_compositor = compositor[0:]
                    if nome_compositor not in lista_compositores:
                        lista_compositores[nome_compositor] = np.array([1, popularidades[indice]])
                    else:
                        lista_compositores[nome_compositor] += np.array([1, popularidades[indice]])
            for indice_compositor in range(len(lista_compositores)):
                qtd_creditos = lista_compositores[list(lista_compositores.keys())[indice_compositor]][0]
                soma_popularidade = lista_compositores[list(lista_compositores.keys())[indice_compositor]][1]
                lista_compositores[list(lista_compositores.keys())[indice_compositor]] = soma_popularidade/qtd_creditos
            
            df_compositores = pd.DataFrame(lista_compositores.items(), columns=["Compositor", "Popularidade Média"]) # Converte para dataframe
            df_compositores = df_compositores.sort_values(by=["Popularidade Média"], ascending=False) # Ordena
            return df_compositores
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

# 1.b. Vocais

def media_popularidade_vocal(dataframe):
    """Função que gera popularidades médias das músicas em que cada membro canta.

    :param dataframe: Dataframe de dados da banda.
    :type dataframe: pd.DataFrame
    :return: Popularidade média das músicas com dado vocalista.
    :rtype: pd.DataFrame
    """
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            lista_vocais = {"McCartney":0, "Lennon":0, "Harrison":0, "Starr":0, "Instrumental":0, "Sound Collage":0}
            for voz in lista_vocais:
                lista_vocais[voz] = np.array([0, 0])
            creditos_vocal = dataframe['vocals_parsed']
            popularidades = dataframe['popularity']
            N = len(creditos_vocal)
            for indice in range(N):
                vocais_msc = creditos_vocal[indice]
                for voz in lista_vocais:
                    if voz in vocais_msc:
                        lista_vocais[voz] += np.array([1, popularidades[indice]])
            for indice_vocal in range(len(lista_vocais)):
                qtd_creditos = lista_vocais[list(lista_vocais.keys())[indice_vocal]][0]
                soma_popularidade = lista_vocais[list(lista_vocais.keys())[indice_vocal]][1]
                lista_vocais[list(lista_vocais.keys())[indice_vocal]] = soma_popularidade/qtd_creditos
            df_vocais = pd.DataFrame(lista_vocais.items(), columns=["Vocalista", "Popularidade Média"]) # Converte para dataframe
            df_vocais = df_vocais.sort_values(by=["Popularidade Média"], ascending=False) # Ordena
            return df_vocais
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

###############################################################################

# 2. Qual a porcentagem de participação em vocal de cada membro em dado álbum?

def porcentagem_participacao_album(dataframe):
    """Função que gera porcentagens de participação dos membros em cada álbum.

    :param dataframe: Dataframe de dados da banda.
    :type dataframe: pd.DataFrame
    :return: Porcentagens de participação para cada álbum e para cada membro.
    :rtype: pd.DataFrame
    """
    lista_albuns = ["Please Please Me", "With The Beatles", "A Hard Day's Night", "Beatles for Sale", "Help!", "Rubber Soul", "Revolver", "Sgt. Pepper's Lonely Hearts Club Band", "Magical Mystery Tour", "The Beatles (white album)", "Yellow Submarine", "Abbey Road", "Let It Be"]
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            dict_albuns = dict()
            for album in lista_albuns:
                df_novo = dataframe.reset_index()
                mask = (df_novo["album"] == album)
                df_novo = df_novo[mask]
                dict_membros = {"McCartney": 0, "Lennon": 0, "Harrison": 0, "Starr": 0}
                qtd_mscs = len(df_novo)
                participacoes = []

                for indice in range(qtd_mscs):
                    creditos_vocais = list(df_novo["vocals_parsed"])
                    creditos_composicao = list(df_novo["songwriters_parsed"])
                    participacao = creditos_vocais[indice] + creditos_composicao[indice]
                    participacoes.append(participacao)

                for participacoes_musica in participacoes:
                    for membro in dict_membros:
                        if membro in participacoes_musica:
                            dict_membros[membro] += (100/qtd_mscs)
                
                dict_albuns[album] = dict_membros
            
            # Conversão para dataframe
            resultado = []
            for album in lista_albuns:
                for membro in ["McCartney", "Lennon", "Harrison", "Starr"]:
                    resultado.append([album, membro, dict_albuns[album][membro]])

            return pd.DataFrame.from_records(resultado)
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

###############################################################################

# 3. Qual é a verborragia de cada álbum?

def verborragia(dataframe):
    """Função que indica a verborragia média de cada álbum.

    :param dataframe: Dataframe de dados da banda.
    :type dataframe: pd.DataFrame
    :return: Média de palavras por segundo de cada álbum.
    :rtype: pd.DataFrame
    """
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            lista_albuns = ["Please Please Me", "With The Beatles", "A Hard Day's Night", "Beatles for Sale", "Help!", "Rubber Soul", "Revolver", "Sgt. Pepper's Lonely Hearts Club Band", "Magical Mystery Tour", "The Beatles (white album)", "Yellow Submarine", "Abbey Road", "Let It Be"]

            resultado = dict()

            for album in lista_albuns:
                df_novo = dataframe.reset_index()
                mask = (df_novo["album"] == album)
                df_novo = df_novo[mask]
                musicas_album = list(df_novo["song"])
                letras = df_novo["lyrics"]
                duracoes = df_novo["duration_ms"]

                verborragia_album = []

                for indice_musica in range(len(df_novo)):
                    letra_musica = letras[letras.keys()[indice_musica]]
                    if isinstance(letra_musica, type(1.5)):
                        letra_musica = ""
                    qtd_palavras = len(letra_musica.split())
                    duracao_seg = duracoes[duracoes.keys()[indice_musica]]/1000
                    palavras_por_seg = qtd_palavras/duracao_seg
                    verborragia_album.append(palavras_por_seg)

                media_album = mean(verborragia_album)
                arredondamento = int(media_album*100)/100

                resultado[album] = arredondamento
            
            return pd.DataFrame(resultado.items(), columns=["Álbum", "Média de Palavras/seg"])
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

###############################################################################