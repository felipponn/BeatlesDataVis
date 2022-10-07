import re
from modulo import *
import modulo.modulo_grupo_perguntas_2 as mgp
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def palavras_frequentes_albuns(dataframe): 
    try:
        texto = mgp.palavras_comuns_albuns(dataframe) 
        novo_texto = ''
        for tupla in texto:
            novo_texto += tupla[0]
            novo_texto += ' '
        palavras = re.sub(r"[^a-zA-Z0-9 ]", "", novo_texto)
        wordcloud = WordCloud().generate(str(palavras))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        wordcloud = WordCloud(max_font_size=40).generate(palavras)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        wordcloud.to_file("Tag_Cloud1.png")
    except Exception as error:
            return error

def palavras_frequentes_musicas(dataframe):
    try:
        texto = mgp.palavras_comuns_musicas(dataframe)
        novo_texto = ''
        for tupla in texto:
            novo_texto += tupla[0]
            novo_texto += ' '
        palavras = re.sub(r"[^a-zA-Z0-9 ]", "", novo_texto)
        wordcloud = WordCloud().generate(str(palavras))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        wordcloud = WordCloud(max_font_size=40).generate(palavras)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        wordcloud.to_file("Tag_Cloud2.png")
    except Exception as error:
            return error

def palavras_frequentes_discografia(dataframe):
    try:
        texto = mgp.palavras_comuns_letras_disco(dataframe)
        novo_texto = ''
        for tupla in texto:
            novo_texto += tupla[0]
            novo_texto += ' '
        palavras = re.sub(r"[^a-zA-Z0-9 ]", "", novo_texto)
        wordcloud = WordCloud().generate(str(palavras))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        wordcloud = WordCloud(max_font_size=40).generate(palavras)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        wordcloud.to_file("Tag_Cloud3.png")
    except Exception as error:
            return error