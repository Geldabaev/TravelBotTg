import requests
from requests import request


res = requests.get(url='https://google.com')
print(res)

with open('/home/runas/PycharmProjects/pythonProject2/text.txt', "a") as file:
    file.write(f"{res}\n")