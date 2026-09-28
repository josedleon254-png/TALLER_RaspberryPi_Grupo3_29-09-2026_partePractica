# Bootear Debian 
El booteo (o arranque) es el proceso mediante el cual una computadora inicia y carga un sistema operativo en memoria para poder utilizarse. Al encender el equipo, el firmware (BIOS o UEFI) realiza una revisión básica del hardware y luego busca un dispositivo desde el cual arrancar, que puede ser el disco duro, una unidad de red o, en este caso, una memoria USB.

Para el booteo del la Distribucion de Linux Debian 13 necesitamos una herramineta con el fin de crear una unidad de arranque portable para poder ejecutarla en un dispositivo nuevo.

## Rufus ¿que es y como usarlo en dispositivos portables?
Creada por la necesidad de remplazar la aplicación **HP USB Disk Storage Format Tool** para Windows, que una vez fue una de las alternativas más rápidas y sencillas para crear un disco de arranque.

La función de **Rufus** es la de crear USBs de arranque. Con ellos puedes hacer varias cosas

- crear medios de instalación de otros sistemas operativos mediante sus imágenes ISO. 
- montar el sistema operativo en el USB para trabajar con él en cualquier ordenador que no lo tenga
- grabar datos con los que actualizar el firmware o la BIOS de un ordenador desde DOS.

Tiene dos versiones diferentes, una que se ejecuta en tu ordenador y otra portátil que puedes llevar en un USB para utilizarla en cualquier otro equipo.

En nuestro caso nos servira con el fin de usarlo en un dispositivo USB para podor arrancar el instalador de la imagen Debian 13

1. Acceder a la pagina de instalacion  
 <https://rufus.ie/es/#download>
2. dirigirse hasta la seccion de descargas 
![imagen de refencia visual para ubicarse al momento de descargar rufus](imagenes\1.png)
luego, dar clic sobre la opcion portable para windows
![imagen de referencia visua para indicar cual version de rufus descargar](imagenes\2.png)
3. guardar la intalacion en una carpeta para mas adelante
![imagen de referencia del guardado en una carpeta de rufus](imagenes\Imagen3.png)

## Descarga de la imagen Debian 13
1. Accder a la pagina de intalacion oficial 
<https://www.debian.org/distrib/>
![imagen de referencia del sitio de descarga oficial de Debian](imagenes\Imagen4.png)
2. dirigirse hacia el link de descarga apropiado, especificamente el apartado que dice "iso netinst para PC de 64 bits"
![imagen de referencia de la opcion de descarga correcta](imagenes\Imagen5.png)
**nota**: Al momento de instalar la imagen aparecera nombrada com arm64, esto no afecta en el caso de que su dispositivo su dispositivo tenga un procesador AMD o INTEL, funcionara en ambos casos.> 
![imagen de referencia de la image iso descargada](imagenes\Imagen6.png)
3. guardar la imagen iso en la misma carpeta donde se guardo previamente rufus 
![imagen de referenicia de guardado de la iso en la misma carpeta que rufus](imagenes\Imagen7.png)

## Limpiar USB previo a hacer el booteo 
**nota**: previo a hacer el booteo es preferible hacer una copia de los archivos que pueda contener el dispositivo ya que el objetivo de este proceso es que solo viva dentro de la USB la imagen ISO, ninguna otra mas.

1. verificar efectivamente que el dispositivo halla leido la USB (en mi caso, mi USB es el dispositivo nombrado como Linux Mint 22.3)
![verificacion que la computadoras halla leido correctamente la USB](imagenes\Imagen8.png)
luego dirigirse hacia el icono de windows, hacer clic derecho sobre el mismo y presionar la opción "adminnistracion de discos"
![imagen de referencia, que opcion presionar para limpiar la usb](imagenes\Imagen9.png)

2. Aparecera una ventana completamente nuevo, donde debe de aparecer nuevamente nuestra USB, de no aparecer puede que el dispositivo sufra de algun daño que no permita su corecta lectura. 
![imagen de la ventana de administracion de discos](imagenes\Imagen10.png)
haciendo clic derecho sobre el disco que tenga las especificaciones de nuestra usb, se desplegara un menu, debemos de seleccionar la opcion "Formatear".
![imagen del menu del USB](imagenes\Imagen11.png)
le aparecera una nueva ventada de verificacion, estando conciente de que perdera todo lo que tenga la USB dentro (y remarcando que si tiene dentro de ella informacion o documentos que le sean importantes, debe de hacer una copia de seguridad de esos archivos)
luego de eso y estar de acuerdo presione "si"
![imagen de verificacion para formatear la USB](imagenes\Imagen12.png)

