# Pines GPIO en Raspberry Pi: pinout y primer proyecto

Hasta ahora tenemos la Raspberry Pi funcionando y accesible por SSH y VS Code. Ahora vamos a usarla para lo que la hace especial frente a una computadora normal: **controlar el mundo físico con código**.

## ¿Qué es un GPIO?

GPIO significa *General Purpose Input/Output* (entrada/salida de propósito general). Son los pines metálicos que sobresalen de la placa (40 pines en las Raspberry Pi 3, 4, 5 y Zero). Cada uno puede configurarse desde Python como:

- **Salida**: el programa decide si el pin entrega **3.3 V** (encendido, `1`) o **0 V** (apagado, `0`). Sirve para encender un LED, un zumbador o un relé.
- **Entrada**: el programa **lee** si el pin recibe 3.3 V o 0 V. Sirve para leer un botón o un sensor digital.

> No todos los pines son GPIO. Algunos entregan alimentación (3.3 V, 5 V) y otros son tierra (GND).

[IMG: foto de la placa señalando la fila de pines]

## El pinout

El **pinout** es el mapa que dice qué hace cada pin. Se puede ver de dos formas:

1. En la terminal de la Raspberry, escribiendo `pinout`. Dibuja la placa completa con sus pines.
2. En la tabla de abajo (vista con la placa con los pines arriba y la ranura de la microSD hacia abajo).

| Pin | Función | | Pin | Función |
|:---:|---|---|:---:|---|
| 1 | 3.3 V | | 2 | 5 V |
| 3 | GPIO 2 (SDA) | | 4 | 5 V |
| 5 | GPIO 3 (SCL) | | 6 | **GND** |
| 7 | GPIO 4 | | 8 | GPIO 14 (TXD) |
| 9 | **GND** | | 10 | GPIO 15 (RXD) |
| 11 | **GPIO 17** | | 12 | GPIO 18 |
| 13 | **GPIO 27** | | 14 | **GND** |
| 15 | **GPIO 22** | | 16 | **GPIO 23** |
| 17 | 3.3 V | | 18 | **GPIO 24** |
| 19 | GPIO 10 (MOSI) | | 20 | GND |
| 21 | GPIO 9 (MISO) | | 22 | GPIO 25 |
| 23 | GPIO 11 (SCLK) | | 24 | GPIO 8 (CE0) |
| 25 | GND | | 26 | GPIO 7 (CE1) |
| 27 | ID_SD | | 28 | ID_SC |
| 29 | GPIO 5 | | 30 | GND |
| 31 | GPIO 6 | | 32 | GPIO 12 |
| 33 | GPIO 13 | | 34 | GND |
| 35 | GPIO 19 | | 36 | GPIO 16 |
| 37 | GPIO 26 | | 38 | GPIO 20 |
| 39 | GND | | 40 | GPIO 21 |

En **negrita** están los pines que usaremos en el proyecto.

[IMG: captura del comando `pinout` en la terminal]

### Dos formas de numerar (fuente clásica de confusión)

Cada pin tiene **dos números**:

| Numeración | Qué es | Ejemplo |
|---|---|---|
| **Física (BOARD)** | La posición del pin en la placa, del 1 al 40 | Pin físico 11 |
| **BCM (GPIO)** | El número del chip Broadcom, el que usa el código | GPIO 17 |

El pin físico 11 **es** el GPIO 17. En el código de este taller siempre usamos la **numeración BCM** (`LED(17)`), pero al cablear contamos los pines físicos de la tabla.

### Reglas de seguridad

1. Los GPIO trabajan a **3.3 V**. **Nunca** conectes 5 V a un pin GPIO: puede dañar la placa de forma permanente.
2. **Apaga la Raspberry** (`sudo shutdown now`) antes de cambiar el cableado.
3. Cada GPIO entrega poca corriente (unos 16 mA como máximo recomendado). **Todo LED lleva una resistencia** en serie.
4. Nunca conectes un pin directamente a GND o a 5 V sin una carga en medio.

## Electrónica mínima que necesitamos

### Resistencia para el LED

Un LED no limita su propia corriente. Con la Ley de Ohm calculamos la resistencia:

