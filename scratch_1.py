from secret.filestack_apikey import API_KEY
from filestack import Client
client = Client(API_KEY')

new_filelink = client.upload(filepath='C:/Users/username/code/python/udemy-pythonprocourse/App-02-Flatmates-Bill/files/August-2022.pdf')
print(new_filelink.url)
