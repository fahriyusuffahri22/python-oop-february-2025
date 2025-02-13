from project.user import User
from project.library import Library


class Registration:
    @staticmethod
    def add_user(user: User, library: Library) -> None | str:
        if user not in library.user_records:
            library.user_records.append(user)
            return

        return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library) -> None | str:
        for i in range(len(library.user_records)):
            if library.user_records[i] == user:
                library.user_records.pop(i)
                return

        return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library) -> str:
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return  (
                        f"Please check again the provided username - it should be different than the username used so "
                        f"far!"
                    )

                if user.username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books.pop(user.username)

                user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return f"There is no user with id = {user_id}!"