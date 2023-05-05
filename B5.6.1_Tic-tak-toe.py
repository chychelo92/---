def greetings():
    print("Я хочу сыграть с тобой в игру")
    print("Крестики-нолики")
    print("Реши, на чьей ты стороне")
    print("и приступим")
    print("Впиши координаты клетки, куда хотел бы поставиться")
    print("Х - это номер строки, Y - номер столбца")


def gamezone():
    print()
    print("   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(zone):
        row_ = f" {i} | {' | '.join(row)} | "
        print(row_)
        print("----------------")
    print()


def request():
    while True:
        coords = input("Ваш ход: ").split()

        if len(coords) != 2:
            print("Надо ввести две координаты!")
            continue
        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Надо ввести числа!")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Ты ткнул пальцем в небо, а надо в игровое поле!")
            continue

        if zone[x][y] != " ":
            print("Выбери другую клетку, эта занята!")
            continue
        return x, y


def win():

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(zone[i][j])
        if symbols == ["X", "X", "X"] and symbols != " ":
            print('Выиграл "X!"')
            return True
        if symbols == ["O", "O", "O"] and symbols != " ":
            print('Выиграл "O!"')
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(zone[j][i])
        if symbols == ["X", "X", "X"] and symbols != " ":
            print('Выиграл "X!"')
            return True
        if symbols == ["O", "O", "O"] and symbols != " ":
            print('Выиграл "O!"')
            return True

    symbols = []
    for i in range(3):
        symbols.append(zone[i][i])
    if symbols == ["X", "X", "X"] and symbols != " ":
        print('Выиграл "X!"')
        return True
    if symbols == ["O", "O", "O"] and symbols != " ":
        print('Выиграл "O!"')
        return True


    symbols = []
    for i in range(3):
        symbols.append(zone[i][2-i])
    if symbols == ["X", "X", "X"]:
        print('Выиграл "X!"')
        return True
    if symbols == ["O", "O", "O"]:
        print('Выиграл "O!"')
        return True
    return False

greetings()
zone = [[" "] * 3 for i in range(3)]
move = 0
while True:
    gamezone()
    move += 1

    if win():
        break

    if move % 2 == 1:
        print('Ход "Х"')
    else:
        print('Ход "O"')


    x, y = request()

    if move % 2 == 1:
        zone[x][y] = "X"
    else:
        zone[x][y] = "O"


    if move == 9:
        print("Ничья!")
        break









