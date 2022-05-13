# https://developers.google.com/books/docs/v1/using#PerformingSearch
import requests

title = 'Why Nations Fail'
author = 'cu'

def get_book_details_from_google(title, author):
    bookResponse = requests.get('https://www.googleapis.com/books/v1/volumes?q=intitle:' + title + '+inauthor:' + author)           
    jsondict = bookResponse.json()
    firstbookresultdetails = jsondict['items'][0]['volumeInfo']
    print(firstbookresultdetails['authors'])
    print(firstbookresultdetails['publisher'])
    print(firstbookresultdetails['categories'])
    
get_book_details_from_google(title, author)