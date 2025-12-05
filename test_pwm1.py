import spidev
import time

# Configuración SPI0 (la estándar de la Raspberry)
SPI_BUS = 0
SPI_DEVICE = 0   # CE0

# Comandos
CMD_PWM_ON  = 0xA5
CMD_PWM_OFF = 0x5A

def init_spi():
    spi = spidev.SpiDev()
    spi.open(SPI_BUS, SPI_DEVICE)
    spi.max_speed_hz = 500000  # 500 kHz (puedes subir luego)
    spi.mode = 0               # SPI mode 0: CPOL=0, CPHA=0
    spi.bits_per_word = 8
    return spi

def send_command(spi, cmd):
    # enviamos un solo byte
    spi.xfer2([cmd])
    print(f"Comando enviado: 0x{cmd:02X}")
    # pequeña espera para no saturar
    time.sleep(0.05)

def main():
    spi = init_spi()
    try:
        while True:
            opcion = input("Pulsa 1=PWM ON, 0=PWM OFF, q=salir: ").strip()
            if opcion == "1":
                send_command(spi, CMD_PWM_ON)
            elif opcion == "0":
                send_command(spi, CMD_PWM_OFF)
            elif opcion.lower() == "q":
                break
            else:
                print("Opción no válida.")
    finally:
        spi.close()
        print("SPI cerrado.")

if __name__ == "__main__":
    main()
