from crud import *

def author_commands(db):
    while True:
        print("\n🧑 Author Menu:\n1. ➕ Add\n2. 👀 View\n3. 📝 Update\n4. ❌ Delete\n5. 🔙 Back")
        choice = input("Choose index: ")

        if choice == "1":
            name = input("Author name: ").strip()
            if name:
                create_author(db, name)
                print(f"✅ Author '{name}' added.")
            else:
                print("❗ Name cannot be empty.")

        elif choice == "2":
            print("======================")
            print("Available Authors")
            print("======================")
            for author in get_all_authors(db):
                print(author)

        elif choice == "3":
            authors = get_all_authors(db)
            for author in authors:
                print(author)
            try:
                author_id = int(input("Enter Author ID to update: "))
                new_name = input("New name: ").strip()
                if new_name:
                    if update_author(db, author_id, new_name):
                        print("✅ Author updated!")
                    else:
                        print("❌ Author not found.")
                else:
                    print("❗ Name cannot be empty.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            authors = get_all_authors(db)
            for author in authors:
                print(author)
            try:
                author_id = int(input("Enter Author ID to delete: "))
                if delete_author(db, author_id):
                    print("✅ Author deleted!")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            break
        else:
            print("❗ Invalid choice.")


def genre_commands(db):
    while True:
        print("\n🎭 Genre Menu:\n1. ➕ Add\n2. 👀 View\n3. 📝 Update\n4. ❌ Delete\n5. 🔙 Back")
        choice = input("Choose index: ")

        if choice == "1":
            name = input("Genre name: ").strip()
            if name:
                create_genre(db, name)
                print(f"✅ Genre '{name}' added.")
            else:
                print("❗ Name cannot be empty.")

        elif choice == "2":
            print("======================")
            print("Available Genres")
            print("======================")
            for genre in get_all_genres(db):
                print(genre)

        elif choice == "3":
            genres = get_all_genres(db)
            for genre in genres:
                print(genre)
            try:
                genre_id = int(input("Enter Genre ID to update: "))
                new_name = input("New name: ").strip()
                if new_name:
                    if update_genre(db, genre_id, new_name):
                        print("✅ Genre updated!")
                    else:
                        print("❌ Genre not found.")
                else:
                    print("❗ Name cannot be empty.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            genres = get_all_genres(db)
            for genre in genres:
                print(genre)
            try:
                genre_id = int(input("Enter Genre ID to delete: "))
                if delete_genre(db, genre_id):
                    print("✅ Genre deleted!")
                else:
                    print("❌ Genre not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            break
        else:
            print("❗ Invalid choice.")


def tag_commands(db):
    while True:
        print("\n🏷️ Tag Menu:\n1. ➕ Add\n2. 👀 View\n3. 📝 Update\n4. ❌ Delete\n5. 🔙 Back")
        choice = input("Choose index: ")

        if choice == "1":
            name = input("Tag name: ").strip()
            if name:
                create_tag(db, name)
                print(f"✅ Tag '{name}' added.")
            else:
                print("❗ Name cannot be empty.")

        elif choice == "2":
            print("======================")
            print("Available Tags")
            print("======================")
            for tag in get_all_tags(db):
                print(tag)

        elif choice == "3":
            tags = get_all_tags(db)
            for tag in tags:
                print(tag)
            try:
                tag_id = int(input("Enter Tag ID to update: "))
                new_name = input("New name: ").strip()
                if new_name:
                    if update_tag(db, tag_id, new_name):
                        print("✅ Tag updated!")
                    else:
                        print("❌ Tag not found.")
                else:
                    print("❗ Name cannot be empty.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            tags = get_all_tags(db)
            for tag in tags:
                print(tag)
            try:
                tag_id = int(input("Enter Tag ID to delete: "))
                if delete_tag(db, tag_id):
                    print("✅ Tag deleted!")
                else:
                    print("❌ Tag not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            break
        else:
            print("❗ Invalid choice.")


def book_commands(db):
    while True:
        print("\n📚 Book Menu\n1. ➕ Add\n2. 👀 View\n3. 📝 Update\n4. ❌ Delete\n5. 🔙 Back")
        choice = input("Choose index: ")

        if choice == "1":
            title = input("Book title: ").strip()
            authors = get_all_authors(db)
            genres = get_all_genres(db)
            tags = get_all_tags(db)

            print("\nAvailable Authors:")
            for author in authors:
                print(author)
            try:
                author_id = int(input("Enter author ID: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            print("\nAvailable Genres:")
            for genre in genres:
                print(genre)
            try:
                genre_id = int(input("Enter genre ID: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            print("\nAvailable Tags (Optional - comma-separated IDs):")
            for tag in tags:
                print(tag)
            tag_input = input("Enter tag IDs (optional): ").strip()
            tag_ids = [int(tid.strip()) for tid in tag_input.split(",") if tid.strip().isdigit()] if tag_input else []

            try:
                create_book(db, title, author_id, genre_id, tag_ids)
                print(f"✅ Book '{title}' added!")
            except Exception as e:
                print(f"❌ Error adding book: {e}")

        elif choice == "2":
            books = get_all_books(db)
            print("\n📖 Books:")
            for book in books:
                print(book)

        elif choice == "3":
            books = get_all_books(db)
            for book in books:
                print(book)

            try:
                book_id = int(input("Enter Book ID to update: "))
                new_title = input("New title (or leave blank): ").strip()

                authors = get_all_authors(db)
                print("\nAvailable Authors:")
                for author in authors:
                    print(author)
                author_input = input("New author ID (or leave blank): ").strip()
                new_author_id = int(author_input) if author_input else None

                genres = get_all_genres(db)
                print("\nAvailable Genres:")
                for genre in genres:
                    print(genre)
                genre_input = input("New genre ID (or leave blank): ").strip()
                new_genre_id = int(genre_input) if genre_input else None

                tags = get_all_tags(db)
                print("\nAvailable Tags:")
                for tag in tags:
                    print(tag)
                tag_input = input("New tag IDs (comma-separated or leave blank): ").strip()
                new_tag_ids = [int(tid.strip()) for tid in tag_input.split(",") if tid.strip().isdigit()] if tag_input else None

                if update_book(db, book_id, new_title, new_author_id, new_genre_id, new_tag_ids):
                    print("✅ Book updated!")
                else:
                    print("❌ Book not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            books = get_all_books(db)
            print("\nAvailable Books:")
            for book in books:
                print(book)
            try:
                book_id = int(input("Enter book ID to delete: "))
                if delete_book(db, book_id):
                    print("✅ Book deleted!")
                else:
                    print("❌ Book ID not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            break
        else:
            print("❗ Invalid choice. Try again.")

