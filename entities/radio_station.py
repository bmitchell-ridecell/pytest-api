class RadioStation:

    def __init__(self, radio_station_id, frequency, genre, name):
        self.radio_station_id = radio_station_id
        self.frequency = frequency
        self.genre = genre
        self.name = name

    @property
    def radio_station_id(self):
        return self.radio_station_id

    @radio_station_id.setter
    def radio_station_id(self, value):
        self.radio_station_id = value

    @property
    def frequency(self):
        return self.frequency

    @frequency.setter
    def frequency(self, value):
        self.frequency = value

    @property
    def genre(self):
        return self.genre

    @genre.setter
    def genre(self, value):
        self.genre = value

    @property
    def name(self):
        return self.name

    @id.setter
    def name(self, value):
        self.name = value
