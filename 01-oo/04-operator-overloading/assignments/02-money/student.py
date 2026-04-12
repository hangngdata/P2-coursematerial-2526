class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if other.currency.lower() == self.currency.lower():
            return Money(
                self.amount + other.amount,
                self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __sub__(self, other):
        if other.currency.lower() == self.currency.lower():
            return Money(
                self.amount - other.amount,
                self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __mul__(self, factor):
        if isinstance(factor, int) or isinstance(factor, float):
            return Money(
                self.amount * factor,
                self.currency)
        else: 
            raise RuntimeError

