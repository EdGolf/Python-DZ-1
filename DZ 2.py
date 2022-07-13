
def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_K = False
        while not is_K:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_K = True
                if a[i] == 0:
                    is_K = False
                    print("Неверная координата ")
            except ValueError:
                print("Ты помоему перепутал!")
    return a


def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


koordinate = inputKoord(2)
checkCoordinates(koordinate)