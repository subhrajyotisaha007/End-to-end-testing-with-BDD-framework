import requests
from behave import *

from data import add_book
from utilities.config import getConfig, getPassword
from utilities.resorces import ApiResources


@given('the book details which needs to be added to Library')
def step_impl(context):
    context.url1 = getConfig()['API']['endpoint'] + ApiResources.addbook
    context.headers = {"Content-Type": "application/json"}
    #context.query = 'SELECT * FROM Books LIMIT 1 OFFSET 2'
    context.payload = add_book('jshshsh',709,'Sahas Story','Jyoti')


@when('we execute the Addbook PostAPI method')
def step_impl(context):
    context.add_book_response = requests.post(context.url1, json=context.payload, headers=context.headers)


@then('Book is successfully added')
def step_impl(context):
    info1 = context.add_book_response.json()
    print(info1)
    context.book_id = info1['ID']
    print(context.book_id)
    assert info1['Msg'] == 'successfully added'


@given('the book details with {isbn}, {aisle},{name} and {author}')
def step_impl(context,isbn,aisle,name,author):
    context.url1 = getConfig()['API']['endpoint'] + ApiResources.addbook
    context.headers = {"Content-Type": "application/json"}
    context.payload = add_book(isbn,aisle,name,author)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = ('subhrajyotisaha007', getPassword())
    context.url3 = getConfig()['API']['github']

@when('I hit getRepo API of github')
def step_impl(context):
    context.github_data = context.se.get(context.url3)


@then('status code of response should be {statuscode:d}')
def step_impl(context,statuscode):
    print(context.github_data.status_code)
    assert context.github_data.status_code == statuscode
    # print(context.github_data.json())