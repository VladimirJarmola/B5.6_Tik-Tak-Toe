print('Добро пожаловать в игру "Крестики - Нолики"!\n')
input_1pl = input('Введите имя первого игорока или нажмите Enter, по умолчанию Player_1:  ')
input_2pl = input('Введите имя второго игрока или нажмите Enter, по умолчанию Player_2:  ')
player_1 = input_1pl if input_1pl else 'player_1' # имя игрока по умолчанию
player_2 = input_2pl if input_1pl else 'player_2' # имя игрока по умолчанию
# создаем матрицу - игровое поле
def field_maker():
    column = 3
    row = 3 # размер игрового поля 3х3
    field_local = [['-'] * row for i in range(column)]
    return field_local
field = field_maker()
#Создаем функцию, выводящую наше поле на экран
def output(field):
    output_0str = '  0 1 2'
    output_1str = '0 ' + ' '.join(field[0])
    output_2str = '1 ' + ' '.join(field[1])
    output_3str = '2 ' + ' '.join(field[2])
    print('\n', output_0str, output_1str, output_2str, output_3str, '\n', sep = '\n' )
    return field
output(field) # выводим на экран пустое игровое поле
print('Ход осуществляется при помощи ввода координаты ячейки в консоль следующим образом:\n 0 0, 2 1')
print('Где первое число - это номер строки, второй - номер столбца\n')
print(f'{player_1} ходит первым')
# Функция ввода координат хода игрока
def step(pl):
    step1 = input(f'Сделайте Ваш ход, {pl}:  ')
    if len(step1) == 3 and step1[1] == ' ' and field[int(step1[0])][int(step1[2])] == '-':
        if 0 <= int(step1[0]) <= 2 and 0 <= int(step1[2]) <= 2:  # Проверяем корректность ввода
            return step1
        else:
            print('Не корректный ввод, попробуйте еще раз')
            return step(pl)
    else:
        print('Не корректный ввод, попробуйте еще раз')
        return step(pl)
# Проверка победителя
def check_winner():
    if field[0][0] == field[0][1] == field[0][2] != '-':
        return True
    elif field[1][0] == field[1][1] == field[1][2] != '-':
        return True
    elif field[2][0] == field[2][1] == field[2][2] != '-':
        return True
    elif field[0][0] == field[1][0] == field[2][0] != '-':
        return True
    elif field[0][1] == field[1][1] == field[2][1] != '-':
        return True
    elif field[0][2] == field[1][2] == field[2][2] != '-':
        return True
    elif field[0][0] == field[1][1] == field[2][2] != '-':
        return True
    elif field[2][0] == field[1][1] == field[0][2] != '-':
        return True
#Функция хода игры
def game():
    for i in range(0, 4):
        if check_winner(): # Проверка наличия победителя перед началом итерации
            break
        for j in range(0, 2):
            if j == 0:
                step_cord = step(player_1) # запускаем функцию ввода координат
                row_0 = int(step_cord[0])
                column_0 = int(step_cord[2])
                field[row_0][column_0] = 'X' # присваеваем значение полю если оно свободно
                output(field) # выводим на экран изменение ситуации
                if check_winner(): # проверяем наличие победителя
                    print(f'Игрок {player_1} победил!!!\n')
                    break # Игрок победил - выходим из цыкла
            if j == 1: # тоже для игрока 2
                step_cord = step(player_2)
                row_0 = int(step_cord[0])
                column_0 = int(step_cord[2])
                field[row_0][column_0] = '0'
                output(field)
                if check_winner():
                    print(f'Игрок {player_2} победил!!!\n')
                    break
game_progress = 'y'
while game_progress == 'y':
    field = field_maker()
    game()
    game_progress = input('Хотите сыграть еще раз? (y):  ')
print('\nСпасибо за игру!')