"""This module creates a database tables"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, DatabaseError

import DatabaseModels
from logs import logging


DATABASE_NAME = "sqlite:///blog_db"


def create_db(DATABASE_NAME):
    """This func creates a database and it's models, provided in DatabaseModels.
    :param DATABASE_NAME: sting "dbtype:///db_name", for example, "sqlite:///blog_db"
    """
    engine = create_engine(DATABASE_NAME, echo=True)
    try:
        DatabaseModels.Base.metadata.create_all(engine)
        print("Все прошло успешно!")
    except SQLAlchemyError:
        logging.exeption("Database models creation error")


def create_db_connection(DATABASE_NAME="sqlite:///blog_db"):
    """This func creates a session for a DB using a scoped_session.
    :param DATABASE_NAME: sting "dbtype:///db_name", for example, "sqlite:///blog_db"
    :return: session object
    """
    try:
        engine = create_engine(DATABASE_NAME, echo=False)
        session_factory = sessionmaker(bind=engine)
        Session = scoped_session(session_factory)
        session = Session()
    except DatabaseError:
        print("Ошибка соединения с БД")
        logging.exeption("Connection Error")
    return session


def db_commit(session):
    """This function adds changes stored in session to database."""
    try:
        session.commit()
    except DatabaseError:
        session.rollback()
        logging.exeption("Database commit error")


if __name__ == "__main__":
    create_db(DATABASE_NAME)
