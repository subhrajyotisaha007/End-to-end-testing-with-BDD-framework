import requests
from data import *

add_book_response = requests.post("http://216.10.245.166/Library/Addbook.php",json=add_book("fgfgfg"),headers={"Content-Type":"application/json"})

info = add_book_response.json()
print(info)

book_id = info['ID']
print(book_id)