import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import chaves

def parser(nome):
    lista = ['', '']
    item = 0
    for i in range(len(nome)):
        if nome[i] in '()':
            item += 1
            continue
        lista[item] += nome[i]
    lista[0] = lista[0][:-1]
    return lista[0], lista[1]

df1 = pd.read_csv("BeatlesDB.csv", sep='|')
df2 = pd.read_csv("Letras.csv", sep="|", encoding="macintosh")

lista_albuns = ["Please Please Me", "With The Beatles", "A Hard Day's Night", "Beatles for Sale", "Help!", "Rubber Soul", "Revolver", "Sgt. Pepper's Lonely Hearts Club Band", "Magical Mystery Tour", "The Beatles (white album)", "Yellow Submarine", "Abbey Road", "Let It Be"]

df2_mask = df2["album"].isin(lista_albuns)
df2 = df2[df2_mask]
df2 = df2.rename(columns={"title":"song"})
df2 = df2.drop(columns=["year"])

beatles = df1.merge(df2, left_on=("song", "album"), right_on=("song", "album"))

beatles_uri = 'spotify:artist:3WrFJ7ztbogyGnTHbHJFl2'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=chaves.CLIENT, client_secret=chaves.SECRET))

results = spotify.artist_albums(beatles_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

lista_albuns = ["Please Please Me", "With The Beatles", "A Hard Day's Night", "Beatles For Sale", "Help!", "Rubber Soul", "Revolver", "Sgt. Pepper's Lonely Hearts Club Band", "Magical Mystery Tour", "The Beatles", "Yellow Submarine", "Abbey Road", "Let It Be"]

info = []

for album in albums:
    nome, versao = parser(album['name'])
    if nome in lista_albuns and versao == "Remastered":
        for msc in spotify.album_tracks(album["id"])["items"]:
            album_nome = nome
            if album_nome == "Beatles For Sale":
                album_nome = "Beatles for Sale"
            if album_nome == "The Beatles":
                album_nome = "The Beatles (white album)"
            msc_nome = msc["name"]
            msc_nome = re.sub(" - Remastered 2009", "", msc_nome)
            msc_nome = re.sub(" - Medley / Remastered 2009", "", msc_nome)
            msc_nome = re.sub("- Reprise / Remastered 2009", "(Reprise)", msc_nome)
            msc_nome = re.sub("Mister", "Mr.", msc_nome)
            msc_nome = re.sub("Mr ", "Mr. ", msc_nome)
            msc_nome = re.sub("Sixty ", "Sixty-", msc_nome)
            if msc_nome == "Kansas City / Hey-Hey-Hey-Hey":
                msc_nome = "Kansas City / Hey-Hey-Hey-Hey!"
            popularity = spotify.track(msc["id"])["popularity"]
            info.append([album_nome, msc_nome, popularity])

popDF = pd.DataFrame(info)
popDF = popDF.drop(columns=["Unnamed: 0"])
popDF = popDF.rename(columns={"0":"album", "1":"song", "2":"popularity"})

beatles['song_lower'] = beatles["song"].str.lower()
popDF['song_lower'] = popDF["song"].str.lower()

beatles = beatles.merge(popDF, left_on=("song_lower", "album"), right_on=("song_lower", "album"))
beatles = beatles.rename(columns={"song_x":"song"})
beatles = beatles.drop(columns=["song_y", "song_lower"])
beatles = beatles.set_index(['album', 'song'])
beatles.to_pickle('beatlesDF.pkl')
