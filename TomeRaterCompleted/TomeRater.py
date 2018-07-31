
# Programmin with Python Intensive Course. Capstone project by Maria Konstantinova.
# TomeRater allows users to read and rate books.


# *** Create a User ***


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{} email has been updated to {}.".format(self.name, self.email))

    def __repr__(self):
        return "User: {}, /n Email: {},/n Books Read: \
         {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average_rating = 0
        total_rating = 0
        for rating in self.books.values():
            if rating is not None:
                total_rating += rating
        average_rating = (total_rating / len(self.books))
        return average_rating


# *** Create a Book ***


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        if new_isbn in self.books:
            new_isbn.append("x")
        return "The ISBN for {} has been updated to {}." \
            .format(self.title, self.isbn)

    def add_rating(self, rating):
        if rating is not None and 0 <= rating <= 4:
            self.ratings.append(rating)
        return "Invalid Rating!"

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        return False

    def get_average_rating(self):
        average_rating = 0
        total_rating = 0
        for rating in self.ratings:
            if rating is not None:
                total_rating += rating
        average_rating = (total_rating / len(self.ratings))
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

# *** Add a Fiction Subclass to Book ***


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}.".format(self.title, self.author)

# *** Add a Non-Fiction Subclass to Book ***


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {} \
        .".format(self.title, self.level, self.subject)

# *** TomeRater ***


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
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with email {}!".format(email)

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

#
# *** Analysys Methods ***
#

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read = None
        times_read = 0
        for key, value in self.books.items():
            if value > times_read:
                times_read = value
                most_read = key
        return most_read

    def highest_rated_book(self):
        highest_rating = 0
        highest_rated = None
        for book in self.books.keys():
            if highest_rating < book.get_average_rating():
                highest_rating = book.get_average_rating()
                highest_rated = book
        return highest_rated

    def most_positive_user(self):
        highest_rating = 0
        positive_user = None
        for user in self.users.values():
            if highest_rating < user.get_average_rating():
                highest_rating = user.get_average_rating()
                positive_user = user
        return positive_user

    def email_exists(self, name, email):
        if email in self.users:
            print("Opps! Looks like this email is already used.\
            How about a new one?")
        else:
            self.add_user(name, email)
