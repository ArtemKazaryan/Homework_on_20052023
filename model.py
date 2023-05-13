import json

class Footwear:
    def __init__(self, type, variety, color, price, manufacturer, size):
        self.type = type
        self.variety = variety
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return f'{self.type} - {self.variety}'

class DecodeError(Exception):
    pass

class Model:
    def __init__(self):
        self.filepath = 'db.txt'
        self.__footwear_pairs = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for footwear in self.data.values():
                self.__footwear_pairs[f'{footwear["type"]} {footwear["variety"]}'] = Footwear(*footwear.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')

    @property
    def footwear_pairs(self):
        return self.__footwear_pairs

    def save_footwear_pairs(self):
        dict_footwear_pairs = {footw.title: footw.__dict__ for footw in self.__footwear_pairs.values()}
        json.dump(dict_footwear_pairs, open(self.filepath, 'w', encoding='utf-8'))

    def add_new_footwear(self, footwear_data):
        new_footwear = Footwear(*footwear_data.values())
        self.__footwear_pairs[f'{new_footwear.type} {new_footwear.variety}'] = new_footwear
        self.save_footwear_pairs()

    def find_footwear_pairs(self, criteria):
        footwear_pairs = []
        for footwear in self.__footwear_pairs.values():
            for crit in criteria:
                if footwear in footwear_pairs:
                    break
                for prop in footwear.__dict__.values():
                    if crit.lower() in prop.lower():
                        footwear_pairs.append(article)
                        break

        return footwear_pairs

    def delete_footwear(self, footwear_pairs):
        if len(footwear_pairs) == 0:
            return "Такой обуви не было найдено!"
        elif len(footwear_pairs) == 1:
            footwear = footwear_pairs[0]
            key = f'{footwear.type} {footwear.variety}'
            self.__footwear_pairs.pop(key)
            self.save_footwear_pairs()
            return 'Пара обуви была удалена!'
        else:
            return 'Слишком много пар обуви'