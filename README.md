## Diego Maroto
### DCA - 2017/18
#### Práctica 2 - bugtracking
*[DCA pr2 repo Diego Maroto](https://github.com/DiegoMGar/DCApr02)*

Aplicación en python que simula, a un nivel muy simple y por consola, un sistema de tracking de bugs en el que los clientes se comunican con desarrolladores.

La persistencia se mantiene en ficheros de texto en la carpeta proyectos, cuyo nombre es la concatenación de año, mes, día, hora y minuto en el que el fichero se creó, con la extensión `.info`.
Tiene formato `json` tal que:

```
{
  "comentarios":[
    "Cliente01 [201709-27 20:50]: Cuando intento conectarme por ftps...",
    "Developer01 [201709-27 20:54]: Probablemente sea porque tienes ...",
    "Cliente01 [201709-27 20:56]: Es verdad, vaya fallo ..."
  ],
  "estado":"cerrado",
  "titulo":"No funciona el FTPS",
  "urgencia":"2",
  "usuario":"Cliente01"
}
```

Se ha añadido los *.info al gitignore para que sólo quede trackeado uno de ejemplo, no tiene sentido tener los informes en el control de versiones, para eso se debería tener una copia de seguridad.

**El proyecto permite:**
- Logarse (falso).
- Crear y listar proyectos.
- Crear y listar informes relacionados con proyectos.
- Ver detalle de un informe.
- Añadir un comentario al informe, vinculado a tu nombre de usuario del login.
- Elegir el nivel de urgencia del proyecto, del 0 al 3.
- Cambiar el estado del informe a `cerrado`.


#### Ejecución:
```
./app.py
```

#### Dependencias:
- python 3.5
- bash (`clear`)