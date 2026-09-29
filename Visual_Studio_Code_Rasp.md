# Como instalar y entrar a visual studio code en una Raspbery

## como isntala visual Studio Code
1. debes entrar directo en el terminal de Rasberry Pi, ara eso habre un terminal directo en Debian y ejecuta el comando `ssh nombreUsuario@NombreEquipo.local`, se le pedira la contraseña para entrar directo en en terminal de Raspberry Pi

![ssh](imagenes/imagen156.png)

2. Actualiza la lista de paquetes: `sudo apt update`

![update](imagenes/imagen157.png)

3. Instala VS Code: `sudo apt install code`

![install code](imagenes/imagen158.png)

## Como ejecutar visual studio code de Raspberry Pi desde la version de PC

1. Prueba primero que el SSH funciona desde tu PC `ssh nombreUsuario@NombreEquipo.local`

![ssh](imagenes/imagen156.png)

2. Instala la extensión "Remote - SSH" de Microsoft en VS Code de tu PC, para esto tienes que ir directo a extenciones
![estenciones](imagenes/imagen159.png)
luego buscar la extencion "Remote - SSH"

![remote install](imagenes/imagen160.png)

3. luego de instalarla busque en la barra lateral izquierda de visual studio el sigueinte simbolo ![remote](imagenes/imagen161.png), acceda a el, debe de mostarse lo siguiente

![ssh](imagenes/imagen162.png)

debera de seleccionar el simbolo "+", al hacerlo aparecera lo siguiente 

![+](imagenes/imagen163.png) 

siga las intruciones y escriba el comando `ssh nombreUsuario@NombreEquipo.local` 

![Rasp](imagenes/imagen164.png) 

luego presione la tecla "enter"

4. debera de aparecerle exactamente su dispositivo, uede notar la flecha y el recuadro? pues tiene opciones distintas de abrir Visual Studio Code desde su version de PC

![opcines](imagenes/imagen165.png)

y sea que quiera conectar en la ventana actual ![actual](imagenes/imagen166.png) o conectar en una nueva ventana ![otra](imagenes/imagen167.png), en neustro caso elejiremos la opcion de nueva ventana

5. al abrir la nueva ventana nospide directamente la contrasea de nuestra Raspberry Pi, siga las instrucciones y coloquela, luego presione "enter"

![contrasena](imagenes/imagen168.png)


6. listo, estamos dentro del Visual Studio Code de la RaspBerry pi, podemos confrimarlo viendo el recuadro azul en la punta izquierda abajo de la pantalla que muestra el nombre de nuestra Raspberry de local

![final](imagenes/imagen169.png)

como nota adicional, al contrrio de como pasa en windows o linux normal, para buscar la ubicacion de nuestros archivos devemos de esribir su direccion en carpeta para acceder a ella.
