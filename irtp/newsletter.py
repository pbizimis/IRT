import sqlite3

DATABASE = "irtp/databases/newsletter.db"
POST_EMAIL = """
INSERT INTO mails (EMAIL)
VALUES ("{}")
"""

def get_db():
    db = sqlite3.connect(DATABASE)
    db_cursor = db.cursor()
    return db, db_cursor

def post_email(email):
    db, db_cursor = get_db()
    db_cursor.execute(POST_EMAIL.format(email))
    db.commit()
    db.close()