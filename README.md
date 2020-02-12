# spacebase
First Django project for spacebase booklist application

VERSIONS:
python: 3.8.1
django: 3.0.3

Structure:
I decided on a many to many model; being that there are many favorite books to a user, and a book can have many users. 

Issues:
My only issue is how to allow individual users to edit the books in their books list. If each individual user is able to edit a books properties, this will effect and damage statistaical analysis; like "top rated book" or "most read book". To get around this, I've decided on allowing users to update the rating they gave each individual book, while keeping the single source of truth for the list of books.


