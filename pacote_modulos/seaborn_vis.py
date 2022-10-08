from pacote_modulos import modulo_grupo_perguntas_1 as mp
import seaborn as sns
import pandas as pd
import matplotlib.pylab as plt

def musicas_mais_populares_da_banda(dataframe):
    """Salva o Plot das musicas mais populares da banda

    :param dataframe: Dataframe com musicas da banda
    :type dataframe: pandas dataframe
    """
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
        fig.savefig("img/Musicas Mais Populares dos Beatles.png")  # salva a figura
        plt.close()
    except Exception as error:
        return error


def musicas_menos_populares_da_banda(dataframe):
    """Salva o Plot das musicas menos populares da banda

    :param dataframe: Dataframe com musicas da banda
    :type dataframe: pandas dataframe
    """
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
        fig.savefig("img/Musicas Menos Populares dos Beatles.png")
        plt.close()
    except Exception as error:
        return error


def musicas_mais_longas_da_banda(dataframe):
    """Salva o Plot das musicas mais longas da banda

    :param dataframe: Dataframe com musicas da banda
    :type dataframe: pandas dataframe
    """
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
        fig.savefig("img/Musicas Mais Longas dos Beatles.png")
        plt.close()
    except Exception as error:
        return error


def musicas_mais_curtas_da_banda(dataframe):
    """Salva o Plot das musicas mais curtas da banda

    :param dataframe: Dataframe com musicas da banda
    :type dataframe: pandas dataframe
    """
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
        fig.savefig("img/Musicas Mais Curtas dos Beatles.png")
        plt.close()
    except Exception as error:
        return error


def albums_mais_premiados_da_banda(dataframe):
    """Salva o plot dos albuns mais premiados da banda

    :param dataframe: Dataframe com musicas da banda
    :type dataframe: pandas dataframe
    """
    try:
        dataframe["num_awards"] = [len(x.split(",")) if x != '[]' else 0 for x in dataframe["awards"]] # conta quantas premios tem um album
        dataframe["num_nominations"] = [len(x.split(",")) if x != '[]' else 0 for x in dataframe["nominations"]] # conta quantas nomeações tem um album
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
        fig.savefig("img/Albuns Mais Premiados dos Beatles.png")
        plt.close()
    except Exception as error:
        return error


def relacao_popularidade_duração(dataframe):
    """Salva o plot da relação de popularidade e duração 

    :param dataframe: Dataframe com musicas da banda
    :type dataframe: pandas dataframe
    """
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
        fig.savefig("img/Popularidade x Duração.png")
        plt.close()
    except Exception as error:
        return error


def mais_longas_por_album(data):
    """Salva os plots das musicas mais longas por album

    :param data: Dataframe com musicas da banda
    :type data: pandas dataframe
    """
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
            fig.savefig(f"img/Mais Longas do {albums[contador]}.png")
            plt.close()
            contador+=1
    except Exception as error:
        return error


def mais_curtas_por_album(data):
    """Salva os plots das musicas mais curtas por album

    :param data: Dataframe com musicas da banda
    :type data: pandas dataframe
    """
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
            fig.savefig(f"img/Mais curtas do {albums[contador]}.png")
            plt.close()
            contador+=1
    except Exception as error:
        return error


def mais_populares_por_album(data):
    """Salva os plots das musicas mais populares por album

    :param data: Dataframe com musicas da banda
    :type data: pandas dataframe
    """
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
            fig.savefig(f"img/Mais Populares do {albums[contador]}.png")
            plt.close()
            contador+=1
    except Exception as error:
        return error


def menos_populares_por_album(data):
    """Salva os plots das musicas menos populares por album

    :param data: Dataframe com musicas da banda
    :type data: pandas dataframe
    """
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
            fig.savefig(f"img/Menos Populares do {albums[contador]}.png")
            plt.close()
            contador+=1
    except Exception as error:
        return error


def plot_participacao_album(dataframe):
    """Salva o lineplot da participação pelos albuns da banda

    :param data: Dataframe com as músicas
    :type data: pandas dataframe
    """
    try:
        plt.figure(figsize=(12, 6))         # cria a janela do gráfico
        plot = sns.lineplot(data=dataframe, # lineplot
        y="participacao", 
        x="album", 
        hue="membro", 
        hue_order=["Lennon", "McCartney", "Harrison", "Starr"]) # ordem das linhas
        plot.set(title="Média de Participação por Álbum")
        plot.set_xlabel( "Album" , size = 12 )
        plot.set_ylabel( "Média Vocal", size = 12)
        plot.set_ylim(0, )
        plt.xticks(rotation=90) # gira o nome dos albuns em 90 graus
        plt.tight_layout() #deixa todos os textos na janela
        fig = plot.get_figure()
        fig.savefig("img/participação_album.png")
        plt.close()
    except Exception as error:
        return error
    

def plotar_media_popularidade_vocal(data):
    """Salva o plot da media popularidade pelos vocalistas da banda

    :param data: Dataframe com as músicas
    :type data: pandas dataframe
    """
    try:
        plt.figure(figsize=(12, 6))         # cria a janela do gráfico
        plot = sns.barplot(
        data=data, 
        y="Popularidade Média", 
        x=data["Vocalista"].head(5),
        color="#7BC5FF")
        plot.set(title="Média de Popularidade por vocalista")
        plot.set_xlabel( "Vocalista" , size = 12 )
        plot.set_ylabel( "Média de Popularidade", size = 12)
        plot.set_ylim(0, )
        fig = plot.get_figure()
        fig.savefig("img/popularidade_vocalista.png")
        plt.close()
    except Exception as error:
        return error

def plotar_media_popularidade_compositor(data):
    """Salva o plot da media popularidade pelos compositores

    :param data: Dataframe com as músicas
    :type data: pandas dataframe
    """
    try:
        plt.figure(figsize=(12, 6))         # cria a janela do gráfico
        plot = sns.barplot(
        data=data, 
        y="Popularidade Média", 
        x=data["Compositor"].head(5),
        color="#7BC5FF")
        plot.set(title="Média de Popularidade por compositor")
        plot.set_xlabel( "Compositor" , size = 12 )
        plot.set_ylabel( "Média de Popularidade", size = 12)
        plot.set_ylim(0, )
        fig = plot.get_figure()
        fig.savefig("img/popularidade_compositor.png")
        plt.close()
    except Exception as error:
        return error
    
def verborragia_album(dataframe):
    """Salva o plot da verborragia media por album

    :param data: Dataframe com as músicas
    :type data: pandas dataframe
    """
    try:
        plt.figure(figsize=(12, 6))
        plot = sns.lineplot(
        data=dataframe, 
        y="Média de Palavras/seg", 
        x="Álbum")
        plot.set(title="Verborragia por Album")
        plot.set_xlabel( "Album" , size = 12 )
        plot.set_ylabel( "Palavras por segundo", size = 12)
        plot.set_ylim(0, )
        plt.xticks(rotation=90)
        plt.tight_layout()
        fig = plot.get_figure()
        fig.savefig("img/verborragia_album.png")
        plt.close()
    except Exception as error:
        return error