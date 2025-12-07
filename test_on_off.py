import spidev
import time

SPI_BUS = 0
SPI_DEVICE = 0

spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 500000
spi.mode = 0  # CPOL=0, CPHA=0

while True:
    cmd = input("1 = 0xA5 (ON), 0 = 0x5A (OFF), q = salir: ").strip()
    if cmd == '1':
        spi.xfer2([0xA5])
    elif cmd == '0':
        spi.xfer2([0x5A])
    elif cmd.lower() == 'q':
        break
