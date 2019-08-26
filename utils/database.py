#concerned eith storing into a a json file
import json

def create_db():
    with open('books.json', 'w'):
        pass

def add_book(name, author):
    books = list_book()
    books.append({'name': name, 'author': author, 'read': False})
    with open('books.json ', 'w') as file:
        json.dump(books, file)


def list_book():
    with open('books.json', 'r') as file:
        return json.load(file)
def mark_book(name):
    # with open('books.txt', 'r') as file
    #     lines = [line.strip().split(',') for line in file.readlines()]
    #     books = [
    #         {'name': line[0], 'author': line[1], 'read': line[2]}
    #         for line in lines
    #     ]
    books = list_book()
    for book in books:
        if book['name'] == name:
            book['read'] = True

    with open('books.json', 'w') as file:
        json.dump(books, file)



# def del_book(name):
#     for book in books:
#        if b ook['name'] == name:
#            books.remove(book)

def del_book(name):
    books = list_book()
    new_book = []
    for book in books:
        if book['name'] != name:
            new_book.append(book)
    with open('book.txt', 'w') as file:
        json.dump(new_book, file )







