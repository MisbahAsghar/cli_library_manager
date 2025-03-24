import os

# Initialize library as an empty list
library = []

# Adding function
def add_book(title, author, year, genre, read_status):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(book)

# Removing function
def remove_book(title):
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]

# Searching function
def search_books(search_by, search_value):
    result = []
    for book in library:
        if search_by == "Title" and search_value.lower() in book["title"].lower():
            result.append(book)
        elif search_by == "Author" and search_value.lower() in book["author"].lower():
            result.append(book)
    return result

# Displaying function
def display_books():
    if library:
        for idx, book in enumerate(library, start=1):
            status = "Read" if book["read_status"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("📚 Your library is empty. 📚")

def display_statistics():
    total_books = len(library)
    read_books = len([book for book in library if book["read_status"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"📘 Total books: {total_books}")
    print(f"📖 Percentage read: {percentage_read:.2f}%")

# CLI Menu
def menu():
    while True:
        print("\n📚 Personal Library Manager 📚")
        print("1. ➕ Add a book")
        print("2. ❌ Remove a book")
        print("3. 🔍 Search for a book")
        print("4. 📖 Display all books")
        print("5. 📊 Display statistics")
        print("6. 🚪 Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            year = int(input("Enter the publication year: "))
            genre = input("Enter the genre: ")
            read_status = input("Have you read this book? (Yes/No): ").strip().lower()

            if read_status == "yes":
                read_status = True
            else:
                read_status = False

            add_book(title, author, year, genre, read_status)
            print(f"'{title}' added successfully! 🎉")

        elif choice == "2":
            title_to_remove = input("Enter the title of the book to remove: ")
            remove_book(title_to_remove)
            print(f"'{title_to_remove}' removed successfully! ✂️")

        elif choice == "3":
            search_by = input("Search by (Title/Author): ").strip()
            search_value = input(f"Enter the {search_by.lower()} to search for: ")
            results = search_books(search_by, search_value)
            if results:
                for idx, book in enumerate(results, start=1):
                    status = "Read" if book["read_status"] else "Unread"
                    print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
            else:
                print(f"No books found matching '{search_value}' 😞.")

        elif choice == "4":
            print("\nYour Library 📚")
            display_books()

        elif choice == "5":
            print("\nLibrary Statistics 📈")
            display_statistics()

        elif choice == "6":
            print("Thank you for using the Personal Library Manager. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
