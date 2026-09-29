# Sistema Operativo para Raspberry Pi 

Recordemos, Raspberry Pi es un ordenador completo de tamaño compacto, como todo ordenador posee un sistema operativo.

También, al igual que cualquier ordenador existe la posibilidad de instalar sistemas operativos diversos que van desde distribuciones de Linux adaptadas al entorno de Raspberry como un sistema operativo oficial proporcionado por la Fundación Raspberry Pi

Hablamos de Raspberry Pi OS, (antes llamado Raspbian) es el sistema operativo oficial desarrollado por la Fundación Raspberry Pi que está basado en Debian. Que incluye un conjunto de Herramientas adaptadas a la educación, la programación y el uso cotidiano. El sistema ofrece un entorno gráfico (de escritorio) completo, ligero y optimizado, entre muchas otras cosas.

## Instalación de Raspberry Pi Imager SetUp
Imager SetUp no es más que el entorno donde llevaremos acabo la instalación del Raspberry Pi OS directo hacia una microSD

Aparte de necesitar una placa Raspberry Pi (no importa cual, prácticamente todas son compatibles) necesitamos de una tarjeta microSD con mínimo de 8 a 16 GB de almacenamiento para la versión de escritorio.

1. Diríjase hacia el siguiente link oficial para descargar Raspberry Pi Imager Setup (el instalador del sistema Raspberry pi OS)
<https://www.raspberrypi.com/software/>

![imagen de referencia visual del sitio oficial de instalación Raspberry Pi OS](imagenes\imagen31.png)

2. Luego, haga clic en la versión que se ajuste a sus preferencias o necesidades, existen tres versiones a descargar, La versión para Windows, La versión para sistemas Mac OS, y la versión para Linux que puede correr en cualquier distribución de Linux de 64 bits ya sea AMD o Intel, en este ejemplo lo estaremos haciendo por comodidad en Windows

![imagen de referencia versiones de instalacion](imagenes\imagen32.png)

![instalacion del instaladro terminada](imagenes\imagen33.png)

3. Una vez completada la instalación, acceder a este instalador que descargar la aplicación de Raspberry Pi Imager Setup, se le pedirán permisos para su ejecución 

![permisos para ejecutar la aplicacion Raspberry Pi Imager Setup](imagenes\imagen34.png)

Luego seleccione el idioma de su preferencia

![seleccion de idioma para Imager SetUp](imagenes\imagen35.png)

Luego de eso empezara la instalación normal de un programa de Windows, simplemente acepte todas las condiciones, luego presione Siguiente y espere a que se termine de instalar Imager SetUp

![instalacion Imager 1](imagenes\imagen36.png)

![instalacion Imager 2](imagenes\imagen37.png)

![instalacion Imager 3](imagenes\imagen38.png)

![instalacion Imager 4](imagenes\imagen39.png)

![instalacion Imager 5](imagenes\imagen40.png)

![instalacion Imager 6](imagenes\imagen41.png)

## Formatear Micro SD previo a instalar Raspberry Pi OS
Como requisito previo antes de instalar Rasberry Pi OS es necesario verificar que la microSD se encuentra limpia (sin ningún archivo en su interior) y no este estropeada, corrupta o posea algún virus, para esto es preferible formatearla para no generar inconvenientes.

**nota**: en caso de tener información o archivos importantes dentro de la microSD haga una copia de seguridad previa, ya que al formatear se perderá toda información que se encuentre dentro de ella.

1. Primero verifique que el sistema reconozca la microSD a usar, en el caso del ejemplo se trata de boofts y del disco extraíble 

![verificacion de lectura correcta de la targeta micro SD](imagenes\imagen42.png)

luego dirigirse hacia el icono de Windows, hacer clic derecho sobre el mismo y presionar la opción "administración de discos"

![imagen de referencia, que opcion presionar para formatear la micro SD](imagenes\Imagen9.png)

2. Aparecerá una ventana completamente nueva, donde debe de aparecer nuevamente nuestra microSD, de no aparecer puede que el dispositivo sufra de algún daño que no permita su correcta lectura. 

![administrador de disco donde se muestra la micro SD](imagenes\imagen43.png)

Haciendo clic derecho sobre el disco que tenga las especificaciones de nuestra microSD, se desplegara un menú, debemos de seleccionar la opción "Formatear".

![formateo de disco](imagenes\imagen44.png)

