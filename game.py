import random

def show_instructions():
    print("Добро пожаловать в Лабиринт!")
    print("Ты находишься в лабиринте и должен найти выход.")
    print("Выбери направление, чтобы двигаться: 'вперед', 'назад', 'влево', 'вправо'.")
    print("Остерегайся ловушек и выбирай свой путь осторожно!")
    print()

def choose_direction():
    direction = input("Куда ты хочешь пойти? (вперед/назад/влево/вправо): ").lower()
    if direction in ['вперед', 'назад', 'влево', 'вправо']:
        return direction
    else:
        print("Неправильное направление! Пожалуйста, выбери одно из доступных направлений.")
        return choose_direction()

def play_game():
    show_instructions()
    # Начинаем игру в центре лабиринта
    current_location = (0, 0)
    while True:
        print("Ты находишься на координатах:", current_location)
        direction = choose_direction()
        # Случайным образом меняем местоположение игрока
        if direction == 'вперед':
            current_location = (current_location[0], current_location[1] + 1)
        elif direction == 'назад':
            current_location = (current_location[0], current_location[1] - 1)
        elif direction == 'влево':
            current_location = (current_location[0] - 1, current_location[1])
        elif direction == 'вправо':
            current_location = (current_location[0] + 1, current_location[1])
        # Проверяем, не достиг ли игрок выхода
        if current_location == (3, 3):
            print("Поздравляем! Ты нашел выход из лабиринта!")
            break

play_game()
