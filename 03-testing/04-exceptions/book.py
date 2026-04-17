class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if not title:
            raise RuntimeError
        self.__title = title

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if not self.is_valid_isbn(isbn):
            raise RuntimeError
        self.__isbn = isbn

    @staticmethod
    def is_valid_isbn(isbn):
        if not isinstance(isbn, str):
            return False
        
        digits = [int(digit) for digit in isbn if digit.isdigit()]
        if len(digits) != 13:
            return False
        
        total = 0
        for i in range(13):
            if i % 2 == 0:
                total += digits[i] * 1
            else:
                total += digits[i] * 3
        
        return total % 10 == 0