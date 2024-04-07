import requests
from data import *
from utilities.config import *
from utilities.resorces import *

headers={"Content-Type":"application/json"}
query = 'select * from books'
#add-
url1 = getConfig()['API']['endpoint']+ApiResources.addbook
add_book_response = requests.post(url1,json=add_book(query),headers=headers)
info1 = add_book_response.json()
print(info1)
book_id = info1['ID']
print(book_id)


#delete-
url2 = getConfig()['API']['endpoint']+ApiResources.deletebook
add_book_response = requests.delete(url2,json={'ID':book_id},headers=headers)
print(add_book_response.status_code)
info2 = add_book_response.json()
print(info2)


#authentication
se = requests.session()
se.auth = ('subhrajyotisaha007', getPassword())
url3 = 'https://api.github.com/user/repos'
github_data = se.get(url3)

print(github_data.status_code)
print(github_data.json())