Se le presenta la opción de cambiarle nombre, puede cambiarlo al que más le guste, eso no importará luego ya que se sobrescribirá más adelante.

![cambio de nombre](imagenes\imagen45.png)

se le presentara una advertencia donde vuelve a recordar que al formatear la micro USB se perderá todo el contenido que tenga almacenado, de tener algo importante dentro se le sugiere presionar en "cancelar" y hacer una copia de seguridad, si quiere continuar solo presione "aceptar"

![advertencia formateo](imagenes\imagen46.png)

Y listo, esa partición en la memoria ha sido formateada, en caso de tener más particiones repita todo el proceso del paso 2.

![fromateo de particion exitoso](imagenes\imagen47.png)

3. en caso tenga mas particiones y ya las tenga todas formateadas se le sugiere eliminarla y juntar todas las particiones 

![borrar particion](imagenes\imagen48.png)

al borrar la partición (o volumen) se le mostrara una advertencia, esto en caso tenga contenido dentro de la partición, sabiendo que ya la hemos formateado simplemente presionamos "si"

![adevntencia borrado](imagenes\imagen49.png)

Y listo, la partición a sido borrada correctamente, en caso de tener más particiones también bórrelas, repita todo el paso 3.

![borrado de particion exitoso](imagenes\imagen50.png)

4. una vez tengamos nuestra micro USB formateada y sin particiones debemos crear un volumen completamente nuevo, hacemos clic derecho sobre la memoria no asignada y presionamos la opción "nuevo volumen simple"

![nuevo volumen simple](imagenes\imagen51.png)

nos aparece una pestaña nueva de instalación, presionamos en siguiente.

![volumen 1](imagenes\imagen52.png)

nos muestra la cantidad de espacio que queremos asignar al nuevo volumen en MB, no debemos editar nada aquí, simplemente le damos a siguiente

![volumen 2](imagenes\imagen53.png)

luego le deberá asignar una letra al volumen, póngale la que usted prefiera, luego dele a siguiente

![volumen 3](imagenes\imagen54.png)

se nos da la opción de volver a formatear el volumen, realmente no importa, puede presionar sin problema el botón "siguiente", también puede ponerle nombre al nuevo volumen, realmente tampoco importa, póngale el nombre que quiera.

![volumen 4](imagenes\imagen55.png)

Se ace un recuento de lo que se hará en el volumen, no le tome importancia, solo presione "finalizar"

![volumen 5](imagenes\imagen56.png)

Y listo, ya tiene el nuevo volumen, listo para instalar Raspberry Pi OS

![formato completo](imagenes\imagen57.png)

## instalacion Raspberry Pi OS
1. Tenemos que abrir la aplicación de Raspberry Pi Imager, donde se nos mostrar de primero la siguiente pantalla.

![pantalla inicion Imager](imagenes\imagen58.png)

Se le muestran varias opciones de placas a las cuales se les puede instalar el Raspberry Pi OS, elija la versión de placa que usted tenga, y tome en cuenta que lo único diferente entre su instalación y la mía será la versión de placa que posea cada uno, en mi caso avanzaremos con la versión de Raspberry pi 4

2. se le muestran 3 versiones de sistemas operativos disponibles a descargar. la versión de 64 bits que suele servir siempre para las placas más nuevas y por tanto también la más recomendable, la versión de 32 bits que como su nombre lo dice está pensada en la arquitectura ARM32 y destinada a los modelos más antiguos, y por último legacy de 32 bits pensada para aquellos que buscan compatibilidad con programas de Debian de versiones anteriores, por lo que no nos es del todo útil en general. Para nuestro taller se usará la primera opción de 64 bits

![version de OS](imagenes\imagen59.png)

3. luego de seleccionar nuestra versión de Raspberry Pi OS, no debe de mostrar nuestro dispositivo microSD para seleccionarlo e instalar ahí el sistema operativo, en caso de no aparecerle puede que el pc no lo halla leído o la microSD tenga algún fallo, también existe la posibilidad que no tenga un volumen en el cual almacenarse, puede volver al momento de limpiar la microSD y conformar que todo está en orden.

![seleccionar la micro SD](imagenes\imagen60.png)

4. luego nos darna aspectos de personalización, primero el nombre, sugiero uno simple y fácil de recordar como su propio nombre.

![personalizacion 1](imagenes\imagen61.png)

