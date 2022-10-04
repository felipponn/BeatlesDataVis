import pandas as pd
import numpy as np

# 1. Como a participação dos membros numa música influenciou em sua popularidade?

# 1.a. Composição

def media_popularidade_compositor(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            lista_compositores = dict()
            creditos_composicao = dataframe['songwriters_parsed']
            eh_cover = dataframe['cover']
            popularidades = dataframe['popularity']
            N = len(creditos_composicao)
            for indice in range(N):
                compositores_msc = creditos_composicao[indice][1:-1].split(', ')
                if eh_cover[indice] == "VERDADEIRO":
                    msc_eh_cover = True
                else:
                    msc_eh_cover = False
                for compositor in compositores_msc:
                    nome_compositor = compositor[0:]
                    if msc_eh_cover:
                        nome_compositor = "COVER: "+nome_compositor
                    if nome_compositor not in lista_compositores:
                        lista_compositores[nome_compositor] = np.array([1, popularidades[indice]])
                    else:
                        lista_compositores[nome_compositor] += np.array([1, popularidades[indice]])
            for indice_compositor in range(len(lista_compositores)):
                qtd_creditos = lista_compositores[list(lista_compositores.keys())[indice_compositor]][0]
                soma_popularidade = lista_compositores[list(lista_compositores.keys())[indice_compositor]][1]
                lista_compositores[list(lista_compositores.keys())[indice_compositor]] = soma_popularidade/qtd_creditos
            return lista_compositores
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

# 1.b. Vocais

def media_popularidade_vocal(dataframe):
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            lista_vocais = dict()
            creditos_vocal = dataframe['vocals_parsed']
            popularidades = dataframe['popularity']
            N = len(creditos_vocal)
            for indice in range(N):
                vocais_msc = creditos_vocal[indice][1:-1].split(', ')
                for vocal in vocais_msc:
                    nome_vocal = vocal[0:]
                    if nome_vocal not in lista_vocais:
                        lista_vocais[nome_vocal] = np.array([1, popularidades[indice]])
                    else:
                        lista_vocais[nome_vocal] += np.array([1, popularidades[indice]])
            for indice_vocal in range(len(lista_vocais)):
                qtd_creditos = lista_vocais[list(lista_vocais.keys())[indice_vocal]][0]
                soma_popularidade = lista_vocais[list(lista_vocais.keys())[indice_vocal]][1]
                lista_vocais[list(lista_vocais.keys())[indice_vocal]] = soma_popularidade/qtd_creditos
            return lista_vocais
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

###############################################################################

# 2. Qual a porcentagem de participação em vocal de cada membro em dado álbum?

def porcentagem_vocal_album(dataframe, album):
    lista_albuns = ["Please Please Me", "With The Beatles", "A Hard Day's Night", "Beatles for Sale", "Help!", "Rubber Soul", "Revolver", "Sgt. Pepper's Lonely Hearts Club Band", "Magical Mystery Tour", "The Beatles (white album)", "Yellow Submarine", "Abbey Road", "Let It Be"]
    if album not in lista_albuns:
        return "Insira um álbum válido da discografia da banda."
    if isinstance(dataframe, pd.DataFrame): # Verifica se é um dataframe
        try: # Trata as exceções para essa função
            df_novo = dataframe.reset_index()
            mask = (df_novo["album"] == album)
            df_novo = df_novo[mask]
            dict_vocais_album = {"McCartney": 0, "Lennon": 0, "Harrison": 0, "Starr": 0}
            N = len(df_novo)

            for musica in df_novo["vocals_parsed"]:
                for membro in dict_vocais_album:
                    if membro in musica:
                        dict_vocais_album[membro] += (100/N)
            
            return dict_vocais_album
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

###############################################################################

# 3. O quais são os picos e vales de verborragia de cada álbum?

def verborragia(dataframe):
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
                    arredondamento = int(palavras_por_seg*100)/100
                    verborragia_album.append(arredondamento)

                verborragia_max = verborragia_album[0]
                verborragia_max_nome = musicas_album[0]

                for indice in range(1, len(musicas_album)):
                    if verborragia_album[indice] > verborragia_max:
                        verborragia_max = verborragia_album[indice]
                        verborragia_max_nome = musicas_album[indice]

                verborragia_min = verborragia_album[0]
                verborragia_min_nome = musicas_album[0]

                for indice in range(1, len(musicas_album)):
                    if verborragia_album[indice] < verborragia_min:
                        verborragia_min = verborragia_album[indice]
                        verborragia_min_nome = musicas_album[indice]
                
                resultado[album] = {"Máximo": verborragia_max_nome+": "+str(verborragia_max)+" palavras por segundo", "Mínimo": verborragia_min_nome+": "+ str(verborragia_min)+" palavras por segundo"}
            
            return pd.DataFrame(resultado).transpose()
        except Exception as error:
            return error
    else:
        print("Não é do tipo pd.DataFrame! Insira um dataframe adequado.")

###############################################################################