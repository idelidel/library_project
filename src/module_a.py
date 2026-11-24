import json

def create_book_request(book_title, user_name):
    request_data = {"action": "borrow", "book": book_title, "user": user_name}
    return json.dumps(request_data, ensure_ascii=False)
