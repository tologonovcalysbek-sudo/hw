import sqlite3

connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
''')

connect.commit()




def add_user(name):
    cursor.execute('INSERT INTO users(name) VALUES (?)', (name,))
    connect.commit()


def add_movie(title, genre):
    cursor.execute('INSERT INTO movies(title, genre) VALUES (?,?)', (title, genre))
    connect.commit()


def add_review(user_id, movie_id, rating):
    cursor.execute(
        'INSERT INTO reviews(user_id, movie_id, rating) VALUES (?,?,?)',
        (user_id, movie_id, rating)
    )
    connect.commit()



def show_reviews():
    cursor.execute('''
        SELECT users.name, movies.title, reviews.rating
        FROM reviews
        JOIN users ON reviews.user_id = users.id
        JOIN movies ON reviews.movie_id = movies.id
    ''')
    for row in cursor.fetchall():
        print(row)

def show_all_movies():
    cursor.execute('''
        SELECT movies.title, reviews.rating
        FROM movies
        LEFT JOIN reviews ON movies.id = reviews.movie_id
    ''')
    for row in cursor.fetchall():
        print(row)


def stats():
    cursor.execute('SELECT AVG(rating) FROM reviews')
    print("Средняя:", cursor.fetchone()[0])

    cursor.execute('SELECT MAX(rating) FROM reviews')
    print("Макс:", cursor.fetchone()[0])

    cursor.execute('SELECT MIN(rating) FROM reviews')
    print("Мин:", cursor.fetchone()[0])


add_user("Kalys")
add_user("Chuke")
add_user("Altyke")
add_user("Namke")
add_user("Lesha")

add_movie("Inception", "Sci-Fi")
add_movie("Titanic", "Drama")
add_movie("Avatar", "Fantasy")
add_movie("Joker", "Crime")
add_movie("Interstellar", "Sci-Fi")

add_review(1, 1, 9)
add_review(2, 1, 8)
add_review(3, 2, 7)
add_review(4, 2, 10)
add_review(5, 3, 9)
add_review(1, 3, 8)
add_review(2, 4, 9)
add_review(3, 4, 6)
add_review(4, 5, 10)
add_review(5, 5, 7)

print("\n Отзывы")
show_reviews()

print("\n Все фильмы ")
show_all_movies()

print("\n Статистика ")
stats()