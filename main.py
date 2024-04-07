import requests

parameter = {
    'AuthorName':'Rahul Shetty'
}
response = requests.get("http://216.10.245.166/Library/GetBook.php",params=parameter)

data = response.json()
print(data)
print(response.status_code)
#print(response.headers)

for book in data:
    if book['isbn'] == 'A1b':
        final_book = book
        print(final_book)

expected_book = {'book_name': 'Postman Course', 'isbn': 'A1b', 'aisle': '1'}
assert expected_book == final_book