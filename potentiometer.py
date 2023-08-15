from analogInput import AnalogInput


class Potentiometer(AnalogInput):
    def read_step(self, steps=20):
        # Returns a value between 1 and steps (inclusive)
        step_val = 65535 // (steps - 1)
        return (self.read() // step_val) + 1
