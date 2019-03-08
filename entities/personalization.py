from entities import radio_station

class Personalization:

    def __init__(self, do_not_disturb, temperature):
        self.radio_station = radio_station.RadioStation()
        self.do_not_disturb = do_not_disturb
        self.temperature = temperature

    @property
    def radio_station(self):
        return self.radio_station

    @radio_station.setter
    def radio_station(self, value):
        self.radio_station = value

    @property
    def do_not_disturb(self):
        return self.do_not_disturb

    @do_not_disturb.setter
    def do_not_disturb(self, value):
        self.do_not_disturb = value

    @property
    def temperature(self):
        return self.temperature

    @temperature.setter
    def temperature(self, value):
        self.temperature = value
