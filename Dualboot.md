# Sistema Dualboot (dos sistemas operativos en un mismo pc)
El arranque dual se refiere al proceso de instalar y ejecutar dos sistemas operativos diferentes en un único ordenador. Esto te permite elegir entre los dos cuando arrancas tu ordenador, dándote la flexibilidad de cambiar entre ellos en función de tus necesidades.

Para nosotros como estudiantes puede llegar a ser complicado el tener mas de una laptop disponible para porder tener un sistema operativo como windows y a su vez tener otra laptop con otro sistema operativo como linux Debian. que nuestro equipo principal no tenga las capacidades necesarias para soportar una maquina virtual. Ese es para nosotros el punto fuerte de usar el metodo Dualboot permite experimentar con distintos sistemas operativos sin tener que comprar hardware aparte, aunque evidentemen este metodo tambien tiene sus complejidades.

es posible el arranque dual de Windows y Linux en un ordenador compatible. Sin embargo, este proceso puede ser más complejo que el arranque dual de dos versiones del mismo sistema operativo. Es posible que tengas que tener en cuenta problemas de compatibilidad, requisitos de hardware y seguir pasos de instalación específicos para establecer una configuración de arranque dual con Windows y Linux.

## como instalar un sistema dualboot? 
se tomara en cuenta que el estudiante cuenta al principio de este taller solamente con sistema operativo Windows, por tanto el segundo sistema operativo a instala sera Linux debian que ya tenemos preparado en nuestro usb (ver leccion sobre bootear Debian)

### punto de Restauracion del sistema como respaldo
existe una posibilidad que muchos realmente queremos evitar, que el dualboot falle y arruine no solo Linux sino tambien Windows, por lo cual es indispensables crea un respaldo previo a hacer el dualboot

1. presione la tecla windows y escriba "crear un punto de restauracion" luego dele clic a la primera opcion que aparece
![punto 1](imagenes\imagen93.png)

2. se abrira una nueva ventana, en la cual nos mostrara las particiones con las que cuenta nuestro disco duro, buscaremos especificamente la particion en la que esta nuestro primer sistema operativo, en mi caso es el disco C
![punto 2](imagenes\imagen94.png)
luego presionamos el boton "crear"

3. luego de precionar el boton "crear" nos aparece una ventana nueva que nos pide ponerle una descipcion al punto de restauracion con el din de identificarla (esto en caso usted haga este tipo de restauraciones seguido)
![descripcion](imagenes\imagen95.png)
luego presione el boton "crear", el sistema hara el resto.
![proceso](imagenes\imagen96.png)
cuando termine el propio sistema, mostrara el siguiente mensaje, por lo que el trabajo ya estara hecho, podemos continuar con la el proceso de dualboot
![punto generado](imagenes\imagen99.png)

### desactivar sifrado de bit_locker
bit-locker púede interferir al momento de instalar linux por lo que es recomendable desabilitarlo. 
Esto es solo en caso utilice una version de windows 10 u 11 profesional, pero como saber que version de windows tengo? 

prseione la combinacion de teclas `windows + r` y escriba `winver` luego presione la tecla enter o el boton "aceptar"
![winver](imagenes\imagen100.png)

le abrira una nueva ventana en la cual le especificara si tiene o no windows profesional, en caso de no tener windows pro siga al sigueinte paso, en caso de si tenerlo permanez aqui para desabilitar efectivamente bit_locker
![pro](imagenes\imagen101.png)

1. presiona la tecla windows y escribe `cmd`, luego selecciona la primera opcion, presiona clic derecho y ejecutalo como administrador
![cmd](imagenes\imagen102.png)

2. dentro del cmd en modo administrador escribe el siguiente comando `manage-bde -status` el cual mostrar si bit-locker esta activada, desactivado o error de "no hay volumenes" (como es mi caso)
![error](imagenes\imagen103.png)
esta otra imagen muestra como se ve un equipo profesional con bit-locker desactivado
![ejemplo desactivado](imagenes\imagen104.png)
en cuyo caso bit-locker este activado deveria de mostrar los siguientes campos