```
R = (V_fuente − V_LED) / I
R = (3.3 V − 2.0 V) / 0.004 A ≈ 325 Ω  →  usamos 330 Ω
```

Con 330 Ω circulan unos 4 mA: el LED se ve bien y el pin trabaja sin esfuerzo. (Un LED rojo cae aprox. 2 V; uno verde, un poco más).

### Botón

El botón se conecta entre el pin GPIO y GND. La Raspberry tiene una **resistencia pull-up interna** que mantiene el pin en 3.3 V (`no presionado`). Al presionar, el pin se conecta a GND (`presionado`). La librería `gpiozero` activa ese pull-up automáticamente, así que **no hace falta una resistencia externa**.

### Polaridad del LED

La pata **larga** es el ánodo (+) y va hacia el GPIO (a través de la resistencia). La pata **corta** es el cátodo (−) y va a GND.

## Proyecto: semáforo con cruce peatonal

Un semáforo de autos que está en **verde** hasta que un peatón presiona un botón. Entonces hace la secuencia completa: amarillo, rojo y zumbador sonando mientras cruza, y luego vuelve a verde.

Es un ejemplo real de **control secuencial** con una entrada (botón) y varias salidas (3 LEDs y un zumbador).

### Materiales

- 1 Raspberry Pi con Raspberry Pi OS
- 1 protoboard y cables macho-macho
- 3 LEDs (rojo, amarillo, verde)
- 3 resistencias de 330 Ω
- 1 zumbador **activo** (suena solo al darle voltaje)
- 1 pulsador

### Conexiones

| Componente | Pin GPIO (BCM) | Pin físico | Al otro lado |
|---|:---:|:---:|---|
| LED rojo (+, pata larga) | GPIO 17 | 11 | Resistencia 330 Ω → pata corta a GND |
| LED amarillo (+) | GPIO 27 | 13 | Resistencia 330 Ω → pata corta a GND |
| LED verde (+) | GPIO 22 | 15 | Resistencia 330 Ω → pata corta a GND |
| Zumbador (+) | GPIO 23 | 16 | Terminal (−) a GND |
| Botón | GPIO 24 | 18 | Otro terminal a GND |
| GND común | — | 6, 9 o 14 | Riel azul (−) de la protoboard |

```
GPIO17 (pin 11) ──[330Ω]──▶|── GND     (LED rojo)
GPIO27 (pin 13) ──[330Ω]──▶|── GND     (LED amarillo)
GPIO22 (pin 15) ──[330Ω]──▶|── GND     (LED verde)
GPIO23 (pin 16) ──────────(BZ)── GND    (zumbador)
GPIO24 (pin 18) ──────────/ ── GND      (botón)
```

> Usa un zumbador activo de bajo consumo. Si el tuyo consume más de unos 10 mA, no lo conectes directo al GPIO.

[IMG: foto o diagrama del circuito armado]

### El código

Crea el archivo `semaforo.py` (por ejemplo, desde VS Code conectado por SSH):

```python
from gpiozero import LED, Button, Buzzer
from time import sleep

# --- Configuración de pines (numeración BCM) ---
rojo     = LED(17)
amarillo = LED(27)
verde    = LED(22)
buzzer   = Buzzer(23)
boton    = Button(24, bounce_time=0.1)   # bounce_time evita lecturas falsas por rebote


def estado_autos():
    """Estado normal: los autos pasan."""
    rojo.off()
    amarillo.off()
    verde.on()


def cruce_peatonal():
    """Secuencia completa cuando un peatón presiona el botón."""
    print("Peatón solicita cruzar...")

    # 1. Aviso a los autos
    verde.off()
    amarillo.on()
    sleep(2)
    amarillo.off()

    # 2. Autos detenidos, peatón cruza (zumbador suena 5 segundos)
    rojo.on()
    print("Peatones cruzando")
    buzzer.beep(on_time=0.25, off_time=0.25, n=10, background=False)

    # 3. Vuelve al estado normal
    rojo.off()
    estado_autos()
    print("Autos circulando")


# --- Programa principal ---
estado_autos()
print("Semáforo listo. Presiona el botón para cruzar (Ctrl+C para salir).")

while True:
    boton.wait_for_press()   # el programa espera aquí hasta que presionen el botón
    cruce_peatonal()
```

