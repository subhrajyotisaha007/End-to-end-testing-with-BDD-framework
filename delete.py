import requests

book_id = 'fgfgfg409'

add_book_response = requests.delete("http://216.10.245.166/Library/DeleteBook.php",json={'ID':book_id},headers={"Content-Type":"application/json"})
print(add_book_response.status_code)
info = add_book_response.json()
print(info)
