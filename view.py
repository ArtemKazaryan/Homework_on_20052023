def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '*'))
            result = func(*args, **kwargs)
            print('=' * 50)
            return result
        return wrapper
    return decorator

class View:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('*' * 50)
        print('Ожидание пользовательского ввода: '.center(50, '='))
        print('Доступные действия:\n'
              '1. Добавить новую обувь\n'
              '2. Отобразить все пары обуви\n'
              '3. Найти обувь\n'
              '4. Удалить обувь\n'
              'Выход. Завершить программу')
        print('*' * 50)
        query = input('Введите номер действия: ')
        return query

    def add_new_footwear(self):
        dict_footwear = {'Тип обуви (мужская/женская)': None,
                        'Вид обуви (кроссовки, сапоги, сандалии, туфли и т.д)': None,
                        'Цвет': None,
                        'Цена': None,
                        'Производитель': None,
                        'Размер': None}
        for key in dict_footwear.keys():
            dict_footwear[key] = input(f'Введите {key.lower()} обуви: ')
        return dict_footwear

    @add_title('Неизвестная ошибка')
    def __throw_an_error__(self, error):
        print('Произошла какая-то ошибка:', error)

    @add_title('Список обуви')
    def print_footwear_pairs(self, footwear_pairs):
        if footwear_pairs:
            [print(i + 1, footwear) for i, footwear in enumerate(footwear_pairs)]
        else:
            print('Ни одной пары обуви нет!')

    @add_title('Поиск обуви')
    def find_footwear_pairs(self):
        criteria = input('Введите список слов для поиска через пробел: ').split()
        return criteria

    @add_title('Дополнительная информация')
    def get_deletion_context(self):
        number = int(input('Введите номер пары обуви для удаления: '))
        return number

    @add_title('Результат удаления')
    def return_delete_result(self, result):
        print(result)