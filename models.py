from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

book_tag_table = Table(
    "book_tag",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        date_str = self.created_at.strftime("%Y-%m-%d %H:%M") if self.created_at else "Unknown"
        return f"{self.id}: {self.name} — added on {date_str}"

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    books = relationship("Book", back_populates="genre")

    def __repr__(self):
        date_str = self.created_at.strftime("%Y-%m-%d %H:%M") if self.created_at else "Unknown"
        return f"{self.id}: {self.name} — added on {date_str}"

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    books = relationship("Book", secondary=book_tag_table, back_populates="tags")

    def __repr__(self):
        date_str = self.created_at.strftime("%Y-%m-%d %H:%M") if self.created_at else "Unknown"
        return f"{self.id}: {self.name} — added on {date_str}"

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    tags = relationship("Tag", secondary=book_tag_table, back_populates="books")

    def __repr__(self):
        title = self.title
        author_name = self.author.name if self.author else "Unknown Author"
        genre_name = self.genre.name if self.genre else "Unknown Genre"
        tag_names = ', '.join(tag.name for tag in self.tags) if self.tags else "No Tags"
        created = self.created_at.strftime("%Y-%m-%d %H:%M") if self.created_at else "Unknown"
        return f"{self.id}: '{title}' by {author_name} | Genre: {genre_name} | Tags: {tag_names} | Added: {created}"
