import weather
import csv


def write(weather_obj):
    csvfile = open('table.csv', 'a', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(weather_obj)
    csvfile.close()


def out():
    list_reader = weather.read_from()
    weather.sorter(list_reader)


if __name__ == '__main__':
    do = int(input("Вывод csv - 1\tДобавить в csv - 2\n"))
    if do == 1:
        out()
    else:
        weather_obj = weather.WeatherData()
        latitude, longitude, width, length, mm_h = map(float, input("Введите параметры: широта, "
                                                                    "долгота, ширина, длина, "
                                                                    "кол-во мм в час: ").split())
        weather_obj.latitude = latitude
        weather_obj.longitude = longitude
        weather_obj.width = width
        weather_obj.length = length
        weather_obj.precipitation = mm_h

        print(weather_obj)
        write(weather_obj)


