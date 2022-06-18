import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue','mub':'okay'}

x = requests.head(url)

#print the response text (the content of the requested file):

print(x.text)