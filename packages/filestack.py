from .secret.filestack_apikey import API_KEY
from filestack import Client
client = Client(API_KEY)

<<<<<<< HEAD
new_filelink = client.upload(filepath='C:/Users/username/code/python/udemy-pythonprocourse/App-02-Flatmates-Bill/files/August-2022.pdf')
=======
new_filelink = client.upload(filepath='C:/Users/{USERNAME}/code/python/udemy-pythonprocourse/App-02-Flatmates-Bill/files/August-2022.pdf')
>>>>>>> 4d6ca05982cde937099bc6474b5ded44ef05898e
print(new_filelink.url)
