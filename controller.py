from model import Model, DecodeError
from view import View

class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model()
        except DecodeError as e:
            self.view.__throw_an_error__(e)

    def run(self):
        query = None
        while query != 'Выход':
            query = self.view.wait_user_answer()
            self.check_user_answer(query)

    def check_user_answer(self, query):
        if query == '1':
            footwear_data = self.view.add_new_footwear()
            self.model.add_new_footwear(footwear_data)
        elif query == '2':
            all_footwear_pairs = self.model.footwear_pairs
            self.view.print_footwear_pairs(all_footwear_pairs)
        elif query == '3':
            criteria = self.view.find_footwear_pairs()
            footwear_pairs = self.model.find_footwear_pairs(criteria)
            self.view.print_footwear_pairs(footwear_pairs)
        elif query == '4':
            footwear_name = self.view.get_footwear_name()
            footwear_pairs = self.model.find_footwear_pairs([footwear_name])
            result = self.model.delete_footwear(footwear_pairs)
            if result == 'Слишком много пар обуви':
                self.view.print_footwear_pairs(footwear_pairs)
                number = self.view.get_deletion_context()
                result = self.model.delete_footwear([footwear_pairs[number - 1]])
            self.view.return_delete_result(result)