class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email updated to {email}".format(email=address))

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(
            name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        ratings = [rating for rating in self.books.values()
                   if rating is not None]
        return (sum(ratings) / len(ratings))


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title} (ISBN: {isbn})".format(title=self.title,
                                            isbn=self.isbn)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("ISBN updated to {}".format(isbn))

    def add_rating(self, rating):
        if rating is not None and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        return (sum(self.ratings) / len(self.ratings))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title,
                                            author=self.author)

    def get_author(self):
        return self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(
            title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email)
        if user is None:
            print("No user with email {email}!".format(email=email))
        else:
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books is not None:
            for user_book in user_books:
                self.add_book_to_user(user_book, user.email)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for key in self.users.keys():
            print(key)

    def most_read_book(self):
        top_read_book = float("-inf")
        number_of_readers = float("-inf")
        for key, value in self.books.items():
            if value > number_of_readers:
                number_of_readers = value
                top_read_book = key
        return top_read_book

    def highest_rated_book(self):
        top_rated_book = float("-inf")
        top_rating = float("-inf")
        for book in self.books.keys():
            book_rating = book.get_average_rating()
            if book_rating > top_rating:
                top_rating = book_rating
                top_rated_book = book
        return top_rated_book

    def most_positive_user(self):
        top_user = float("-inf")
        top_users_rating = float("-inf")
        for user in self.users.values():
            user_rating = user.get_average_rating()
            if user_rating > top_users_rating:
                top_users_rating = user_rating
                top_user = user
        return top_user

    def get_n_most_read_books(self, n):
        sorted_books = sorted(self.books, key=self.books.__getitem__,
                              reverse=True)
        i = 0
        while i < n and i <= len(self.books) - 1:
            print(sorted_books[i])
            i += 1

    def get_n_most_prolific_readers(self, n):
        sorted_users = sorted(self.users.values(), key=get_number_of_books_read,
                              reverse=True)
        i = 0
        print(f'length of users is {len(self.users)}')
        while i < n and i <= len(self.users) - 1:  # up to n users or all users if n is greater
            print(sorted_users[i])
            i += 1


def get_number_of_books_read(user):
    return len(user.books)
