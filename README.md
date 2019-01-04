# Хранилище файлов с доступом по http

## Доступны следующие операции:

### Upload ###

Загрузка файла осуществляется по api запросу вида http://127.0.0.1:8000/file/upload/путь_к_файлу

В ответ сервер возвращает словарь в формате JSON вида {"status": true, "file_path": "F:/Dr Web/storage/storageapp/temp.txt", "hash": "ab4f83f9b476169972758aef0cb4115e70fd6ecd", "file_upload_path": "F:\\Dr Web\\storage\\store\\ab\\ab4f83f9b476169972758aef0cb4115e70fd6ecd.txt"}

где "status" - это статус загрузки файла на сервер(True - успешно, False - запрос не обработан); "file_path" - переданный адрес файла для загрузки; "hash" - хеш файла после обработки хеш-функцией; "file_upload_path" - адрес директории на сервере в которую загружен файл

### Download ###

Скачивание файла осуществляется по api запросу вида http://127.0.0.1:8000/file/download/хеш_файла

В ответ сервер возвращает словарь в формате JSON вида {"status": true, "file_download_path": "F:\\Dr Web\\storage\\store\\ab\\ab4f83f9b476169972758aef0cb4115e70fd6ecd.txt", "hash": "ab4f83f9b476169972758aef0cb4115e70fd6ecd"}

где "status" - это статус получения файла с сервера(True - успешно, False - запрос не обработан); "file_download_path" - адрес расположения файла на сервере для скачивания; "hash" - переданный хеш файла.

### Delete ###

Удаление файла осуществляется по api запросу вида http://127.0.0.1:8000/file/delete/хеш_файла

В ответ сервер возвращает словарь в формате JSON вида {"status": true, "file_delete_url": "F:\\Dr Web\\storage\\store\\ab\\ab4f83f9b476169972758aef0cb4115e70fd6ecd.txt", "hash": "ab4f83f9b476169972758aef0cb4115e70fd6ecd"}

где "status" - это статус получения файла с сервера(True - успешно, False - запрос не обработан); "file_delete_url" - адрес расположения удаленного файла на сервере; "hash" - переданный хеш файла.