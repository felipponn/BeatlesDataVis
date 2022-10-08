from modulo import *
from modulo.modulo_grupo_perguntas_2 import palavras_comuns_albuns, palavras_comuns_letras_albuns, palavras_comuns_letras_disco, palavras_comuns_musicas, titulo_album_letras, titulo_musica_letras
from pacote_modulos import *

df = dataset.beatlesDF

print(titulo_musica_letras(df))