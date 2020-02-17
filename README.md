# spacebase
Django project for spacebase booklist application

## VERSIONS:
  python: 3.8.1
  django: 3.0.3
  sqlite3: 3.24.0
  
## Installation/Run instructions
  Verify proper versions of python, django and sqlite3 are installed
  To run server:
  1. navigate to the parent "readinglist" directory (there are two). There should be a manage.py file on the same level.
  2. type python3 manage.py runserver
  3. server will default to localhost:8000
  
  To access shell to create database data:
  1. python3 manage.py shell
  
## Urls:
  accounts/signup/ (directs to signup page)
  accounts/userpage/ (directs to userpage; must be authenticated)
  accounts/login/ (directs to login page)
  accounts/logout/ (logs current user out, redirects to login page)
  list/ (directs to book list page)
  admin/ (admin view; must be authenticated with admin privileges) 

## Models:

  User model: using django's builtin User model.

  Book(models.Model):
    title = models.CharField(max_length=40, null=False, default="untitled")
    author = models.CharField(max_length=40, default="no author listed")

  Userfavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
  
## Schema:

  user: 
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT 
    "password" varchar(128) NOT NULL 
    "last_login" datetime NULL 
    "is_superuser" bool NOT NULL 
    "username" varchar(150) NOT NULL UNIQUE 
    "first_name" varchar(30) NOT NULL 
    "email" varchar(254) NOT NULL 
    "is_staff" bool NOT NULL 
    "is_active" bool NOT NULL 
    "date_joined" datetime NOT NULL 
    "last_name" varchar(150) NOT NULL)
    
  book: 
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT 
    "author" varchar(40) NOT NULL 
    "title" varchar(40) NOT NULL)
    
  userfavorite:
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT 
    "book_id" integer NOT NULL REFERENCES "booklist_book" ("id") DEFERRABLE INITIALLY DEFERRED 
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED 
    "rating" integer NULL);
    
    