| Campo | BitLocker activo | BitLocker desactivado (listo para Linux) |
|---|---|---|
| Conversion Status | Fully Encrypted / Encryption in Progress | Fully Decrypted |
| Percentage Encrypted | 100.0% | 0.0% |
| Encryption Method | XTS-AES 128 o 256 | None |
| Protection Status | Protection On | Protection Off |
| Key Protectors | TPM, Numerical Password, etc. | None Found | 

3. en caso de tenerlo activo haga lo siguiente
Desde una terminal (cmd) como administrador: `manage-bde -off C:` Repetir para cada unidad cifrada
4. El descifrado ocurre en segundo plano. Se puede seguir con: `manage-bde -status C:`

5. por ultimo volver a probar `manage-bde -status`, debera tener los valores correctos segun la tabla

### creacion de espacio para debian 
1. sobre el icono de windows precionamos el click derecho, buscamos la opcion "administracion de discos" y accedemos a ella.
![imagen de referencia, que opcion presionar para limpiar la usb](imagenes\Imagen9.png)

2. en caso de no tener espacio libre o espacio suficiente en el disco podemos utilizar un poco del espacio de otr particion mas grande, damos clic derecho a la particion que deseamos reducir y damos click en la opcion de "reducir volumen"
![reducir](imagenes\imagen105.png)

3. nos abrira una nueva pestaña, en ella nos mostrar cuantas megas tiene en total la particion, cuantas megas tiene disponible y de cuantas megas queremos hace rla reduccion, lo minimo indispensables para linux Debian podrian ser 50 GB de almacenamiento, puede asiganrle mas no hay problema, como saber cuanto son 50 GB en MG? con la siguiente formula `totalGigas * 1024` para las 50 GB la formula seria `50 * 1024 = 51200` por lo que eso es lo que destinare en mi equipo hacia linux Debian
![megas a reducir](imagenes\imagen106.png)
luego presionamos el boton "reducir"

4. esto creara un espacio libre sin asignar, eso seria todo el proceso en este punto 
![libre](imagenes\imagen107.png)

### Arrenque de sistema desde la bios 
para este punto debe de tener conectada a la PC/laptop la USB boorteada con el sistema operativo deseado

para esto es necesario apagar la pc, volver a encenderla y justo en ese momento debera de usar el atajo del teclado para acceder a la bios segun su laptop o modelo de placa base.

debera de buscar la pocion de "boot opcions", exciste la posibilidad que esta configuracon no este directamente en la bios, por lo cual se le recomienda buscar segun su modelo de placa como acceder a ese apartado, en mi caso no se encuentra dentro de la bios por o que debere de apagar mi laptop, encenderla y presionar en ese momento F9 y tambien para las mayoria de laptop HP

debera de abilitar el arranque mediante USB (si es que su pc lo pide), luego desabilidtar el arranque seguro (a menos que te preocupen las politocas de seguridad de windows, en cuyo caso mantenlas abilitadas), estas dos cosas dependiendo del equipo puede pedirlas o no, en mi caso no las pide y directamente me permite arrancar el sistema con mi USB
![boot USB](imagenes\imagen108.png)
selecciona la opcion "USB hard Drive 1" o similar e inicia la instalacion

## Instalacion de Debian 
1. aparece el siguiente menu de seleccion, con varias opciones, la que nos interesa es la opcion "Graphical install" 
![1](imagenes\imagen109.png)

2. se nos da a elegir el idioma 
![2](imagenes\imagen110.png)

3. se nos da la opcion de elegir la ubicacion donde nos enconramos, el primer menu de seleccion solo muestra unos cuantos paises, para encontrar a otros Paises de latinoamerica nos dirijimos hasta abajo y seleccionamos "other" 
![3](imagenes\imagen111.png)
luego seleccionamos la region que deseamos
![4](imagenes\imagen112.png)
por ultimo el pais deseado
![5](imagenes\imagen113.png)

