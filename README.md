[![Build Status](https://travis-ci.com/larryTheGeek/EbookShare.svg?branch=develop)](https://travis-ci.com/larryTheGeek/EbookShare)

# EbookShare
EbookShare  is a platform that connects readers around the world by enabling  them to share Ebooks from their google drives.

### Framework used
The application is built using python: Django Rest framework.
>[Django Rest](https://www.django-rest-framework.org/topics/documenting-your-api/)
### End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/auth/signup` |  Register a user. |
|POST| `api/v1/auth/login` | Login user.|
|POST| `api/v1/books` | Share a book. |
|GET| `api/v1/books` | Get all all books. |
|GET| `api/v1/books/user` | Get all the books created by the current user who is logged in. |
|GET| `api/v1/books/<book_id>` | Get a single book. |
|PUT| `api/v1/books/<book_id>/title` | Update a book title. |
|DELETE| `api/v1/books/<book_id>` | Delete a book incident. | 

## Installation 🕵
- To run on local machine git clone this project :
```
$ git clone https://github.com/larryTheGeek/EbookShare.git
```
Copy and paste the above command in your terminal, the project will be downloaded to your local machine.

To Install python checkout:
```
https://www.python.org/
```

- create a virtualenv and make it use python 3 using the following command.
```

$ pipenv shell
```
- Install Requirements
```
$ pipenv sync
```
### Testing
- Run the following command
```
$ python manage.py test
```

The app can also be tested via Postman
- Run App 
```
$ python manage.py runserver
```
The app should be accessiable via : http://127.0.0.1:8000/

open postman and navigate to the API endpoints described above