### Ejecutarlo

En la terminal de la Raspberry, dentro de la carpeta del archivo:

```bash
python3 semaforo.py
```

Para detenerlo, presiona `Ctrl + C`.

[IMG: captura de la terminal con la salida del programa]

### ¿Cómo funciona?

| Parte del código | Qué hace |
|---|---|
| `LED(17)` | Crea un objeto que controla el GPIO 17 como salida. |
| `Button(24)` | Crea una entrada con pull-up interno en el GPIO 24. |
| `.on()` / `.off()` | Pone el pin en 3.3 V o en 0 V. |
| `sleep(2)` | Pausa el programa 2 segundos. |
| `buzzer.beep(..., n=10, background=False)` | Suena 10 veces (0.25 s encendido, 0.25 s apagado) y espera a terminar. |
| `boton.wait_for_press()` | Detiene el programa hasta que se presione el botón. |
| `while True` | Repite el ciclo para siempre. |
| `def estado_autos()` | Función que agrupa acciones para no repetir código. |

## Probarlo sin Raspberry Pi (simulación)

`gpiozero` incluye un modo simulado que permite ejecutar el mismo código en cualquier PC con Python, sin hardware. Instalación:

```bash
pip install gpiozero
```

Guarda este archivo como `semaforo_simulado.py` junto a tu código. Simula el botón y muestra los estados en pantalla:

```python
import os
os.environ["GPIOZERO_PIN_FACTORY"] = "mock"   # pines simulados

from threading import Timer
from time import sleep
from gpiozero import LED, Button, Buzzer, Device

rojo, amarillo, verde = LED(17), LED(27), LED(22)
buzzer = Buzzer(23)
boton = Button(24, bounce_time=0.1)

def estado_autos():
    rojo.off(); amarillo.off(); verde.on()

def cruce_peatonal():
    verde.off()
    amarillo.on(); print("Amarillo encendido:", amarillo.value); sleep(1)
    amarillo.off()
    rojo.on(); print("Rojo encendido:", rojo.value)
    buzzer.beep(on_time=0.1, off_time=0.1, n=5, background=False)
    rojo.off()
    estado_autos(); print("Verde encendido:", verde.value)

def presionar_boton():
    pin = Device.pin_factory.pin(24)
    pin.drive_low(); sleep(0.2); pin.drive_high()   # simula pulsación

estado_autos()
print("Verde encendido:", verde.value)
Timer(2, presionar_boton).start()   # "presiona" el botón a los 2 segundos
boton.wait_for_press()
cruce_peatonal()
```

Así puedes practicar la lógica aunque no tengas la placa. No verás luces, pero sí el estado (`1` = encendido, `0` = apagado) de cada salida.

## Errores comunes

| Problema | Causa probable | Solución |
|---|---|---|
| El LED no enciende | Está al revés (polaridad) | Invierte las patas del LED |
| El LED no enciende | Cable en un pin distinto al del código | Revisa BCM vs número físico |
| El botón no responde | No está conectado a GND | Revisa el cable a tierra |
| El botón "dispara" varias veces | Rebote mecánico | Usa `bounce_time=0.1` |
| `gpiozero.exc.BadPinFactory` | Ejecutas el código en un PC sin modo mock | Corre en la Raspberry o usa el modo simulado |
| `Permission denied` al ejecutar | Archivo o carpeta sin permisos | Revisa que estés en tu carpeta de usuario |
| Todo apagado y nada responde | Falta GND común | Une todos los GND al mismo riel |

## Retos extra

1. Cambia el tiempo del amarillo a 3 segundos y el del cruce a 8 segundos.
2. Haz que el LED amarillo **parpadee** durante la fase amarilla (`amarillo.blink()`).
3. Agrega un **LED verde peatonal** (un cuarto LED en otro GPIO) que encienda mientras el rojo de los autos está encendido.
4. Cuenta cuántos peatones han cruzado e imprime el total cada vez.
5. Ignora el botón si ya hay un cruce en curso.

## Entrega

Guarda tu código con el formato `CARNE_Nombre_Proyecto.py`, por ejemplo `202301234_JuanPerez_Taller1.py`, y envíalo por el medio que indiquen los tutores.