from machine import ADC


class AnalogInput:
    def __init__(self, pin):
        self.adc = ADC(pin.upper())

    def read(self):
        # read value, in range 0-65535
        return self.adc.read_u16()

    def read_percentage(self):
        # read value, in range 0-100
        return int(self.read() / 65535 * 100)
