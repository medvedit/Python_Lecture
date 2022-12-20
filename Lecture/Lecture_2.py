# Файлы ====================================================================================================================
# Хранение данных
# Передача данных в клиент-серверных проектах
# Хранение конфигов
# Логирование действий
# *********************************************
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+
# *********************************************
# один из вариантов создания файла, работы с ним, с автомотическим разрывом соединения по зваершении работы кода.
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
# ************************************
# один из вариантов создания файла, работы с ним, с принудительным закрытием связи с файлом .txt путем команды data.close()
exit() # отключает выполнение кода ниже.
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w') # Создаем файл file.txt , создается он в корневой, первой папке.
data.writelines(colors) # Заносим текст из переменной colors, разделителей не будет.
                        # Приповторном запуске, данные будут дописываться.
data.write('\n112233\n')
data.write('445566\n')
data.close() # Закрываем, разрываем связь с файлот file.txt .
# ***********************************

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()