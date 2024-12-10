from src.v2.pizza import Pizza
 
class Pepperoni(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def calculate_price(self):
        return self.pizza.get_price() + 4
    def is_dairy_free(self):
        return True
    def is_veggetarian(self):
        return False
    