#!/usr/bin/python3.5
#json.loads : str to obj
#json.dumps : obj to str
import os
import time
import datetime
import json
clear = lambda: os.system('clear')
try:
    print("Login:")
    usuario = input()
    while True:
        clear()
        print("Bienvenido "+usuario+"\n")
        dir = "proyectos/"
        proyectos = os.listdir(dir)
        if len(proyectos) > 0:
            print("Proyectos:")
            contador = 0
            for f in proyectos:
                print(str(contador) +": " + f)
                contador+=1
            print("")
            print("Indica el id del proyecto que quieres abrir: ")
        print("Introduce -1 para abrir un proyecto nuevo. [Ctr+C para salir]")
        try:
            id = int(input())
        except ValueError:
            print("Debes indicar el índice numérico de un proyecto o -1 para uno nuevo.")
            print("\n\nPresiona cualquier tecla para volver a empezar.")
            input()
            continue
        clear()
        if id != -1 :
            try:
                proyecto = proyectos[id]
            except IndexError:
                print("Ese proyecto no existe.")
                print("\n\nPresiona cualquier tecla para volver a empezar.")
                input()
                continue
            try:
                while True:
                    clear()
                    print("Recuperando el proyecto...\n")
                    time.sleep(1)
                    informes = os.listdir(dir+proyecto)
                    if len(informes) > 0:
                        print("Informes:")
                        contador = 0
                        for informe in informes:
                            print(str(contador)+": "+informe)
                            contador+=1
                        print("")
                        print("Indica el id del informe que quieres abrir: ")
                    else:
                        print("No hay informes.")
                    print("Introduce -1 para abrir un informe nuevo. [Ctr+C para salir]")
                    try:
                        id = int(input())
                    except ValueError:
                        print("Debes indicar el índice numérico de un informe o -1 para uno nuevo.")
                        print("\n\nPresiona cualquier tecla para volver a empezar.")
                        input()
                        continue
                    if id != -1 :
                        try:
                            informe = informes[id]
                        except IndexError:
                            print("Ese informe no existe.")
                            print("\n\nPresiona cualquier tecla para volver a empezar.")
                            input()
                            continue
                        print("Informe: "+informe+"\n")
                        f = open(dir+proyecto+"/"+informe,'r')
                        line = f.read()
                        try:
                            obj = json.loads(line)
                        except json.decoder.JSONDecodeError:
                            print("El fichero está corrupto, no se puede leer el JSON.")
                            print("\n\nPresiona cualquier tecla para volver a empezar.")
                            input()
                            continue
                        print("Título: "+obj['titulo']+"\n")
                        print("Gravedad: "+obj['urgencia']+"\n")
                        for comentario in obj['comentarios']:
                            print("· "+comentario)
                        print("--------\nEstado: "+obj["estado"])
                        print("\n\n¿Quieres continuar el informe? [Y,n,cerrar]")
                        continuar = input()
                        if continuar == "cerrar":
                            obj['estado']='cerrado'  
                        elif not(continuar == "Y" or continuar == "YES" or continuar == "y" or continuar == "yes"):
                            continue
                    else:
                        now = datetime.datetime.now()
                        informe = str(now.year)+str('{:02d}'.format(now.month))+ \
                        str('{:02d}'.format(now.day))+ \
                        str('{:02d}'.format(now.hour))+ \
                        str('{:02d}'.format(now.minute))+".info"
                        obj={}
                        obj['usuario']=usuario
                        obj['estado']='abierto'
                        obj['comentarios']=[]
                        print("Título de la incidencia:")
                        obj['titulo'] = input()
                        print("Elije el nivel de urgencia:\n\t0: poca, 1: media, 2: alta")
                        try:
                            urgencia=int(input())
                            if urgencia>2 or urgencia<0:
                                raise ValueError
                            obj['urgencia']=str(urgencia)
                        except ValueError:
                            print("Debes elegir el identificador de una de las urgencias sugeridas.")
                            print("\n\nPresiona cualquier tecla para volver a empezar.")
                            input()
                            continue
                    print("Escribe tu comentario:")
                    comentario = input()
                    f = open(dir+proyecto+"/"+informe,'w')
                    now = datetime.datetime.now()
                    obj['comentarios'].append(usuario+" ["+\
                        str(now.year)+str('{:02d}'.format(now.month))+"-"+ \
                        str('{:02d}'.format(now.day))+" "+ \
                        str('{:02d}'.format(now.hour))+":"+ \
                        str('{:02d}'.format(now.minute))+"]: "+comentario)
                    f.write(json.dumps(obj, sort_keys=True,indent=2, separators=(',', ':')))
                    f.close()
                    print()
                    print("***************************************")
                    print("*Actualización del informe almacenado.*")
                    print("***************************************")
                    print("\n\nPresiona cualquier tecla para volver a empezar.")
                    input()
            except KeyboardInterrupt:
                continue
        else:
            print("Da nombre al proyecto:")
            proyecto = input()
            if os.path.exists(dir+proyecto):
                print("El proyecto ya existe.")
                print("\n\nPresiona cualquier tecla para volver a empezar.")
                input()
            else:
                os.makedirs(dir+proyecto) 
        print()
        print("***************************************")
        print("*Nuevo proyecto creado.*")
        print("***************************************")
        print("\n\nPresiona cualquier tecla para volver a empezar.")
        input()
except KeyboardInterrupt:
    print("\n\nNos vemos :)\n")