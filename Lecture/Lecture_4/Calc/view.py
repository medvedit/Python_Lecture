# view - юзер интерфейс. Обеспечиваем взаимодействие с пользователем. Создаем кнопочку, которую пользователь будет нажимать.

def view_data(data, title): # data - заходят данные
    print(f'{title} = {data}') # Выводим данные на экран

def get_value():
    return int(input('Введите число -> '))