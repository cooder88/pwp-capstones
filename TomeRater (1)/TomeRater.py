class User(object):
    def __init__(self, name, email):
        self.name= name
        self.email=email
        self.books={}

    def get_email(self):
        return self.email

    def change_email(self, address):
        address = self.email
        return "The email have been changed"

    def __repr__(self):
        return "User " + self.name + ",email: " + self.email + ",books read: " + str(self.books) 

    def __eq__(self, other_user):
        return other_user.name == self.name and self.get_email == other_user.get_email

    def read_book(self, book, rating=None):
        self.books[book]= rating

    def get_average_rating(self,avarage):
        
        avarage = 0
        for total in self.books[]:
            total += avarage
        return avarage
    




    

class book:
    def __init__(self,title,isbn):
        self.title= title
        self.isbn=isbn
        self.ratings= []
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, new_isbn):
        new_isbn= self.isbn
        return "This book’s ISBN has been updat"
    def add_rating(self, rating):
        ratingsNumber = 0
        for rat in rating
        ratingsNumber += self.ratings[]
        if rating >=0 and rating <= 4:
            return ratingsNumber
        return "Invalid Rating"
    def __eq__(self, other_book):
        return other_book.title == self.title and other_book.new_isbn == self.new_isbn

    def get_average_rating(self, avarage_rating):
        avarage_rating = 0
        for total in  self.ratings:
            total += avarage_rating
        return avarage_rating
    def __hash__(self):
        return hash((self.title, self.isbn))
    
        
class Fiction(book):
    def __init__(self,title,author,isbn):
        self.author=authot
    def get_author(self):
        return self.author
    def __repr__(self):
        return {tittle}.format(self.title) + "by" + {author}.format(author=self.author)

class Non_Fiction(book):
    def __init__(self,title,subject,level,isbn):
        self.subject= subject
        self.level = level

    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(subject = self.subject, title=self.title, level=self.level)


class TomeRater:

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(title,isbn):
        return book(title, isbn)

    def create_novel(title , author , isbn):
        return Fiction(title , author , isbn)



    def create_non_fiction(title , subject , level ,isbn):
        return Non_Fiction(title , subject , level ,isbn)


    def add_book_to_user(self,book , email , rating= None):
        self.users[email]= rating
        if self.email != self.users[email]:
            print("No user with email {email}!”)
        else:
                  read_book(book,rating)and add_rating(book,rating)
                  
        if book in self.books:
                  self.books[book]=1
                  
        else:
                  self.books[book] +=1

    def add_user(self,  name , email, user_books=None):
        User(name, email)
        if user_books != None:
                  for book in self.books:
                  book += add_book_to_user

    def print_catalog(self, book):
        for book in self.books:
                  print(book)
    def print_users(self, user):
        for user in self.users:
                  print(user)
    def most_read_book(self, books):
        for books in self.books:
                  return self.books

    def highest_rated_book(self, ratings):
        for ratings in self.books:
                  return book.get_average_rating(book)

    def most_positive_user(self,user):
        for user in self.users:
                  return user.get_average_rating(user)

    
        

                



                  
                     
                
                
                
                
        


    
    
        


        
            
            