4. esta pantalla es mostrada devido a que no hay un idioma ingles asigando a la region de centro america, solo elijamos USA
![6](imagenes\imagen114.png)

5. elegir la distribucion de teclado que queremos
![7](imagenes\imagen115.png)

6. el instalador busca la usb para descargar el resto de componentes
![8](imagenes\imagen116.png)

7. opcines de coneccion a internet, si queremos hacerlo mediante ethernet o wifi, elegimos wifi
![9](imagenes\imagen117.png)
elegimos el internet que queremos usar para el resto de la instalacion
![10](imagenes\imagen118.png)
aora nos pregunta ue tipo de seguridad tiene el wifi, si es abierta (publica) o protegida (privada), en nuestro caso nuesstras redes domestocas usan WPA/SPA2 PSK, por lo tanto la seleccionamos
![11](imagenes\imagen119.png)
luego nos pide introducir la contraseña del internet que hemos seleccionado 
![12](imagenes\imagen120.png)
el instalador está haciendo el "handshake" o intercambiar claves con el router o punto de acceso usando la contraseña escrita.
![13](imagenes\imagen121.png)

8. ahora pide ponerle un nombre al equipo, use el de su preferencia
![14](imagenes\imagen122.png)
Aquí puedes dejar el campo vacío y presionar Continuar. El dominio solo se usa en redes corporativas o de servidores; en una computadora personal o de estudiante no hace falta.
![15](imagenes\imagen123.png)
Se nos da la opcion de crear una cuenta root en nuestra distribucion. Dejar ambos campos vacíos y continuar: la cuenta root queda deshabilitada y el usuario normal podrá usar sudo para tareas de administrador.
![16](imagenes\imagen124.png)
Ahora creremos el usuario principal del sistema,puedes ponerle el tu nombre completo si quieres o solo un nombre, da igual 
![17](imagenes\imagen125.png)
Este es el nombre con el que iniciarás sesión y que verás en la terminal (por ejemplo, sfmx@debian), puedes cambiarlo sin problemas, es solo un nombre sugerencia basado en las iniciales del nombre que escribiste en el paso anterior.
![18](imagenes\imagen126.png)
en este paso se elige la contraseña a usar en tu dispositivo, de dejar el campo vacio el usuario no contara con contraseña
![19](imagenes\imagen127.png)

9. el instalador está buscando los discos de tu computadora para poder particionarlos.
![20](imagenes\imagen128.png)
es la parte mas delicada de la instalacion, se dan varias opciones 
- **Guiado - usar el mayor espacio libre contiguo**: instala Debian solo en el espacio libre que ya exista, sin tocar lo demás. Es la opción segura si quieres conservar otro sistema (por ejemplo Windows) y ya dejaste espacio libre.
- **Guiado - usar todo el disco**: borra todo el disco y crea las particiones automáticamente. NO ELEGIR ESTA OPCION BAJO NINGUN CONCEPTO
- **LVM / LVM cifrado**: igual que la anterior, pero con volúmenes lógicos (LVM) o con cifrado del disco. Útiles en casos específicos. NO ELEGIR ESTA OPCION BAJO NINGUN CONCEPTO
- **Manual**: tú creas y asignas cada partición. Es la que está seleccionada ahora, y solo conviene si sabes qué esquema quieres, no es necesario ya que creamos anteriormente una particion exclusiva para debian

Para lo que nosotros respecta, podemos usar tanto la primera como la ultima opcion, en este Caso usaremos "manual"
![21](imagenes\imagen129.png)
pantalla de particionado del disco, en el caso de la imagen se cuentan con mas de 200 GB libres, ahi se instalaremos Debian
![22](imagenes\imagen130.png)
Elegir "Create a new partition" y pulsa "Continue"
![23](imagenes\imagen131.png)
Escribe el tamaño deceado de a particion y pulsa Continue. En la captura se escribió 32gb; para un equipo normal basta con 4 a 8 GB
![24](imagenes\imagen132.png)
Deja Beginning y pulsa Continue
![25](imagenes\imagen133.png)