Luego aparecerá la localización, esto para tomar aspectos como la hora actual en su región, también el teclado con el que desea trabajar, si prefiere en ingles solo busque la opción "us" si lo quiere en español la opción "es"

![personalizacion 2](imagenes\imagen62.png)

luego tanto nombre de usuario como contraseña y su confirmación, sugiero algo fácil de recordar y no tan complejo, en el nombre no se pueden poner mayúsculas

![personalizacion 3](imagenes\imagen63.png)

Luego se le da la opción de elegir una conexión Wifi, esto es importante que lo sepa, en caso de que el pc no posea la misma conexión Wifi que la placa de Raspberry ya con su sistema operativo funcionando simplemente no se podrán conecta la una con la otra, siempre téngalas conectadas a la misma red

![personalizacion 4](imagenes\imagen64.png)

este es un punto importante de la personalización, por defecto la autenticación por SSH viene desactivada, debemos de activarla y marcar que se usara autenticación por contraseña

![personalizacion 5](imagenes\imagen65.png)

luego se le muestra la última opción de personalización que nos da la opción de conectarnos a Raspberry Pi Connect, una plataforma en línea que nos permite acceder 100% mediante internet hacia el escritorio de nuestra placa Raspberry Pi. Hacemos Click en el switch interactivo que nos despliega el siguiente menú, seleccionamos "Abrir Raspberry Pi Connect" 

![personalizacion 6](imagenes\imagen66.png)

se le abrirá en su navegador la siguiente pestaña, esta es la pestaña que le ha de aparecer en caos ya tenga una cuanta creada, de no tenerla simplemente cree una cuenta propia en el siguiente link <https://www.raspberrypi.com/software/connect/> luego vuelva a la aplicación de Raspberry Pi Imager y vuelva a presionar el botón de "Abrir Raspberry Pi Connect" **nota**: solo se puede asignar una cuenta de Raspberry Pi Connect a un sistema operativo de Raspberry Pi OS, en un futuro podrá añadir a otros colaboradores para que trabajen en la misma placa pero no en este momento.

![personalizacion 7](imagenes\imagen67.png)

luego presione en su usuario personal, le deberá de aparecer esta nueva pestaña, presione el botón “Create auth key and launch Raspberry Pi Imager” 

![personalizacion 8](imagenes\imagen68.png)

luego de presionar la opción requerida el sistema le pedirá abrir cierto contenido en Raspberry Pi Imager, simplemente presione en "abrir"

![personalizacion 9](imagenes\imagen69.png)

luego de presionar en "abrir" vuelva a Raspberry Pi Imager y vera que ahora abra un código en pantalla en donde antes solo había la frase "esperando testigo" por motivos de seguridad no comparta esa clave con nadie

![personalizacion 10](imagenes\imagen70.png)

5. luego de toda la personalización de su Usuario, se empezará el proceso de escritura en el dispositivo microSD que haya seleccionado, Presione el botón "escribir" y espere a que termine de ejecutar todos los comandos

![escritura 1](imagenes\imagen71.png)

se le mostrar la siguiente advertencia, ya era consiente de antemano que todo el contenido dentro de la microSD seria borrado irremediablemente por eso la hemos preparado antes formateándola, ahora solo debe de presionar el botón "lo entiendo, borrar y escribir" para empezar ahora si la instalación del sistema operativo Raspberry Pi OS

![escritura 2](imagenes\imagen72.png)

luego de terminar la escritura en aproximadamente 5 a 7 minutos se le mostrar esta pantalla confirmando que el sistema Raspberry Pi OS a sido instalado correctamente en el microSD

![escritura 3](imagenes\imagen73.png)

## como ver el esritorio de Raspberry pi OS?
para acceder al escritorio de Raspberry Pi OS se deben de seguir los siguientes pasos.

1. ya con el sistema operativo instalado en la micro D retíralo de manera segura de tu pc y luego instálalo en la parte de abajo de la Raspberry pi
2. luego de eso conecta tu Raspberry Pi a la corriente, espera un minuto encienda de manera correcta
3. recuerda está conectado a la misma red de internet tanto en la pc como en el Raspberry Pi, para hacer la conexión correcta
4. **nota**: todos los procedimientos que siguen pueden ser usados indiferentemente del sistema operativo que utilice.
debe abrir su cmd si se encuentra en Windows o un terminal en caso se encuentre en Linux, luego escriba este código `ssh nombreUsuario@NombreEquipo.local` luego presione la tecla Enter

