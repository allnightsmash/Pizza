from src.v2.pizza import Pizza
 
class StuffedCrust(Pizza):
    def is_veggetarian(self):
        return True
    def get_price(self):
        return 8.0