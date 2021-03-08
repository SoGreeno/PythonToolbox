# działa, ale nie jestem pewien czy zapisuje tekst..
import time
editingnow = input("Wybierz nazwę pliku w folderze:")
plik = open(editingnow, "w")
print("TextEditor v1.0")
plik.write( input("& "))
print("Zapisywanie...")
time.sleep(1)
