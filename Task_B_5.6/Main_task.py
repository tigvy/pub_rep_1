# ЗАДАНИЕ:
# Создать игру крестики-нолики.
# Консоль, куда будет выводиться ход игры. С помощью форматированных строк.
# ------------------------------------------------------------------------

# БЛОК 0. ВВОДНЫЕ ПЕРЕМЕННЫЕ:
main_board = [ # Основное поле игры, заданное условиями задачи.
     ['-', '-', '-'],
     ['-', '-', '-'],
     ['-', '-', '-']
]
start_game_board = main_board.copy() # Стартовое поле игры. Созадем через копию основного
# поля игры, чтобы исходное поле игры случайно не испортить.
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# >>>>> БЛОК 1. (начало). Печатаем сообщение о начале игры и печатаем стартовое поле игры
print('Начинается игра!')

def current_gboard(list_): # Функций показывает вид текущего поля игры.
    print('Текущий вид поля игры:')
    cur_game_board = []
    for i in start_game_board:
        cur_game_board.append(i)
        print(i)
    return cur_game_board

gb = current_gboard(start_game_board) # Создаю переменную текущего game board,
# через функцию current_gboard(start_game_board). В последствии переменная gb будет меняться,
# через контролер ввода символов игроков.
print('---------------------------------------')
# <<<<< БЛОК 1. (конец).
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# >>>>> БЛОК ПРОВКЕРОК. Проверки выигрыша игроков.
# >>>>> ПРОВЕРКА 1 (начало) - проверка совпадения всех символов по строке прямо.
def func_win_line(list_):
    counter_simbol_x = 0
    counter_simbol_o = 0
    simbol_1, simbol_2 = 'х', 'о'
    for row in list_: # Проходим по строкам
        for element_to_check in row: # Проходим по символам в строке
            if element_to_check == simbol_1: # если символ игрока 1 попадается,
                counter_simbol_x += 1 # то добавляем его в счетчик "x"
                if counter_simbol_x == counter_column: # если кол-во символов
                    # в счетчике 'х' равно кол-ву столбцов, то условие победы выполнено.
                    print('---------------------------------------')
                    print('Победил Игрок 1. Символы совпали по строке прямо.')
                    return True
            else:
                if element_to_check == simbol_2: # если символ игрока 2 попадается,
                    counter_simbol_o += 1 # то добавляем его в счетчик "o"

                    if counter_simbol_o == counter_column:
                        print('---------------------------------------')
                        print('Победил Игрок 2. Символы совпали по строке прямо.')
                        return True

        counter_simbol_x = 0 # Если в строке не совпали все символы "x", обнуляем счетчик "x".
        counter_simbol_o = 0 # Если в строке не совпали все символы "о", обнуляем счетчик "о".

# <<<<< ПРОВЕРКА 1 (конец). ГОТОВО.
# --------------------------------------------------------------------------

# >>>>> ПРОВЕРКА 2 (начало) - проверка совпадения всех символов по диагонали массива.
def func_win_diog(list_):
    counter_simbol_x = 0
    counter_simbol_o = 0
    simbol_1, simbol_2 = 'х', 'о'
    step = 0 # Шаг смещения по следующей строке
    for row in list_:
        element_to_check = list_[step][step]
        if element_to_check == simbol_1:
            counter_simbol_x += 1
        if counter_simbol_x == counter_row:
            print('---------------------------------------')
            print('Победил Игрок 1')
            return True
        else:
            if element_to_check == simbol_2:
                counter_simbol_o += 1

            if counter_simbol_o == counter_row:
                print('---------------------------------------')
                print('Победил Игрок 2.')
                return True
        step += 1
# <<<<< ПРОВЕРКА 2 (конец). ГОТОВО.
# --------------------------------------------------------------------------

# >>>>> ПРОВЕРКА 3 (начало) - проверка совпадения всех символов по диагонали (обратной) массива.
def func_win_diog_reverse(list_):
    list_reverse = []
    for row in list_:
        list_reverse.append(list(reversed(row)))

    counter_simbol_x = 0
    counter_simbol_o = 0
    simbol_1, simbol_2 = 'х', 'о'
    step = 0 # Шаг смещения по следующей строке
    for row in list_reverse:
        element_to_check = list_reverse[step][step]
        if element_to_check == simbol_1:
            counter_simbol_x += 1
        if counter_simbol_x == counter_row:
            print('---------------------------------------')
            print('Победил Игрок 1. Символы совпали по обратной диагонали.')
            return True
        else:
            if element_to_check == simbol_2:
                counter_simbol_o += 1

            if counter_simbol_o == counter_row:
                print('---------------------------------------')
                print('Победил Игрок 2. Символы совпали по обратной диагонали.')
                return True
        step += 1
# <<<<< ПРОВЕРКА 3 (конец). ГОТОВО.
# --------------------------------------------------------------------------

