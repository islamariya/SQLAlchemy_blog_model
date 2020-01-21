import DatabaseModels
from db_operations import create_db_connection, db_commit
import data
from logs import logging


def add_new_user(session, user_list):
    """This function adds a new user to current session.
    :param current session object
    :param user_list: list of user names needed to be added, uploaded from data.py
    :return: session object
    """
    for index, data in enumerate(user_list):
        if isinstance(data, str) and data:
            new_user = DatabaseModels.User(user_name=data)
            session.add(new_user)
        else:
            logging.exception(f"Пользователь {index} {data} is not added")
    db_commit(session)
    return session


def add_new_tags(session, tag_list):
    """This function adds a new tag to current session.
    :param session: current session object
    :param tag_list: list of tags needed to be added, uploaded from data.py
    :return: session object
    """
    for index, data in enumerate(tag_list):
        if isinstance(data, str) and data:
            new_tag = DatabaseModels.Tags(tag_name=data)
            session.add(new_tag)
        else:
            logging.exception(f"Тег {index} {data} is not added")
    db_commit(session)
    return session


def add_new_post_category(session, post_category_list):
    """This function adds a new post category to current session.
    :param session: current session object
    :param post_category_list: list of categories needed to be added, uploaded from data.py
    :return: session object
    """
    for index, data in enumerate(post_category_list):
        if isinstance(data, str) and data:
            new_category = DatabaseModels.PostsCategory(category_name=data)
            session.add(new_category)
        else:
            logging.exception(f"Категория {index} {data} is not added")
    db_commit(session)
    return session


def add_post(session, posts):
    """This function adds a new post to current session.
    :param session: current session object
    :param posts list of posts needed to be added, uploaded from data.py. Each post is a dict.
    :return: session object
    """
    for post in posts:
        a = DatabaseModels.Posts(**post)
        session.add(a)
        session.flush()
    db_commit(session)
    return session


def tags_set(session, data):
    """This function adds to session tags to the single selected post.
    :param session: current session object
    :param data: dict {"post_id": value, "tags": ("value",)}
    :return: session object
    """
    for tag in data["tags"]:
        post = session.query(DatabaseModels.Posts).filter(DatabaseModels.Posts.post_id == data["id"]).first()
        tag_id = session.query(DatabaseModels.Tags).filter(DatabaseModels.Tags.tag_name == tag)
        post.tags.extend(tag_id)
        session.flush()
    return session


def tag_set_many(session, tag_post):
    """This funcs operates with list of several posts, which tags need to be added.
    :param session: current session object
    :param tag_post: list of dicts needed to pass to tags_set function.
    :return: session
    """
    for data in tag_post:
        session = tags_set(session, data)
    db_commit(session)
    return session


if __name__ == "__main__":
    session = create_db_connection()
    add_new_user(session, data.user_list)
    add_new_tags(session, data.tag_list)
    add_new_post_category(session, data.post_category_list)
    add_post(session, data.posts)
    tag_set_many(session, data.tag_post)
    print("Все добавилось!")