from modulo import *
from pacote_modulos import *
from seaborn_plots import seaborn_vis
from wordcloud_plots import wordcloud_vis

beatlesDF = dataset.beatlesDF
premiosDF = dataset.premiosDF


# Grupo de Perguntas 1

# mais longas e curtas
print("Músicas mais longas dos Beatles\n", modulo_grupo_perguntas_1.mais_x_da_banda(beatlesDF, "duration_ms").head(3),"\n\n", 
      "Músicas mais curtas dos Beatles\n", modulo_grupo_perguntas_1.mais_x_da_banda(beatlesDF, "duration_ms").tail(3).sort_values(), "\n\n\n")

# plot das mais longas e mais curtas
seaborn_vis.musicas_mais_longas_da_banda(beatlesDF)
seaborn_vis.musicas_mais_curtas_da_banda(beatlesDF)


# mais e menos populares
print("Músicas mais populares dos Beatles\n", modulo_grupo_perguntas_1.mais_x_da_banda(beatlesDF, "popularity").head(3),"\n\n", 
      "Músicas menos populares dos Beatles\n", modulo_grupo_perguntas_1.mais_x_da_banda(beatlesDF, "popularity").tail(3).sort_values(), "\n\n\n")

# plot das mais populares e das menos populares
seaborn_vis.musicas_mais_populares_da_banda(beatlesDF)
seaborn_vis.musicas_menos_populares_da_banda(beatlesDF)


# mais longas e mais curtas por album
albums= beatlesDF.index.levels[0]
contador=0
for i in modulo_grupo_perguntas_1.mais_x_por_album(beatlesDF, "duration_ms"):
    print(f"Músicas mais longas do {albums[contador]}\n", i.head(3),"\n\n", 
      f"Músicas mais curtas do {albums[contador]}\n", i.tail(3).sort_values(),"\n\n")
    contador+=1
print("\n")

# plot das mais longas e mais curtas por album
seaborn_vis.mais_longas_por_album(beatlesDF)
seaborn_vis.mais_curtas_por_album(beatlesDF)


# mais populares e menos populares por album
albums= beatlesDF.index.levels[0]
contador=0
for i in modulo_grupo_perguntas_1.mais_x_por_album(beatlesDF, "popularity"):
    print(f"Músicas mais populares do {albums[contador]}\n", i.head(3),"\n\n", 
      f"Músicas menos populares do {albums[contador]}\n", i.tail(3).sort_values(),"\n\n")
    contador+=1
print("\n")

seaborn_vis.mais_populares_por_album(beatlesDF)
seaborn_vis.menos_populares_por_album(beatlesDF)


# albuns mais premiados
print("Albuns mais premiados\n\n", modulo_grupo_perguntas_1.mais_premiados_album(premiosDF, "num_awards"), "\n\n\n")

seaborn_vis.albums_mais_premiados_da_banda(premiosDF)


# relação entre popularidade e duração
print("correlação entre popularidade e duração", modulo_grupo_perguntas_1.correlacao(beatlesDF, "duration_ms", "popularity"), "\n\n\n")

seaborn_vis.relacao_popularidade_duração(beatlesDF)

# Grupo de Perguntas 2

print("Palavras Mais Comuns nos Títulos dos Albuns", "\n",
modulo_grupo_perguntas_2.palavras_comuns_albuns(beatlesDF), "\n\n\n")

print("Palavras Mais Comuns nos Títulos das Músicas", "\n",
modulo_grupo_perguntas_2.palavras_comuns_musicas(beatlesDF), "\n\n\n")


print("Palavras Mais Comuns na Letra das Músicas da Banda", "\n",
modulo_grupo_perguntas_2.palavras_comuns_letras_disco(beatlesDF), "\n\n\n")

print("Palavras Mais Comuns na Letra das Músicas por Álbum", "\n",
modulo_grupo_perguntas_2.palavras_comuns_letras_albuns(beatlesDF), "\n\n\n")

print("Frequência do título do Álbum na Letra das Músicas", "\n",
modulo_grupo_perguntas_2.titulo_album_letras(beatlesDF), "\n\n\n")

print("Frequência do título das Músicas na Letra das Músicas", "\n",
modulo_grupo_perguntas_2.titulo_musica_letras(beatlesDF), "\n\n\n")

wordcloud_vis.palavras_frequentes_albuns(beatlesDF)
wordcloud_vis.palavras_frequentes_musicas(beatlesDF)
wordcloud_vis.palavras_frequentes_discografia(beatlesDF)

# Grupo de Perguntas 3

print("Popularidade média dos compositores", "\n",
modulo_grupo_perguntas_3.media_popularidade_compositor(beatlesDF), "\n\n\n")

seaborn_vis.plotar_media_popularidade_compositor(modulo_grupo_perguntas_3.media_popularidade_compositor(beatlesDF))

print("Popularidade média dos vocalistas", "\n",
modulo_grupo_perguntas_3.media_popularidade_vocal(beatlesDF), "\n\n\n")

seaborn_vis.plotar_media_popularidade_vocal(modulo_grupo_perguntas_3.media_popularidade_vocal(beatlesDF))

print("Participação vocal de cada membro por Álbum", "\n",
modulo_grupo_perguntas_3.porcentagem_participacao_album(beatlesDF), "\n\n\n")

seaborn_vis.plot_participacao_vocal_album(modulo_grupo_perguntas_3.porcentagem_participacao_album(beatlesDF))

print("Palavras médias por segundo por Álbum", "\n",
modulo_grupo_perguntas_3.verborragia(beatlesDF))

seaborn_vis.verborragia_album(modulo_grupo_perguntas_3.verborragia(beatlesDF))