![entrada a Raspberry pi](imagenes\imagen74.png)

luego se le preguntara si deseas continuar con la conexión, tiene que escribir "yes" en el cmd/terminal luego presione enter.
luego de eso le pedirán escribir su contraseña, misma que habría escrito durante la instalación de Raspberry Pi OS

![contraseña Raspberry](imagenes\imagen75.jpeg)

de esta manera estará oficialmente dentro de la Raspberry, lo podrá notar ya que al inicio de cada línea de código ahora aparece el nombre y usuario asignado a la Raspberry Pi y no al del pc

5. una vez dentro de la Raspberry es recomendable ejecutar el siguiente comando `sudo apt update && sudo apt upgrade` para hacer actualización de librerías entre otras cosas que tiene Raspberry pero se encuentran desactualizadas. 

![actualizacion 1](imagenes\imagen76.png)

una vez ejecutado el comando se le pedirá permiso para actualizar y descargar todo lo necesario, solo debe de escribir en el terminal la letra "Y". **Nota**: este proceso es tardado, tomarlo en cuenta si se cuenta con prisa, todo dependerá del internet que posea.

![actualizacion 2](imagenes\imagen77.png)

![actualizacion 3](imagenes\imagen78.png)

![actualizacion 4](imagenes\imagen79.png)

6. De manera manual desde el CMD/terminal haremos la conexión inicial 
`rpi-connect on` esto para el arranque, presionamos después la tecla enter

![on](imagenes\imagen80.png)

luego escribiremos este otro comando `rpi-connect signin` este link servirá para conectar la cuenta directo con nuestra Raspberry

![signin](imagenes\imagen81.png)

nos dará un link, al dual deberemos de ingresar. Teniendo nuestra cuenta de Raspberry Pi Connect ya iniciada simplemente presionamos el botón de "sing in ass Tudispositivo" 

![link](imagenes\imagen82.png)

Luego le ponemos nombre a nuestro dispositivo

![nombre](imagenes\imagen83.png)

Luego nos mostrara otra pestaña donde nos responderá que la conexión fue exitosa 

![exito 1](imagenes\imagen84.png)

![exito 2](imagenes\imagen85.png)

siempre en el navegador accederemos a ese hipervínculo nombrado como "the device" y nos mostrara otra pestaña con todas las especificaciones de nuestro dispositivo 

![dispositivo](imagenes\imagen86.png)

en esa misma pestaña nos dirigimos al botón "Connect via" en el cual se nos mostraran dos formas de conectarnos directo a la Raspberry 
- **remote shell** nos abrirá una nueva ventana de navegador en la cual básicamente se muestra el terminal directo de la Raspberry (como el que tenemos abierto actualmente en nuestra pc). en caso de querer cerrarlo solamente cierre la ventana

![terminal Rasp](imagenes\imagen87.png)

- **Screen Sharing** nos abrirá una nueva ventana de navegador en la cual nos mostrara un escritorio interactivo, este seria el escritorio de la Raspberry Pi, por tanto ese sistema operativo que vemos es el Raspberry Pi OS, en el cual se puede trabajar como en un ordenador común y corriente. en caso de cerrarlo el sistema tiene un botón "Disconect" presiónelo y se cerrara la sesión, puede después cerrar la ventana.

![OS](imagenes\imagen88.png)

ahora en caso de querer desconectarlo usaremos el comando `rpi-connect signout` desde nuestro terminal en el pc el cual desconectara nuestro Raspberry pi con Raspberry Pi Connect.

![signout](imagenes\imagen89.png)

![desconectado](imagenes\imagen90.png)

ahora en caso de querer desconectar totalmente Raspberry Pi Connect de nuestra Raspberry simplemente escribimos el comando `rpi-connect off`el cual detendrá en automático todos los procesos que la Raspberry tenía relacionados con Raspberry Pi Connect 

![off](imagenes\imagen91.png)

en caso quiera conocer más acerca de Raspberry Pi Connect recomiendo leer su documentación, que se encuentra en el siguiente link `https://www.raspberrypi.com/documentation/services/connect.html`

7.  para desconectar el terminal de Raspberry Pi de nuestro ordenador simplemente basta con escribir `exit`en el terminal y volveremos al terminal original de nuestro pc

![exit](imagenes\imagen92.png)

