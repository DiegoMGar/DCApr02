## Diego Maroto
### DCA - 2017/18
#### Práctica 2 - bugtracking
*[DCA pr2 repo Diego Maroto](https://github.com/DiegoMGar/DCApr02)*

Aplicación en python que simula, a un nivel muy simple y por consola, un sistema de tracking de bugs en el que los clientes se comunican con desarrolladores.

La persistencia se mantiene en ficheros de texto en la carpeta informes, cuyo nombre es la concatenación de año, mes, día, hora y minuto en el que el fichero se creó, con la extensión `.info`

Se ha añadido los *.info al gitignore para que sólo quede trackeado uno de ejemplo, no tiene sentido tener los informes en el control de versiones, para eso se debería tener una copia de seguridad.

##### Ejecución:
```
./app.py
```

##### Dependencias:
- python 3.5
- bash (`clear`)