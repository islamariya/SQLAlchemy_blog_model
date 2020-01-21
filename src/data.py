"""This module contents test data for DB population"""

import datetime

user_list = [{},"","Nelson", "Mariya", "Denis"]
tag_list = ["Python", {}, "Unittest", "SQLAlchemy", "Django", "Flask", "JavaScript"]
post_category_list = ["Программирование","", "Адинистрирование", "Дизайн", "Менеджмент"]

posts = [
    {"post_title": "Python Best Practices for More Pythonic Code",
     "post_date_creation": datetime.datetime.now(),
     "post_reading_time": "10 min",
     "author_id": 2,
     "category_id": 1,
     "post_text": "The articles and tutorials in this section contain best practices and other “nuggets of wisdom to "
                  "help your write better, more Pythonic code."},

    {"post_title": "Supercharge Your Classes With Python super",
     "post_date_creation": datetime.datetime.now(),
     "post_reading_time": "14 min",
     "author_id": 2,
     "category_id": 2,
     "post_text": "While Python isn’t purely an object-oriented language, it’s flexible enough and powerful enough to "
                  "allow you to build your applications using the object-oriented paradigm."},

    {"post_title": "Arcade: A Primer on the Python Game Framework",
     "post_date_creation": datetime.datetime.now(),
     "post_reading_time": "10 min",
     "author_id": 3,
     "category_id": 1,
     "post_text": "Computer games are a great way to introduce people to coding and computer science. Since I was"
                  " a player in my youth, the lure of writing video games was the reason I learned to code. "
                  "Of course, when I learned Python, my first instinct was to write a Python game."},

    {"post_title": "3 Python list comprehension tricks you might not know yet",
     "post_date_creation": datetime.datetime.now(),
     "post_reading_time": "12 min",
     "author_id": 1,
     "category_id": 1,
     "post_text": "If you’ve used Python you’re probably familiar with the list comprehension syntax."},

    {"post_title": "Organizing your Python Code In spite of yourself",
     "post_date_creation": datetime.datetime.now(),
     "post_reading_time": "4 min",
     "author_id": 2,
     "category_id": 1,
     "post_text": "The first question one might ask is why we need to organize our code, after all, spaghetti code "
                  "can work, even if it becomes an unreadable, hard to maintain mess"},

    {"post_title": "Document Your Python Code Without Writing Documentation",
     "post_date_creation": datetime.datetime.now(),
     "post_reading_time": "10 min",
     "author_id": 3,
     "category_id": 1,
     "post_text": "A programmer might read more code than he/she writes at certain points in their career, "
                  "so it must be frustrating to read badly documented code."},

    {"post_title": "Stop Using Lists for Everything in Python",
     "post_date_creation": datetime.datetime.now(),
     "post_reading_time": "7 min",
     "author_id": 1,
     "category_id": 1,
     "post_text": "When you’re learning something new, you’re unfamiliar with all the possibilities and once"
                  " something’s effective, you tend to stick with it… in Python, that something is lists."}
]

tag_post = [{"id": 1, "tags": ("Python", "JavaScript")},
            {"id": 2, "tags": ("Unittest",)},
            {"id": 3, "tags": ("Django", "Flask", "JavaScript")},
            {"id": 4, "tags": ("Unittest", "SQLAlchemy", "Django", "Flask")},
            {"id": 5, "tags": ("JavaScript",)},
            {"id": 6, "tags": ("Flask", "JavaScript")},
            {"id": 7, "tags": ("Unittest", "SQLAlchemy", "Django")},
            ]
