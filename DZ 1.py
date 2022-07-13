
def InputNumbers(inputText):
    is_DN = False
    while not is_DN:
        try:
            number = int(input(f"{inputText}"))
            is_DN = True
        except ValueError:
            print("Ты помоему перепутал!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes")
    elif 0 < num < 6:
        print("No")
    else:
        print("Впервые вижу это число")


num = InputNumbers("Введите число: ")
checkNumber(num)