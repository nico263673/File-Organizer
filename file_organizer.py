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

            bilder_count = 0
            pdf_count = 0
            musik_count = 0
            video_count = 0
            textdate_count = 0
            archiv_count = 0



            nochnichtvorhandeneart = []

            nochnichtvorhandeneart_count = 0


            for files in ordner:
                if files.endswith(".jpg") or files.endswith(".jpeg") or files.endswith(".png") or files.endswith(".gif") or files.endswith(".webp"):
                    bilder.append(files)
                    bilder_count += 1
                elif files.endswith(".pdf"):
                    pdfs.append(files)
                    pdf_count += 1
                elif files.endswith(".mp3") or files.endswith(".wav") or files.endswith(".flac"):
                    musik.append(files)
                    musik_count += 1
                elif files.endswith(".mp4") or files.endswith(".mkv") or files.endswith(".mov"):
                    videos.append(files)
                    video_count += 1
                elif files.endswith(".md") or files.endswith(".txt"):
                    textdatein.append(files)
                    textdate_count += 1
                elif files.endswith(".zip") or files.endswith(".rar") or files.endswith(".7z") or files.endswith(".tar") or files.endswith(".gz"):
                    archiv.append(files)
                    archiv_count += 1
                else:
                    nochnichtvorhandeneart.append(files)
                    nochnichtvorhandeneart_count += 1

            datei_anzahl = bilder_count + pdf_count + musik_count + video_count + textdate_count + archiv_count + nochnichtvorhandeneart_count


            print("Deine Bilder datein sind: ")
            for bild in bilder:
                print(bild)
            print(f"das sind {bilder_count} Bilder")
            print(" ")

            print("Deine Pdf datein sind: ")
            for pdfs in pdfs:
                print(pdfs)
            print(f"das sind {pdf_count} Pdfs")

            print("Deine Musik datein sind: ")
            for lied in musik:
                print(lied)
            print(f"das sind {musik_count} Lieder")
            print("")

            print("Deine Video datein sind: ")
            for video in videos:
                print(video)
            print(f"das sind {video_count} videos")
            print(" ")

            print("Deine Text datein sind: ")
            for text in textdatein:
                print(text)
            print(f"das sind {textdate_count} Textdatein")
            print(" ")

            print("Deine Archiv datein sind: ")
            for archivdatein in archiv:
                print(archivdatein)
            print(f"das sind {archiv_count} Archiv datein")
            print(" ")

            print("folgende Datein können wir noch nicht zuordnen: ")
            for unerkennbar in nochnichtvorhandeneart:
                print(unerkennbar)
            print(f"das sind {nochnichtvorhandeneart_count} Datein die wir noch nicht zuordnen können")

            print(f"Du hats insgesamt {datei_anzahl} Datein in diesem ordner")
            while True:
                print("Willst du wissen zu wie viel prozent jeder dateityp in deinem ordner ist?")
                willst_du = input("j/n ").lower()
                if willst_du == "n":
                    break
                elif willst_du == "j":
                    bilder_prozent = bilder_count / len(ordner)
                    pdf_prozent = pdf_count / len(ordner)
                    musik_prozent = musik_count / len(ordner)
                    video_prozent = video_count / len(ordner)
                    textdate_prozent = textdate_count / len(ordner)
                    archiv_prozent = archiv_count / len(ordner)
                    nochnichtvorhandeneart_prozent = nochnichtvorhandeneart_count / len(ordner)

                    print(f"dein ordner besteht zu {bilder_prozent} aus Bildern")
                    print(f"dein ordner besteht zu {pdf_prozent} aus Pdfs")
                    print(f"dein ordner besteht zu {musik_prozent} aus Musik")
                    print(f"dein ordner besteht zu {video_prozent} aus videos")
                    print(f"dein ordner besteht zu {textdate_prozent} aus Text datein")
                    print(f"dein ordner besteht zu {archiv_prozent} aus archiv datein")
                    print(f"dein ordner besteht zu {nochnichtvorhandeneart_prozent} aus Dateien die noch nicht zugeordnet werden können ")
                else:
                    print("du musst eine zahl schreiben")
        break

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
