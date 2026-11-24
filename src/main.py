from module_a import create_book_request
from module_b import LibraryDatabase

db = LibraryDatabase()
request = create_book_request("Война и мир", "Иван")
print("Отправлен JSON:", request)
print("Ответ системы:", db.process_request(request))
