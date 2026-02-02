Langkah pertama untuk instalasi django, menggunakan venv

1) mulai dengan untuk membuat core
```python
django-admin startproject mywebsite
```
_Note : boleh nama lain selain mywebsite_

2) untuk menjalankan server
```python
python manage.py runserver
```


_Note_
- untuk membuat app baru
```python
python manage.py starapp namaapp
```
- setelah menambahkan app baru masuk ke dalam setting/instal app dan tambahkan nama
aplikasi yang di tambahkan 
- setelah menambahkan template, masukkan dictionary template ke dalam setting
- masukkan static ke dalam setting dengan format

```python
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
```

- file static untuk menyimpan css, js, img
- file template berisi template index.html

