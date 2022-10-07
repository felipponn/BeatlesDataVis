import re
from modulo import *
import modulo.modulo_grupo_perguntas_2 as mgp
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def palavras_frequentes_albuns(dataframe):
    """Esta função cria duas Tag Clouds com as palavras mais frequentes nos títulos
    dos álbuns do dataframe. A primeira, mais simples, e a segunda, com uma outra 
    formatação (palavras com tamanhos diferentes).

    Arg:
        dataframe (pd.Dataframe): Base de dados da banda de música trabalhada

    Return:
        wordcloud.WordCloud: Plota e mostra duas Tag Clouds
    """
    
    try:
        texto = mgp.palavras_comuns_albuns(dataframe) # output da função do modulo_grupo_perguntas_2
        novo_texto = ''
        for tupla in texto: # Pega apenas as strings na lista da variável texto
            novo_texto += tupla[0]
            novo_texto += ' '
        palavras = re.sub(r"[^a-zA-Z0-9 ]", "", novo_texto) # Elimina aspas simples
        wordcloud = WordCloud().generate(str(palavras)) # Gera a Tag Cloud com as palavras
        plt.imshow(wordcloud, interpolation='bilinear') # Plota a imagem
        plt.axis("off") # Eixo da Tag Cloud
        wordcloud = WordCloud(max_font_size=40).generate(palavras) # Gera uma outra Tag Cloud com formato diferente
        plt.figure() # Plota a figura
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show() # Mostra a Tag Cloud final
        wordcloud.to_file("Tag_Cloud1.png") # Salva a figura
    except Exception as error:
            return error

def palavras_frequentes_musicas(dataframe):
    """Esta função cria duas Tag Clouds com as palavras mais frequentes nos títulos 
    das músicas do dataframe. A primeira, mais simples, e a segunda, com uma outra 
    formatação (palavras com tamanhos diferentes).

    Arg:
        dataframe (pd.Dataframe): Base de dados da banda de música trabalhada

    Return:
        wordcloud.WordCloud: Plota e mostra duas Tag Clouds
    """
    
    try:
        texto = mgp.palavras_comuns_musicas(dataframe) # output da função do modulo_grupo_perguntas_2
        novo_texto = ''
        for tupla in texto: # Pega apenas as strings na lista da variável texto
            novo_texto += tupla[0]
            novo_texto += ' '
        palavras = re.sub(r"[^a-zA-Z0-9 ]", "", novo_texto) # Elimina aspas simples
        wordcloud = WordCloud().generate(str(palavras)) # Gera a Tag Cloud com as palavras
        plt.imshow(wordcloud, interpolation='bilinear') # Plota a imagem
        plt.axis("off") # Eixo da Tag Cloud
        wordcloud = WordCloud(max_font_size=40).generate(palavras) # Gera uma outra Tag Cloud com formato diferente
        plt.figure() # Plota a figura
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show() # Mostra a Tag Cloud final
        wordcloud.to_file("Tag_Cloud2.png") # Salva a figura
    except Exception as error:
            return error

def palavras_frequentes_discografia(dataframe):
    """Esta função cria duas Tag Clouds com as palavras mais comuns nas letras das músicas 
    do dataframe. A primeira, mais simples, e a segunda, com uma outra formatação
    (palavras com tamanhos diferentes).

    Arg:
        dataframe (pd.Dataframe): Base de dados da banda de música trabalhada

    Return:
        wordcloud.WordCloud: Plota e mostra duas Tag Clouds
    """
    
    try:
        texto = mgp.palavras_comuns_letras_disco(dataframe) # output da função do modulo_grupo_perguntas_2
        novo_texto = ''
        for tupla in texto: # Pega apenas as strings na lista da variável texto
            novo_texto += tupla[0]
            novo_texto += ' '
        palavras = re.sub(r"[^a-zA-Z0-9 ]", "", novo_texto) # Elimina aspas simples
        wordcloud = WordCloud().generate(str(palavras)) # Gera a Tag Cloud com as palavras
        plt.imshow(wordcloud, interpolation='bilinear') # Plota a imagem
        plt.axis("off") # Eixo da Tag Cloud
        wordcloud = WordCloud(max_font_size=40).generate(palavras) # Gera uma outra Tag Cloud com formato diferente
        plt.figure() # Plota a figura
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show() # Mostra a Tag Cloud final
        wordcloud.to_file("Tag_Cloud3.png") # Salva a figura
    except Exception as error:
            return error