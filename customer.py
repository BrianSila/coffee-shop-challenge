from order import Order

class Customer():
    
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 25 characters")
        
    def orders(self):
        return self._orders.copy()

    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

    