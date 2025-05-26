from models import Author, Book, Genre, Tag

# ========== CREATE ==========
def create_author(db, name):
    db.add(Author(name=name))
    db.commit()

def create_genre(db, name):
    db.add(Genre(name=name))
    db.commit()

def create_tag(db, name):
    db.add(Tag(name=name))
    db.commit()

def create_book(db, title, author_id, genre_id, tag_ids=[]):
    tags = db.query(Tag).filter(Tag.id.in_(tag_ids)).all() if tag_ids else []
    book = Book(title=title, author_id=author_id, genre_id=genre_id, tags=tags)
    db.add(book)
    db.commit()

# ========== READ ==========
def get_all_authors(db):
    return db.query(Author).all()

def get_all_genres(db):
    return db.query(Genre).all()

def get_all_tags(db):
    return db.query(Tag).all()

def get_all_books(db):
    return db.query(Book).all()

# ========== DELETE ==========
def delete_author(db, author_id):
    author = db.query(Author).get(author_id)
    if author:
        db.delete(author)
        db.commit()
        return True
    return False

def delete_genre(db, genre_id):
    genre = db.query(Genre).get(genre_id)
    if genre:
        db.delete(genre)
        db.commit()
        return True
    return False

def delete_tag(db, tag_id):
    tag = db.query(Tag).get(tag_id)
    if tag:
        db.delete(tag)
        db.commit()
        return True
    return False

def delete_book(db, book_id):
    book = db.query(Book).get(book_id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False

# ========== UPDATE ==========

def update_author(db, author_id, new_name):
    author = db.query(Author).get(author_id)
    if author:
        author.name = new_name
        db.commit()
        return True
    return False

def update_genre(db, genre_id, new_name):
    genre = db.query(Genre).get(genre_id)
    if genre:
        genre.name = new_name
        db.commit()
        return True
    return False

def update_tag(db, tag_id, new_name):
    tag = db.query(Tag).get(tag_id)
    if tag:
        tag.name = new_name
        db.commit()
        return True
    return False

def update_book(db, book_id, new_title=None, new_author_id=None, new_genre_id=None, new_tag_ids=None):
    book = db.query(Book).get(book_id)
    if not book:
        return False

    if new_title:
        book.title = new_title
    if new_author_id:
        book.author_id = new_author_id
    if new_genre_id:
        book.genre_id = new_genre_id
    if new_tag_ids is not None:  
        tags = db.query(Tag).filter(Tag.id.in_(new_tag_ids)).all()
        book.tags = tags

    db.commit()
    return True
