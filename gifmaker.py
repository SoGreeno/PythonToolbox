# może nie działać
# a i pamiętaj. zeby plik był w mp4 i zeby był poniżej 30 minut długi
from moviepy.editor import *
	print("GifMaker")
clip = VideoFileClip( input("Wpisz nazwę pliku w folderze:")
print("Czy jesteś pewnien żeby zrobić plik GIF (0 - Nie | 1 - Tak")
a = input("& ")
if a == 1:
    clip.write_gif("gifmaker.gif")
    
    else:
        print("anulowano")

if a == 0:
    print("anulowano")
    
    else:
    print("anulowano")
