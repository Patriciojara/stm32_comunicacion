import spidev
import time

SPI_BUS = 0
SPI_DEVICE = 0

CMD_SET_DUTY_ON = 0xA0
CMD_PWM_OFF     = 0xA1

spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 100000  # 100 kHz
spi.mode = 0  # CPOL=0, CPHA=0

def send_set_duty(duty):
    # limitar entre 0 y 100
    duty = max(0, min(100, int(duty)))
    spi.xfer2([CMD_SET_DUTY_ON, duty])
    print(f"Enviado: SET DUTY {duty}% y ON")

def send_pwm_off():
    spi.xfer2([CMD_PWM_OFF, 0])
    print("Enviado: PWM OFF")

def main():
    while True:
        txt = input("d=<0-100> (duty y ON), off, q: ").strip().lower()

        if txt == 'q':
            break
        elif txt == 'off':
            send_pwm_off()
        elif txt.startswith('d='):
            try:
                val = int(txt[2:])
                send_set_duty(val)
            except ValueError:
                print("Formato: d=50, d=75, etc.")
        else:
            print("Comandos: d=NN, off, q")

if __name__ == "__main__":
    main()