3. se le pedira asiganrle un nuevo nombre al disco (la USB), pongale un nombre cualquiera, no importa realmnete ya que posteriormente al bootear ese nombre se sobreescribira. Luego precione el boton "Aceptar"
![imagen de renombramiento del disco](imagenes\Imagen13.png)
nuevamente mostrara una advetencia para que sepa que todo lo que contega el USB sera borrado (se remarca nuevamente hacer copia de seguridad si tiene algo importante dentro del USB, de lo contrario todo dentro de el se perdera irremediablemente), luego presionar en el boton "Aceptar"
![imagen de ultima advertencia antes de formatear el USB](imagenes\Imagen14.png)

4. Listo, una vez formateado el USB cambiara efectiavmente al nombre que le asigno previamente
![imagen del USB ya formateado](imagenes\Imagen15.png)
puede verificar tambien en el administrador de archivos del PC que efectivamente a sido formateado exitosamente
![imagen de administrador de archivos](imagenes\Imagen16.png)
![imagen dentro del USB](imagenes\Imagen17.png)

## bootear Debian 
1. dirijase nuevamente a la carpeta donde tiene almacenados tanto rufus como la imagen iso de Debian 13, luego haga doble clic en el archivo de Rufus, le saldran las siguientes advertencias, en ambas precione "si"
![imagen advertencia rufus 1](imagenes\Imagen18.jpg)
![imagen advertencia rufus 2](imagenes\Imagen19.png)

2. aparecera una nueva ventana, este es el programa de Rufus, en el debera de seleccionar tanto el la USB donde desea hacer el booteo y la imagen iso del sistema operativo deseado.
![imagen programa RUFUS funcionando](imagenes\Imagen20.png)
**nota: el programa puede llegar a seleccionar de manera autoamtica la USB, mientras que muy probablemente le toce buscar de amnera manualla imagen iso, para eso solamente presione la opcion de "seleccionar" y busque exactamente donde tiene guardada la imagen iso y seleccionela 
![imagen seleccion de ISO](imagenes\Imagen21.png)
![imagen rufus final](imagenes\Imagen22.png)
Luego presione el boton "Empezar"
**nota**: puede que le aparezca la siguiente advertencia, al nosotros descargar la imagen ISO del sitio oficial no tenemos ningun problema, ignorela y presione el boton "OK"
![advertencia Rufus](imagenes\Imagen23.png)

3. luego le aparecera una nueva ventana que le dara la opcion de escribir la imagen ya sea en ISO o DD, ya estara marcada como recomendada la opcion de la ISO, simplemente presione el boton "OK"
![seleccion entre ISO y DD](imagenes\Imagen25.png)
Luego le aparecera una nueva pestaña de advertencia, es esperable ya que la imagen que descargamos del sitio oficial de Debian es espeficiamente para que al momento de bootear se haga la descarga de los paquetes necesarios directos de internet, simplemente presione el boton "Si", si le aparece una nueva venta vuelva a presionar "Si" ya que es solo una confirmacion mas de lo que se debe hacer
![imagen de advertencia descarga de internet](imagenes\Imagen26.png)
![imagen de advertencia 2 descarga de internet](imagenes\Imagen27.png)
nuevamente aparecera una ventana nueva, en donde se le advierte que todo lo que pueda contener el USB sera borrado, por eso previamente se realizo el formateo del dispositivo, simplemente presione el boton "OK"
![imagen de advertencia 3 eliminacion de archivos](imagenes\Imagen28.png)
luego de eso empezara efectivamente el booteo de la imagen ISO Debian hacia la USB seleccionda
![proceso de booteo en marcha](imagenes\Imagen29.png)

4. posterior a espera unos minutos, podra denotarse que el boteo finalizo exitosamente cuando dentor de la barra verde aparece la frace "PREPARADO", con esto termina el booteo Debian 13
![booteo finalizado](imagenes\Imagen30.png)