# >>>>> ПРОВЕРКА 4 (начало) - совпадения всех символов по столбцу массива.
def func_win_column(list_):
    list_reverse = [[],[],[]]
    for i in range(len(list_)):
        for q in range(len(list_)-1, -1, -1):
            b=list_[q][i]
            list_reverse[i].append(b)



    counter_simbol_x = 0
    counter_simbol_o = 0
    simbol_1, simbol_2 = 'х', 'о'
    step_row = 0
    step_column = 0

    for row in list_: # проходимся по строкам
        element_to_check = list_[step_row][step_row]
        if element_to_check == simbol_1:
            counter_simbol_x += 1
        step_row += 1

        if counter_simbol_x == counter_column:
            print('---------------------------------------')
            print('Победил Игрок 1. Символы совпали по столбцу.')
            return True
    step_column += 1


# <<<<< ПРОВЕРКА 4 (конец).
# --------------------------------------------------------------------------

# >>>>> БЛОК 2 (начало). Счиатем количество ходов и печатаем сообщение о количестве ходов.
# Считаем соличество строк и столбцов в массиве.

counter_motion = 0
counter_row = 0
counter_column = 0
for i in gb:
        counter_row += 1
        counter_column += 1
        pluser = i.count("-")
        counter_motion += pluser

print(f'Всего в игре: {counter_motion} ходов.')
print('---------------------------------------')
# <<<<< БЛОК 2. (конец).
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# >>>>> БЛОК 3. Выводим инфо о том, чей сейчас ход.
# Функция вставки символа в игровое поле.
def add_simbol(simbol):
    add_row = int(input(f'Введите порядковый номер строки, от 1 до {counter_row}, для ввода символа:'))-1
    add_column = int(input(f'Введите порядковый номер стобца, от 1 до {counter_column}, для ввода символа:'))-1

    if [add_row, add_column] in previous_motion: # здесь проверка на заполнение в пустое поле.
        print('Заполняемое поле не является свободным. Введите порядковый номер строки и столбца заново.')
    else:
        previous_motion.append([add_row, add_column])
        list_from_row = gb[add_row]
        string_from_list__from_row = list_from_row[add_column]
        gb[add_row].pop(add_column)
        gb[add_row].insert(add_column, simbol)
        return True # Если символ игрока заполняется в сводобное поле, то True.
        # Это далее пригодится в цикле while.
# <<<<< БЛОК 3. (конец).
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# >>>>> БЛОК 4. Контролер. Переключает игроков, в зависисоти от общего количества ходов - по очереди.

n = counter_motion # Передаем общее кол-во ходов и игре (из БЛОКА 2).
counter = n # Счетчик оставшихся ходов.
# if counter == 0: # Условие выхода из игры по завершению ходов. - ЭТО НЕ РАБОТАЕТ.
#     print('Конец игры. Закончились ходы.')

previous_motion = [] # Сбор инфо о ранее введенных ходах игроков.
# Для последующего контроля ввода в пустое поле.

while n != 0: # Основной цикл. Работает, пока не закончятся ходы.

    if counter > 0 and counter % 2 == 1: # Если кол-во ходов нечетное,
        # то начинает ходить Игрок 1. Далее переключение по очереди.
        print('Ход Игрока 1. Игрок ходит крестиками = x.')
        simbol = 'х'

        result = add_simbol(simbol) # Передача True из БЛОКА 3, если символ вводился в пустое поле.
        if result:
            print('---------------------------------------')
            current_gboard(gb) # Запускаем функцию из БЛОКА 1 - обновление текущего поля игры, его вывод.
            if func_win_line(gb) or func_win_diog(gb) or func_win_diog_reverse(gb) or func_win_column(gb): # Условия проверки выигрыша игроков.
                # Запускаем функцию из БЛОКА ПРОВЕРОК.
                print('Игра закончилась.')
                print('---------------------------------------')
                break


            print(f'Осталось: {counter - 1} ходов, из {n}.')
            print('---------------------------------------')
            counter -= 1 # убираем один ход.

        else:
            print('---------------------------------------')
            print(f'Осталось: {counter} ходов, из {n}.')
            current_gboard(gb)
            print('---------------------------------------')
    elif counter > 0 and counter % 2 == 0:
        print('Ход Игрока 2. Игрок ходит ноликами = о.')
        simbol = 'о'

        result = add_simbol(simbol)
        if result:
            print('---------------------------------------')
            current_gboard(gb)
            if func_win_line(gb) or func_win_diog(gb) or func_win_diog_reverse(gb) or func_win_column(gb) or ((counter-1) == 0):# Условия проверки выигрыша игроков.
                # Запускаем функцию из БЛОКА ПРОВЕРОК.
                print(f'Игра закончилась.')
                print('---------------------------------------')
                break


            print(f'Осталось: {counter - 1} ходов, из {n}.')
            print('---------------------------------------')
            counter -= 1  # убираем один ход.

        else:
            print('---------------------------------------')
            print(f'Осталось: {counter} ходов, из {n}.')
            current_gboard(gb)
            print('---------------------------------------')


# <<<<< БЛОК 4. (конец).
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

