# Bienvenido al Manual de Usuario
IPCMusic es un reproductor de música basado en el lenguaje de programación Python, su funcionamiento se basa en listas enlazadas que almacenan la información de los objetos necesarios para la creación de una biblioteca que almacenará el contenido de un archivo xml con la información de la música que contenga una persona en su computadora esto con el objetivo de que un usuario pueda escuchar su música de una forma más fácil y generar sus propias listas si así lo desea. 

El usuario podrá generar reportes si así lo desea para poder tener una mejor vista de su música, un reporte creado por el programa graphvis que generará una imagen para visualizar la manera en la que las listas se relacionan y un archivo con formato dot que contendrá toda la información del archivo xml. 

## Inicio Rápido
La interfaz de MP3music se divide en dos secciones principales: la barra de herramientas y el área de reproducción.
- ***Herramientas:*** 

  * **Cargarr XML:** Carga la lista de reproducción aa la app para poder mostrar los datos.
  * **Exportar Graphviz:** Exporta la lista de reproducción actual a un archivo Graphviz.
  * **Exportar HTML:** Exporta la lista de reproducción actual a un archivo HTML.
  * **Modo normal:** Reproduce la lista de reproducción actual en modo normal.
  * **Modo aleatorio:** Reproduce la lista de reproducción actual en modo aleatorio.
  * **Play:** Reproduce la canción seleccionada.
  * **Reproducir/pausar:** Pausa o reanuda la reproducción de la música.
  * **Siguiente:** Avanza a la siguiente canción de la lista de reproducción.
  * **Anterior:** Retrocede a la canción anterior de la lista de reproducción.

- ***Área de reproducción:***
El área de reproducción muestra la información sobre la canción que se está reproduciendo actualmente. Incluye el título de la canción, el artista, el álbum y la imagen de la cancion.

MP3music ofrece las siguientes opciones para gestionar listas de reproducción:
- Agregar lista: Agrega una nueva lista de reproducción.
- Crear nueva: Crea una nueva lista de reproducción a partir de la lista de reproducción actual.
- Agregar canciones a lista: Agrega canciones a una lista de reproducción existente.
- Limpiar lista: Elimina todas las canciones de una lista de reproducción.
- Reproducir lista: Reproduce la lista de reproducción seleccionada.
- Reproducir canción: Reproduce la canción seleccionada.
Salir: Cierra la aplicación.

MP3music también incluye un combobox que permite al usuario seleccionar el artista, el álbum o la lista que desea reproducir

## Menu Principal
Cuenta con interfaz sencilla y minimalista, que le permite al usuario ciertas funciones basicas las que fueron mencionadas anteriormente para que el usuario pueda interactuar con la aplicacion de una manera facil y sencilla.

[Menu principal]
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\inicio.png">
</p>  

Además de las funcionalidades básicas, MP3music cuenta con un área de texto en la que el usuario puede visualizar el contenido del archivo abierto. Esto permite un uso más intuitivo y sencillo del manejo del archivo, ya que el usuario puede verificar el contenido del archivo sin necesidad de abrirlo en un editor de texto externo.

## Cargar XML
[cargar archivo xml]
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\load.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\load1.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\load2.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\Archivocargadoxml.png">
</p>  
Al presionar el boton abrir, se desplega un cuadro de dialogo, en el que el usuario podra seleccionar cualquier tipo de archivo, unicamente con la restriccion detallada, que el tipo de archivo que acepta el programa es unicamente con extension "XML". Cualquier otro tipo de archivo, no se podra cargar en el sistema.

## Normal
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\normal.png">
</p>  

## Play
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\Archivocargadoxml.png">
</p>
Estando en inicio y cargado el xml que seleccionamos nos muestra los datos del xml cargado por artista, album y lista pero sin obtener el img o mp3, para obtenerlo damos play a la cancion que queremos escuchar. 
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\play.png">
</p>
Esto nos mostrara la cancion que seleccionamos con su img y mp3, ademas de que nos mostrara la informacion de la cancion que seleccionamos. 
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\PlaySong.png">
</p>  

