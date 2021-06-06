import numpy


def super_sort(rows, cols):
    A = numpy.random.randint(1, 100, (rows, cols))
    B = numpy.copy(A)
    print('A\n', A, '\n')
    print('B\n', B, '\n')

    B[:, ::2] = -numpy.sort(-B[:, ::2], axis=0)
    B[:, 1::2] = numpy.sort(B[:, 1::2], axis=0)

    print(B)


x = int(input("Введите длинну"))
y = int(input("Введите ширину"))
super_sort(x, y)
