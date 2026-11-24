import json

class LibraryDatabase:
    def __init__(self):
        self.books = {"Война и мир": 1, "Преступление и наказание": 2}

    def process_request(self, json_string):
        data = json.loads(json_string)
        book = data.get("book")
        user = data.get("user")
        
        if book in self.books and self.books[book] > 0:
            self.books[book] -= 1
            return f"Книга '{book}' выдана пользователю {user}."
        else:
            return "Ошибка: Книги нет в наличии."
