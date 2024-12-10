from src.v2.pizza import Pizza
 
class Sausage(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def calculate_price(self):
        return self.pizza.get_price() + 1.5
    def is_veggetarian(self):
        return False