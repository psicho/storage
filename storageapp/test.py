import requests
import json

# Проверка хеширования
# hashfile.md5('temp.txt')
# hashfile.sha1('temp.txt')

# Загрузка файла
server = 'http://127.0.0.1:8000/file/upload/'
path = r'F:\Dr Web\storage\storageapp\temp.txt'
response = requests.get(server + path)
# print(response.text)
data = json.loads(response.text)
print(type(data))
print('Url', data['url'])
print('Hash', data['hashs'])
print('Mkdir', data['mkdir'])
print('status', data['status'])
print()

# Скачивание файла
# if data['status'] == True:
# server = 'http://127.0.0.1:8000/file/download/'
# hashs = '5f6ef9cc177fa5ed76c66dfdf693df4769fb707'
# response = requests.get(server + hashs)
# data = json.loads(response.text)
# print(type(data))
# print('file_url', data['file_url'])
# print('Hash', data['hashs'])
# print('status', data['status'])


# Удаление файла
# # if data['status'] == True:
# server = 'http://127.0.0.1:8000/file/delete/'
# # hashs = '79cdd4d0206074d80f25ecd173d7cb80635a1b78'
# hashs = data['hashs']
# response = requests.get(server + hashs)
# data = json.loads(response.text)
# print(type(data))
# print('file_url', data['file_url'])
# print('Hash', data['hashs'])
# print('status', data['status'])