from modulo import *
from pacote_modulos import *
import modulo_grupo_perguntas_1 as mp
import seaborn as sns
import pandas as pd
import matplotlib.pylab as plt

beatlesDF = dataset.beatlesDF
# beatlesDF = dataset.beatlesDF

def musicas_mais_populares_da_banda(dataframe):
    try:
        dataframe = dataframe.reset_index() # tira o multindex do dataframe
        plt.figure(figsize=(12, 6))         # cria a janela do gráfico
        plot = sns.barplot(                 # gráfico de barras
        x="song",
        y="popularity",
        data=dataframe.sort_values("popularity", ascending=False).head(5), # pegas as linhas com 5 maiores popularidade
        color="#7BC5FF"
        )
        plot.set(title="Músicas mais Populares")      # titulo
        plot.set_xlabel( "Músicas" , size = 12 )      # eixo x
        plot.set_ylabel( "Popularidade", size = 12)   # eixo y
        plot.set_ylim(50, 90)                         # quando do eixo será mostrado
        fig = plot.get_figure()
        fig.savefig("./img/Musicas Mais Populares dos Beatles.png")  # salva a figura
    except Exception as error:
        return error


def musicas_menos_populares_da_banda(dataframe):
    try:
        dataframe = dataframe.reset_index()  # tira o multindex do dataframe
        plt.figure(figsize=(12, 6))          # cria a janela do gráfico
        plot = sns.barplot(                  # gráfico de barras
        x="song",
        y="popularity",
        data=dataframe.sort_values("popularity").head(5), # pegas as linhas com 5 menores popularidade
        color="#7BC5FF"
        )
        plot.set(title="Músicas menos Populares")
        plot.set_xlabel( "Músicas" , size = 12 )
        plot.set_ylabel( "Popularidade", size = 12)
        plot.set_ylim(0, )
        fig = plot.get_figure()
        fig.savefig("./img/Musicas Menos Populares dos Beatles.png")
    except Exception as error:
        return error


def musicas_mais_longas_da_banda(dataframe):
    try:
        dataframe = dataframe.reset_index()
        dataframe["duration_sec"]=dataframe["duration_ms"]/1000 # transforma ms em segundos
        plt.figure(figsize=(12, 6))
        plot = sns.barplot(
        x="song",
        y="duration_sec",
        data=dataframe.sort_values("duration_sec", ascending=False).head(5), # as 5 linhas com maior duração
        color="#7BC5FF"
        )
        plot.set(title="Músicas mais Longas")
        plot.set_xlabel( "Músicas" , size = 12 )
        plot.set_ylabel( "Duração (sec)", size = 12)
        plot.set_ylim(0, )
        fig = plot.get_figure()
        fig.savefig("./img/Musicas Mais Longas dos Beatles.png")
    except Exception as error:
        return error


def musicas_mais_curtas_da_banda(dataframe):
    try:
        dataframe = dataframe.reset_index()
        dataframe["duration_sec"]=dataframe["duration_ms"]/1000
        plt.figure(figsize=(12, 6))
        plot = sns.barplot(
        x="song",
        y="duration_sec",
        data=dataframe.sort_values("duration_sec").head(5), # 5 linhas com menor duração
        color="#7BC5FF"
        )
        plot.set(title="Músicas mais Curtas")
        plot.set_xlabel( "Músicas" , size = 12 )
        plot.set_ylabel( "Duração (sec)", size = 12)
        plot.set_ylim(0, 70)
        fig = plot.get_figure()
        fig.savefig("./img/Musicas Mais Curtas dos Beatles.png")
    except Exception as error:
        return error


def albums_mais_premiados_da_banda(dataframe):
    try:
        plt.figure(figsize=(12, 6))
        plot = sns.barplot(
        x="album",
        y="num_awards",
        data=dataframe.sort_values(["num_awards", "num_nominations"], ascending=False).head(5), # 5 linhas com maior numero de premios
        color="#7BC5FF"
        )
        plot.set(title="Albums mais Premiados")
        plot.set_xlabel( "Albums" , size = 12 )
        plot.set_ylabel( "Prêmios", size = 12)
        plot.set_ylim(0, )
        fig = plot.get_figure()
        fig.savefig("./img/Albuns Mais Premiados dos Beatles.png")
    except Exception as error:
        return error


