import time


class Position:

    def __init__(self, pos, latitude, longitude, width, length):
        self.pos = int(pos)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.width = float(width)
        self.length = float(length)


class WeatherData(Position):

    def __init__(self, pos=-1, latitude=0.0, longitude=0.0, width=0.0, length=0.0, precipitation=0.0,
                 date=time.strftime("%Y-%m-%d %H:%M")):
        super().__init__(pos, latitude, longitude, width, length)
        self.precipitation = precipitation
        self.date = date
        if self.pos == -1:
            WeatherData.last_n(self)

    def __repr__(self):
        return f"WeatherData(id={self.pos}, lat={self.latitude}, long={self.longitude}, width={self.width}, " \
               f"length={self.length}, precipitation={self.precipitation}, date={self.date})"

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getitem__(self, index):
        return [self.pos, self.latitude, self.longitude, self.width, self.length, self.precipitation, self.date][index]

    def __iter__(self):
        return iter([self.pos, self.latitude, self.longitude, self.width, self.length, self.precipitation, self.date])

    @classmethod
    def from_string(cls, string):
        _id, lat, long, width, length, precipitation, date = string.strip().split(",")
        return cls(int(_id), float(lat), float(long), float(width), float(length), float(precipitation), date)

    def generator(self):
        for i in self:
            yield i

    def last_n(self):
        ar = read_from()
        if ar:
            n = ar[-1].pos + 1
        else:
            n = 1
        self.pos = n


def read_from(path="table.csv"):
    csvfile = open(path, 'r+', newline='')
    _list = []
    if csvfile != 0:
        for i in csvfile.readlines():
            _list.append(WeatherData.from_string(i))
        return _list
    else:
        return 0


def sorter(list_reader):
    print("Сортировка по строке (дате):")
    for i in sorted(list_reader, key=lambda d: d.date, reverse=True):
        print(i)

    print("\nСортировка по числу (мм/ч):")
    for i in sorted(list_reader, key=lambda d: float(d.precipitation)):
        print(i)

    print("\nВывод данных значения об осадках которых превышают 5:")
    for i in list_reader:
        if float(i.precipitation) > 5:
            print(i)

if __name__ == '__main__':
    weather = WeatherData()

    weather.latitude = 11  # Проверка __setatr__
    weather.longitude = 7.2
    weather.length = 4
    weather.width = 12
    weather.precipitation = 7

    print(weather, "Проверка __repr__\n")  # Проверка __repr__

    print(weather[2], "Проверка __getitem__\n")  # Проверка __getitem__

    for i in weather:  # Проверка __iter__
        print(i, end=' ')
    print("Проверка __iter__\n")

    print(weather.generator(), "Проверка generator")  # Проверка generator
    print(*weather.generator(), "\n")

    print(read_from())  # Проверка static метода


