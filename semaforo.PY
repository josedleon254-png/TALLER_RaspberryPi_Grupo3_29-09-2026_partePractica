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