def relacao_popularidade_duração(dataframe):
    try:
        dataframe["duration_sec"]=dataframe["duration_ms"]/1000
        plt.figure(figsize=(8, 8))
        plot = sns.regplot(           # scatterplot com linhha de regressão
        data=dataframe, 
        x = dataframe["duration_sec"], 
        y=dataframe["popularity"], 
        ci = None)                   # linha de regressão normal
        corr = mp.correlacao(dataframe, "duration_ms", "popularity") # correlação
        plot.set(title="Relação Entre Popularidade e Duração da Música")
        plot.set_xlabel(f"Duração (sec)" , size = 12 )
        plot.set_ylabel( "Popularidade", size = 12)
        plt.text(200, 2, f'Correlação:{corr}', fontsize = 10) # texto mostrando a correlação no plot
        plot.set_ylim(0, )
        fig = plot.get_figure()
        fig.savefig("./img/Popularidade x Duração.png")
    except Exception as error:
        return error


def mais_longas_por_album(data):
    try:
        data["duration_sec"]=data["duration_ms"]/1000 # transforma ms em segundos
        albums= data.index.levels[0] # lista com o nome dos albuns em ordem alfabética
        contador = 0                 # para o nome do título e do arquivo ficarem sincronizados
        lista = mp.mais_x_por_album(data, "duration_sec") # lista com um dataframe por album
        for dataframe in lista:
            dataframe = dataframe.reset_index()
            plt.figure(figsize=(12, 6))
            plot = sns.barplot(
            x="song",
            y="duration_sec",
            data=dataframe.sort_values("duration_sec", ascending=False).head(5), # 5 linhas com mais duração
            color="#7BC5FF"
            )
            plot.set(title=f"Músicas mais Longas do {albums[contador]}")
            plot.set_xlabel( "Músicas" , size = 12 )
            plot.set_ylabel( "Duração", size = 12)
            fig = plot.get_figure()
            fig.savefig(f"./img/Mais Longas do {albums[contador]}.png")
        contador+=1
    except Exception as error:
        return error


def mais_curtas_por_album(data):
    try:
        data["duration_sec"]=data["duration_ms"]/1000 # transforma ms em segundos
        albums= data.index.levels[0]
        contador = 0
        lista = mp.mais_x_por_album(data, "duration_sec")
        for dataframe in lista:
            dataframe = dataframe.reset_index()
            plt.figure(figsize=(12, 6))
            plot = sns.barplot(
            x="song",
            y="duration_sec",
            data=dataframe.sort_values("duration_sec").head(5),  # 5 linhas com menos duração
            color="#7BC5FF"
            )
            plot.set(title=f"Músicas mais curtas do {albums[contador]}")
            plot.set_xlabel( "Músicas" , size = 12 )
            plot.set_ylabel( "Duração", size = 12)
            fig = plot.get_figure()
            fig.savefig(f"./img/Mais curtas do {albums[contador]}.png")
            contador+=1
    except Exception as error:
        return error


def mais_populares_por_album(data):
    try:
        albums= data.index.levels[0]
        contador = 0
        lista = mp.mais_x_por_album(data, "popularity")
        for dataframe in lista:
            dataframe = dataframe.reset_index()
            plt.figure(figsize=(12, 6))
            plot = sns.barplot(
            x="song",
            y="popularity",
            data=dataframe.sort_values("popularity", ascending=False).head(5),
            color="#7BC5FF"
            )
            plot.set(title=f"Músicas mais Populares do {albums[contador]}")
            plot.set_xlabel( "Músicas" , size = 12 )
            plot.set_ylabel( "Popularidade", size = 12)
            fig = plot.get_figure()
            fig.savefig(f"./img/Mais Populares do {albums[contador]}.png")
            contador+=1
    except Exception as error:
        return error


def menos_populares_por_album(data):
    try:
        albums= data.index.levels[0]
        contador = 0
        lista = mp.mais_x_por_album(data, "popularity")
        for dataframe in lista:
            dataframe = dataframe.reset_index()
            plt.figure(figsize=(12, 6))
            plot = sns.barplot(
            x="song",
            y="popularity",
            data=dataframe.sort_values("popularity").head(5),
            color="#7BC5FF"
            )
            plot.set(title=f"Músicas menos Populares do {albums[contador]}")
            plot.set_xlabel( "Músicas" , size = 12 )
            plot.set_ylabel( "Popularidade", size = 12)
            fig = plot.get_figure()
            fig.savefig(f"C:/Users/otavi/Desktop/FGV/Python/A1 LP/img/Menos Populares do {albums[contador]}.png")
            contador+=1
    except Exception as error:
        return error