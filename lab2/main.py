# Выполнить обработку элементов прямоугольной матрицы A,
# имеющей N строк и M столбцов. Все элементы имеют целый тип.
# Дано целое число H. Определить,
# какие столбцы имеют хотя бы одно такое число,
# а какие не имеют.

import numpy


def calculate(n, m, h, out):
    matrix = numpy.random.randint(0, 10, (n, m))
    res = []

    for i in matrix:  # Запись матрицы в файл
        for j in i:
            out.write(str(j) + " ")
        out.write("\n")

    for i in matrix:  # Поиск значений
        for j in range(len(i)):
            if j in res:
                continue
            if i[j] == h:
                res.append(j)

    return res


def action(path):
    out = open(path, 'w', encoding="UTF-8")
    n, m, h = map(int, input("Введите n(кол-во строк) m(кол-во столбцов) h(искомое число): ").split())
    res = calculate(n, m, h, out)
    if res:
        out.write("\nЗначение было найдено в столбцах:\n")
        for i in res:
            out.write(str(i) + " ")
    else:
        out.write("\nЗначение не найдено(")


if __name__ == '__main__':
    action("output.txt")
