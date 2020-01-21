"""These are ORM models provided to the blog."""

from sqlalchemy import (Boolean, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

tag_posts_relation = Table("tags_posts_relation", Base.metadata,
                           Column("post_id", Integer, ForeignKey('posts.post_id')),
                           Column("tag_id", Integer, ForeignKey("tags.tag_id"))
                           )


class User(Base):
    """This class represents User in blog.
    id: is a unique identification of a User in DB, integer, auto increment.
    user_name: string max 30 characters, can be repeated in DB
    """
    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True)
    user_name = Column(String(30), nullable=False)

    posts = relationship("Posts", back_populates="user")

    def __repr__(self):
        return f"User id#{self.id}, User name {self.user_name}"


class PostsCategory(Base):
    """ This class represents Posts categories available in blog.
    category_id: is a unique identification of a Post's Category in DB, integer, auto increment.
    category_name: string, can be repeated in DB
    """
    __tablename__ = "post_category"

    category_id = Column(Integer, nullable=False, primary_key=True)
    category_name = Column(String, nullable=False)

    posts = relationship("Posts", back_populates="post_category")

    def __repr__(self):
        return f"Post's Category Id #{self.id}, Category name {self.user_name}"


class Posts(Base):
    """ This class represents Posts in blog
    post_id: is a unique identification of a Post in DB, integer, auto increment.
    post_date_creation: datetime
    post_reading_time: string
    author_id: integer, relation type with User class one to many
    category_id: integer, relation type with PostsCategory class one to many
    post_title: string, 120 characters max
    post_text: text
    is_post_published: Boolean, False as default value
    posts_claps: integer, amount of "likes" of this post's.

    Posts have a many2many relation with Tags class.
    """
    __tablename__ = "posts"

    post_id = Column(Integer, nullable=False, primary_key=True)
    post_date_creation = Column(Date, nullable=False)
    post_reading_time = Column(String)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)
    category_id = Column(Integer, ForeignKey(PostsCategory.category_id))
    post_title = Column(String(120), nullable=False)
    post_text = Column(String, nullable=False)
    is_post_published = Column(Boolean, nullable=False, default=False)
    posts_claps = Column(Integer, default=0)

    user = relationship(User, back_populates="posts", lazy="joined")
    post_category = relationship(PostsCategory, back_populates="posts")
    tags = relationship("Tags", secondary=tag_posts_relation, back_populates="posts")

    def __repr__(self):
        return f"Post{self.post_id} {self.post_title}"


class Tags(Base):
    """ This class represents Tags in blog.
    tag_id: is a unique identification of a Tag in DB, integer, auto increment.
    tag_name: string, 120 characters max
    """
    __tablename__ = "tags"

    tag_id = Column(Integer, nullable=False, primary_key=True)
    tag_name = Column(String(120), nullable=False)

    posts = relationship(Posts, secondary=tag_posts_relation, back_populates="tags")

    def __repr__(self):
        return f"Tag{self.tag_id} {self.tag_name}"
