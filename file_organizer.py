#benutzer nennt ein ordner
#programm liest alle datein im ordner
#programm erkennt dateityp
#beispiel bilder.jpg ausgabe die datei ist ein bild

#wichtig
#os
#os.listdir("name datei")
#os.path.exists()
#ordner erstellen = os.mkdir("name ordner")
#shutil.move("name date", "name ordner")

import os


def version1():
    while True:
        eingabe = input("Bitte geben sie den Namen des ordners an den sie durchsucht haben wollen: ")
        print(" ")

        if not os.path.exists(eingabe):
            print("Ordner nicht gefunden nicht gefunden.")

        elif os.path.exists(eingabe):
            ordner = os.listdir(eingabe)

            bilder = []
            pdfs = []
            musik = []
            videos = []
            textdatein = []
            archiv = []

            nochnichtvorhandeneart = [0]

            for files in ordner:
                if files.endswith(".jpg") or files.endswith(".jpeg") or files.endswith(".png") or files.endswith(".gif") or files.endswith(".webp"):
                    bilder.append(files)
                elif files.endswith(".pdf"):
                    pdfs.append(files)
                elif files.endswith(".mp3") or files.endswith(".wav") or files.endswith(".flac"):
                    musik.append(files)
                elif files.endswith(".mp4") or files.endswith(".mkv") or files.endswith(".mov"):
                    videos.append(files)
                elif files.endswith(".md") or files.endswith(".txt"):
                    textdatein.append(files)
                elif files.endswith(".zip") or files.endswith(".rar") or files.endswith(".7z") or files.endswith(".tar") or files.endswith(".gz"):
                    archiv.append(files)
                else:
                    nochnichtvorhandeneart.append(files)

            print("Deine Bilder datein sind: ")
            for bild in bilder:
                print(bild)
            print(" ")

            print("Deine Musik datein sind: ")
            for lied in musik:
                print(lied)
            print("")

            print("Deine Video datein sind: ")
            for video in videos:
                print(video)
            print(" ")

            print("Deine Text datein sind: ")
            for text in textdatein:
                print(text)
            print(" ")

            print("Deine Archiv datein sind: ")
            for archivdatein in archiv:
                print(archivdatein)
            print(" ")

            print("folgende Datein können wir noch nicht zuordnen: ")
            for unerkennbar in nochnichtvorhandeneart:
                print(unerkennbar)

            break
        return 0

def main():
    print("Wilkommen in meinem Daten Organizierer ")

    print("Willst du")
    print("1. wissen was für datein in deinem ordner sind")
    print("4. das programm verlassen")

    while True:
        try:
            auswahl = int(input("bitte waehle aus den zahlen oben bitte beachte das du nur mit der zahl antworten sollst"))

            if auswahl == 1:
                version1()
                break
            #elif auswahl == 2:
                #version2()
                #brea
            #elif auswahl == 3:
                #version3()
                #break
            elif auswahl == 4:
                break
            else:
                print("du darfst nur mit einer der zur verfuegung stehenden zahlen antworten")
        except ValueError:
            print("du musst mit einer Zahl antworten")


    print("Bye")

main()
