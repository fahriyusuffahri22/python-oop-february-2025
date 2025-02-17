from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}
        self.rented_books: Dict[str, Dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        author_books = self.books_available[author]

        for i in range(len(author_books)):
            if author_books[i] == book_name:
                if user.username in self.rented_books:
                    self.rented_books[user.username][book_name] = days_to_return
                else:
                    self.rented_books[user.username] = {book_name: days_to_return}

                user.books.append(book_name)
                author_books.pop(i)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for books in self.rented_books.values():
            if book_name in books:
                return f'The book "{book_name}" is already rented and will be available in {books[book_name]} days!'


    def return_book(self, author:str, book_name:str, user: User) -> None | str:
        if book_name in self.rented_books[user.username]:
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
            user.books.remove(book_name)
            return

        return f"{user.username} doesn't have this book in his/her records!"