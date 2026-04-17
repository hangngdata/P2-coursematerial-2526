from book import *
import pytest

def test_valid_creation():
    book = Book('Watchmen', '978-1779501127')
    assert book.title == 'Watchmen'
    assert book.isbn == '978-1779501127'


def test_creation_with_invalid_title():
    with pytest.raises(RuntimeError):
        Book('', '978-1779501127')

def test_creation_with_invalid_isbn():
    with pytest.raises(RuntimeError):
        Book('Watchmen', '978-1779501128')