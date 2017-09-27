#!/usr/bin/python3.5
import os
import time
import datetime
clear = lambda: os.system('clear')
try:
    while True:
        clear()
        dir = "informes/"
        informes = os.listdir(dir)
        if len(informes) > 0:
            print("Informes:")
            contador = 0
            for f in informes:
                print(str(contador) +": " + f)
                contador+=1
            print("")
            print("Indica el id del informe que quieres abrir: ")
        print("Introduce -1 para abrir un informe nuevo. [Ctr+C para salir]")
        try:
            id = int(input())
        except ValueError:
            print("Debes indicar el índice numérico de un informe o -1 para uno nuevo.\nInténtalo de nuevo.\n")
            continue
        clear()
        if id != -1 :
            try:
                informe = informes[id]
                print("Recuperando el informe...\n")
                time.sleep(1)
                print("Informe: "+informe+"\n")
                with open(dir+informe,'r') as f:
                    for line in f:
                        print("· "+line)
                
                print("\n\n¿Quieres continuar el informe? [Y,n]")
                continuar = input()
                if not(continuar == "Y" or continuar == "YES" or continuar == "y" or continuar == "yes"):
                    continue
            except IndexError:
                print("Ese informe no existe.\nInténtalo de nuevo.\n")
                print("\n\nPresiona cualquier tecla para volver a empezar...")
                input()
                continue
        else:
            now = datetime.datetime.now()
            informe = str(now.year)+str('{:02d}'.format(now.month))+ \
            str('{:02d}'.format(now.day))+ \
            str('{:02d}'.format(now.hour))+ \
            str('{:02d}'.format(now.minute))+".info"

        print("¿Quién eres?")
        usuario = input()
        print("Escribe tu comentario:")
        comentario = input()
        f = open(dir+informe,'a')
        f.write(usuario+": "+comentario+"\n")
        f.close()
        print()
        print("***************************************")
        print("*Actualización del informe almacenado.*")
        print("***************************************")
        print("\n\nPresiona cualquier tecla para volver a empezar...")
        input()
except KeyboardInterrupt:
    print("\n\nBye  :)\n")