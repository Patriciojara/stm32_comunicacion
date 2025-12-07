import spidev
import time

SPI_BUS = 0
SPI_DEVICE = 0

CMD_SET_DUTY_ON = 0xA0
CMD_PWM_OFF     = 0xA1
CMD_SET_FREQ    = 0xA2

spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 100000  # 100 kHz
spi.mode = 0  # CPOL=0, CPHA=0

def send_set_duty(duty):
    duty = max(0, min(100, int(duty)))
    spi.xfer2([CMD_SET_DUTY_ON, duty, 0])
    print(f"Enviado: SET DUTY {duty}% y ON")

def send_pwm_off():
    spi.xfer2([CMD_PWM_OFF, 0, 0])
    print("Enviado: PWM OFF")

def send_set_freq(freq_hz):
    freq_hz = max(20, min(20000, int(freq_hz)))
    hi = (freq_hz >> 8) & 0xFF
    lo = freq_hz & 0xFF
    spi.xfer2([CMD_SET_FREQ, hi, lo])
    print(f"Enviado: SET FREQ {freq_hz} Hz")

def main():
    print("Comandos:")
    print("  d=NN    -> duty % y ON (ej: d=30)")
    print("  f=NNNN  -> frecuencia Hz (ej: f=1000)")
    print("  off     -> apagar PWM")
    print("  q       -> salir")

    while True:
        txt = input("> ").strip().lower()

        if txt == 'q':
            break
        elif txt == 'off':
            send_pwm_off()
        elif txt.startswith('d='):
            try:
                val = int(txt[2:])
                send_set_duty(val)
            except ValueError:
                print("Formato: d=50")
        elif txt.startswith('f='):
            try:
                val = int(txt[2:])
                send_set_freq(val)
            except ValueError:
                print("Formato: f=1000")
        else:
            print("Comandos: d=NN, f=NNNN, off, q")

if __name__ == "__main__":
    main()
