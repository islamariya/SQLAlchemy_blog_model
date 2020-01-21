"""This module """

from sqlalchemy import func
from sqlalchemy.exc import OperationalError

from DatabaseModels import User, Posts, tag_posts_relation
from db_operations import create_db_connection
from logs import logging


def get_user_posts(session, username, tags_qt):
    """This func loads from DB posts of particular user which have at least tags_qt tags.
    :param session:
    :param username: string, User, whose posts you want to get
    :param tags_qt: int, min qt of tags post should have to be selected
    :return list of tuples (post_id, Post title, post's tags number)
    """
    is_user_exist = session.query(User.user_name).filter(User.user_name == username).first()
    if is_user_exist:
        posts_found = session.query(Posts, func.count(tag_posts_relation.c.post_id).label("TagsNum")
                                    ).join(tag_posts_relation, User).group_by(Posts).filter(User.user_name == username
                                                                                            ).having(
            func.count(tag_posts_relation.c.post_id) >= tags_qt).all()
        return posts_found
    else:
        print(f"Пользователя {username} в БД нет")


def print_results(posts_found, username, tags_qt):
    """This function prints the search results in console
    :param my_query: list of results found get_user_posts
    :param username: string, User, whose posts you want to get
    :param tags_qt: int, min qt of tags post should have to be selected
    """
    successful_message = f"У пользователя {username} найдено {len(posts_found)} постов с {tags_qt} тегами и больше \n" \
                         f"Список постов и кол-во тегов:"
    zero_result_found_message = f"Постов с {tags_qt} тегами у пользователя {username} не найдено."
    message_to_print = successful_message if len(posts_found) > 0 else zero_result_found_message
    print(message_to_print)
    for result in posts_found:
        print(result)


if __name__ == "__main__":
    session = create_db_connection()
    username = "Alise"
    tags_qt = 5
    try:
        posts_found = get_user_posts(session, username, tags_qt)
        print_results(posts_found, username, tags_qt)
    except TypeError:
        logging.exception("TypeError")
        print("Ничего не найдено")
    except OperationalError:
        logging.exception("OperationalError")
        print(f"БД сйчас недоступна")
