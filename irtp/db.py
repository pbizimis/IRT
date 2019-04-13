import sqlite3

DATABASE = "irtp/databases/articles.db"
GET_ARTICLES = "Select * from articles"

def get_db():
    db = sqlite3.connect(DATABASE)
    db_cursor = db.cursor()
    return db, db_cursor

def get_articles():

    db, db_cursor = get_db()
    db_cursor.execute(GET_ARTICLES)
    articles = db_cursor.fetchall()
    #for i, article in enumerate(articles):
    #    articles[i] = list(article)
    #    articles[i][2] = article[2].split(".")
    db.close()
    return articles