import csv
import datetime
import os


def get_files():
    files = os.listdir(path=".")
    for i in files:
        print(i)
    return len(files)


def get_last_n():
    f = open('table.csv', 'r', newline='')
    reader = csv.reader(f)
    n = 0
    for i in reader:
        n = int(i[0])

    n += 1
    f.close()

    return n


def get_date():
    now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    return now


def write(latitude, longitude, width, length, mm_h):
    csvfile = open('table.csv', 'a', newline='')
    fieldnames = ['N', 'latitude', 'longitude', 'width', 'length', 'mm/h', 'date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow({'N': get_last_n(), 'latitude': latitude, 'longitude': longitude,
                     'width': width, 'length': length, 'mm/h': mm_h, 'date': get_date()})

    csvfile.close()


def out():
    csvfile = open('table.csv', 'r+', newline='')
    fieldnames = ['N', 'latitude', 'longitude', 'width', 'length', 'mm/h', 'date']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)

    list_reader = []
    for i in reader:
        list_reader.append(i)

    print("Сортировка по строке (дате):")
    for i in sorted(list_reader, key=lambda d: d['date']):
        print(i)

    print("\nСортировка по числу (мм/ч):")
    for i in sorted(list_reader, key=lambda d: float(d['mm/h']), reverse=True):
        print(i)

    print("\nВывод данных значения об осадках которых превышают 5:")
    for i in list_reader:
        if float(i['mm/h']) > 5:
            print(i)

    csvfile.close()


if __name__ == '__main__':
    do = int(input("Показать файлы - 1\tВывод csv - 2\tДобавить в csv - 3\n"))
    if do == 1:
        print(get_files())
    elif do == 2:
        out()
    else:
        latitude, longitude, width, length, mm_h = map(float, input("Введите параметры: широта, "
                                                                    "долгота, ширина, длина, "
                                                                    "кол-во мм в час: ").split())
        write(latitude, longitude, width, length, mm_h)