## Play/Pausa
El boton de play/pausa nos permite pausar la cancion que estamos escuchando y reanudarla cuando queramos.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\Play_stop.png">
</p>  

## Siguiente
El boton de siguiente nos permite pasar a la siguiente cancion de la lista de reproduccion.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\nex.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\Nextmenu.png">
</p>
Otro ejemplo con otra Playlist
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\playlistseleccion.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\next.png">
</p>  

## Anterior
El boton de anterior nos permite pasar a la cancion anterior de la lista de reproduccion.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\back.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\Playsong.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\back1.png">
</p>  

## Aleatorio
El boton de aleatorio nos permite reproducir la lista de reproduccion en modo aleatorio.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\random.png">
</p>  

## Crear Lista
El boton de crear lista nos permite crear una lista de reproduccion nueva a partir de la lista de reproduccion actual.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\btncrear.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\crearlista.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\namelista.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\listashow.png">
</p>  

## Agregar Lista
El boton de agregar lista nos permite agregar una lista de reproduccion nueva.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\addli.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\lista.png">
    <img src= "C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\list2.png">
</p>  

## Add To List
El boton de add to list nos permite agregar canciones a una lista de reproduccion existente.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\listadd.png">
</p>  

## Save List
El boton de save list nos permite guardar la lista de reproduccion actual.
Por ejemplo usando los botones de crear lista y agregar lista, podemos crear una lista de reproduccion nueva y agregarle canciones. viendo se asi
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\save1.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\save2.png">
</p>  
Ok ahora dando al boton de save list
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\save.png">
</p>  
y asi quedaria al darle el xmly se guardaria en la Carpeta "MisListas"
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\save4.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\xmlsave.png">
</p>  
En caso de que exista una lista con el mismo nombre lanzara el siguiente mensaje
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\save3.png">
</p>  

## Clear List
El boton de clear list nos permite eliminar todas las canciones de una lista de reproduccion.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\btnclear.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\btnclear1.png">
</p> 
Asi quedaria la lista vacía sin datos:
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\clearlist.png">
</p>  

## Reproducir
El boton de reproducir nos permite reproducir la lista de reproduccion seleccionada.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\btnreproducir.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\playlistseleccion.png">
</p>  

## Reproducir Lista
El boton de reproducir lista nos permite reproducir la lista de reproduccion seleccionada.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\btnreproducirlist.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\playlistseleccion.png">
</p>  

## Combobox  Artista
Nos permite seleccionar el artista que queremos escuchar.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\choose.png">
</p>  

## Combobox  Album
Nos permite seleccionar el album que queremos escuchar en dado caso sea in single o si exista un album.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\album.png">
</p>  

## Combobox  Lista
Nos permite seleccionar la lista que queremos escuchar.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\Listaplaylistcombo.png">
</p>  

## Graphviz
El boton de graphviz nos permite exportar la lista de reproduccion actual a un archivo graphviz.dot y un png con la imagen de la lista de reproduccion.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\graphvizreport.png">
</p>
Crea lo siguiente:
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\library.dot.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\librarycode.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\GRaphdotpng.png">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\grapvhiz.png">
</p>   

## Generar Reporte HTML
El boton de generar reporte html nos permite exportar la lista de reproduccion actual a un archivo html junto con el numero de veces que se escucho una canción.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\btnhtml.png">
</p> 
Crea lo siguiente:
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\reports.png">
</p>
En la ruta de nuestra carpeta:
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\htmlurl.png">
</p>  
Viendo asi el reporte html que se genero queda de la siguiente manera:
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\Htmlreport.png">

## Salir
El boton de salir nos permite salir de la aplicacion mostrando un mensaje si deseamos salir.
<p align="center">
    <img src="C:\Users\javie\Escritorio\IPC2_Proyecto1Diciembre_-Grupo8\IMG\exit.png">
</p>  
Gracias por prestar atencion a nuestro manual de usuario, esperamos que disfrute de la aplicacion y que sea de su agrado.
