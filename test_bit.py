import spidev
import time

SPI_BUS = 0
SPI_DEVICE = 0  # usa CE0

spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 100000  # 100 kHz para estar tranquilos
spi.mode = 0  # CPOL=0, CPHA=0

while True:
    spi.xfer2([0x55])  # manda cualquier byte
    print("Enviado 0x55")
    time.sleep(1)
