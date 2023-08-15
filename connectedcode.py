from kooka import button_a, button_b, button_c, button_d

def connect_analog_input(pin):
    from analogInput import AnalogInput

    analog_in = AnalogInput(pin)
    return analog_in

def connect_potentiometer(pin):
    from potentiometer import Potentiometer

    pot = Potentiometer(pin)
    return pot