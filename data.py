import mysql.connector

from utilities.config import getQuery


def add_book(isbn,aisle,name,author):
    book = {'name': name,
     'isbn': isbn,
     'aisle': aisle,
     'author': author
            }

    return book



# def add_book(query):
#     addBody = {}
#     tp = getQuery(query)
#     addBody['name'] = tp[0]
#     addBody['isbn'] = tp[1]
#     addBody['aisle'] = tp[2]
#     addBody['author'] = tp[3]
#     return addBody