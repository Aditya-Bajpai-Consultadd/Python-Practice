# Build a library catalog that supports searching by title, author, or
# category. Use dictionaries and lists for efficient data organization.

def main():
    books = []
    while True:
        print("1. Add Book")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Search by Category")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book(books)
        elif choice == 2:
            search_by_title(books)
        elif choice == 3:
            search_by_author(books)
        elif choice == 4:
            search_by_category(books)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

def add_book(books):
    book = {}
    book["title"] = input("Enter title: ")
    book["author"] = input("Enter author: ")
    book["category"] = input("Enter category: ")
    books.append(book)
    print("Book added successfully")

def search_by_title(books):
    title = input("Enter title: ")
    found = False
    for book in books:
        if book["title"] == title:
            print("Author:", book["author"])
            print("Category:", book["category"])
            found = True
    if not found:
        print("Book not found")

def search_by_author(books):
    author = input("Enter author: ")
    found = False
    for book in books:
        if book["author"] == author:
            print("Title:", book["title"])
            print("Category:", book["category"])
            found = True
    if not found:
        print("Book not found")

def search_by_category(books):
    category = input("Enter category: ")
    found = False
    for book in books:
        if book["category"] == category:
            print("Title:", book["title"])
            print("Author:", book["author"])
            found = True
    if not found:
        print("Book not found")

main()