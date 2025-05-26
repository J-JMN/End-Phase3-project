import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
from cli_models import author_commands, genre_commands, tag_commands, book_commands

engine = create_engine("sqlite:///library.db")
Session = sessionmaker(bind=engine)
db = Session()

Base.metadata.create_all(engine)

@click.group()
def cli():
    pass

@cli.command()
def run():
    while True:
        print("\n📚 LIBRARY CLI MANAGER")
        print("1. 🧑 Authors\n2. 🎭 Genres\n3. 🏷️ Tags\n4. 📖 Books\n5. ❌ Exit")
        choice = input("Choose index: ")

        if choice == "1":
            author_commands(db)
        elif choice == "2":
            genre_commands(db)
        elif choice == "3":
            tag_commands(db)
        elif choice == "4":
            book_commands(db)
        elif choice == "5":
            print("👋 Come Again!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    cli()
