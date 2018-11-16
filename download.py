from pytube import Playlist
import os
print("\n" *100)
os.system("cls")
print("Pega el link de la lista de reproducción y presiona ENTER")
lista = str(input())

convertir = False

while True:
    print("Deseas convertir los videos a MP3? (s/n)")
    c = str(input())
    if c == "s":
        convertir=True
        break
    elif c=="n":
        convertir=False
        break
    else:
        print("Respuesta no reconocida")


pl = Playlist(lista)

directorioVideos = "videos"

try: 
	os.mkdir(directorioVideos)
except:
	print("No se pudo crear el directorio, presiona una tecla para salir")
	input()
	exit()

pl.download_all(os.getcwd() + "\\" + directorioVideos)

if convertir==True:
    pass
else:
    print("Proceso terminado, presiona una tecla para salir")
    input()
    exit()


#Convertir en mp3

import moviepy.editor as mp
import os
import imageio

imageio.plugins.ffmpeg.download()

try:
    os.mkdir("audio")
except:
    print("No se pudo crear el directorio '/audio'")
path = os.getcwd() + "\\videos"
outPath = os.getcwd() + "\\audio"
os.chdir("./audio")

files = os.listdir(path)
for name in files:
    clip = mp.VideoFileClip(path + "\\" + name)
    clip.audio.write_audiofile(name + ".mp3")
    clip.reader.close()

print("Proceso terminado, presiona una tecla para salir")
input()
exit()