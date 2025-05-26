from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

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

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"{self.id}: {self.name}"

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="genre")

    def __repr__(self):
        return f"{self.id}: {self.name}"

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", secondary=book_tag_table, back_populates="tags")

    def __repr__(self):
        return f"{self.id}: {self.name}"

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    tags = relationship("Tag", secondary=book_tag_table, back_populates="books")

    def __repr__(self):
        tag_names = ', '.join(tag.name for tag in self.tags) or "No Tags"
        return f"{self.id}: '{self.title}' by {self.author.name} | Genre: {self.genre.name} | Tags: {tag_names}"