10. ahora hay que combertila en Swap (Memoria de apoyo) Por defecto la partición nueva aparece como Ext4 en /:
![26](imagenes\imagen134.png)
Selecciona Use as: y pulsa Continue. En la lista elige swap area:
![27](imagenes\imagen135.png)
Deberá quedar así. Luego elige Done setting up the partition:
![28](imagenes\imagen136.png)

11. es momento de Revisar. Ya aparece la partición swap. Ahora selecciona el FREE SPACE que sobra (el de abajo).
![29](imagenes\imagen137.png)
Elige Create a new partition otra vez
![30](imagenes\imagen138.png)

12. ahora el tamaño de la raiz (Todo el sistema y tus archivos) Deja el tamaño máximo que ya aparece (o escribe max) y pulsa Continue. Elige Beginning si te lo pregunta.
![31](imagenes\imagen139.png)

13. Configurar la raíz, Aquí ya viene todo bien por defecto:
- **Use as:** Ext4 journaling file system
- **Mount point:** `/`
Solo elige **Done setting up the partition** y pulsa **Continue**
![32](imagenes\imagen140.png)

14. la vista final, Comprueba que tienes:
- una partición **swap**
- una partición **ext4** con `/`
![33](imagenes\imagen141.png)

15. Elige Finish partitioning and write changes to disk y pulsa Continue.
![34](imagenes\imagen142.png)

16. Lee la lista de particiones que se van a formatear: solo deben ser las nuevas (swap y ext4). Si aparece alguna partición de Windows, elige No y revisa. Si todo está bien, marca Yes y pulsa Continue.
![35](imagenes\imagen143.png)

17. El instalador formatea las particiones. Solo espera.
![36](imagenes\imagen144.png)

18. Ahora el instalador copia al disco los paquetes esenciales de Debian. No tienes que hacer nada, solo esperar.
![37](imagenes\imagen145.png)

19. Aquí eliges desde qué servidor se descargarán los paquetes de Debian. United States funciona bien desde Guatemala y suele ser rápido, pulsar Continue.
![38](imagenes\imagen146.png)

20. traduccion directa, Debería usar un espejo de su país o región si no sabe qué espejo tiene la mejor conexión a Internet para usted. Normalmente, deb.debian.org es una buena elección.
![39](imagenes\imagen147.png)

21. Déjalo vacío y pulsa Continue. Solo lo necesitas si tu red (por ejemplo, una empresa o universidad) obliga a usar un proxy para salir a internet. En una red de casa o Wi-Fi normal, no.
![40](imagenes\imagen148.png)

22. El instalador está descargando las listas de paquetes del espejo que elegiste (deb.debian.org), solo espere.
![41](imagenes\imagen149.png)
el instalador está preparando la lista de software y descargando los archivos necesarios. No tienes que hacer nada, solo esperar.
![42](imagenes\imagen150.png)

23. traduccion directa: Por el momento, solo está instalado el núcleo del sistema. Para ajustar el sistema a sus necesidades, puede elegir instalar una o más de las siguientes colecciones predefinidas de software.Ya viene marcado lo que conviene: Debian desktop environment, GNOME y standard system utilities. Así tendrás un escritorio completo y las herramientas básicas.
![43](imagenes\imagen151.png)

24. traduccion directa. La instalación ha terminado, así que es hora de arrancar su nuevo sistema. Asegúrese de retirar el medio de instalación, para que arranque el nuevo sistema en lugar de reiniciar la instalación.
![44](imagenes\imagen152.png) 

24. simplemente se esta reiniciando el sistema operativo, no hay qu ehacer nada. 
![45](imagenes\imagen153.png)

25. el sistema iniciar de manera normal. no debe de ahcer nada, solo esperar a que aparezaca su usuraio
![46](imagenes\imagen154.png)
![47](imagenes\imagen155.png)
