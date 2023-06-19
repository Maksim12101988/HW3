
# Создаем пустой словарь для хранения записей
phone_book = {}

while True:
    # Считываем команду от пользователя
    command = input("Введите команду (add для добавления записи, search для поиска по фамилии, exit для выхода): ")
    
    if command == "add":
        # Считываем данные о новой записи
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        # Добавляем запись в словарь
        phone_book[surname] = (name, phone_number)
        print("Запись добавлена")
    elif command == "search":
        # Считываем фамилию для поиска
        surname = input("Введите фамилию: ")
        # Ищем записи с этой фамилией
        found = False
        for key, value in phone_book.items():
            if key == surname:
                print(key, value[0], value[1])
                found = True
        if not found:
            print("Записи с такой фамилией не найдены")
    elif command == "exit":
        # Выходим из цикла
        break
    else:
        print("Неизвестная команда")

