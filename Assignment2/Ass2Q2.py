#Create a program to implement a simple text-based menu system for a library
#  that allows users to add, remove, search, and list books. 
# Use loops and conditional statements effectively.


def main():
    books = []
    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List Books")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book(books)
        elif choice == 2:
            remove_book(books)
        elif choice == 3:
            search_book(books)
        elif choice == 4:
            list_books(books)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

def add_book(books):
    book = input("Enter book name: ")
    books.append(book)
    print("Book added successfully")

def remove_book(books):
    book = input("Enter book name: ")
    if book in books:
        books.remove(book)
        print("Book removed successfully")
    else:
        print("Book not found")

def search_book(books):
    book = input("Enter book name: ")
    if book in books:
        print("Book found")
    else:
        print("Book not found")

def list_books(books):
    for i in books:
        print(i)

main()