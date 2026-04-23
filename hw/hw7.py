import sqlite3

connect = sqlite3.connect("store.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
''')

connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products(name, price, quantity) VALUES (?,?,?)',
        (name, price, quantity)
    )
    connect.commit()

def read_products():
    cursor.execute('SELECT * FROM products')
    for product in cursor.fetchall():
        print(product)

def update_product(id, price):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (price, id)
    )
    connect.commit()

def delete_product(id):
    cursor.execute(
        'DELETE FROM products WHERE id = ?',
        (id,)
    )
    connect.commit()

create_product("Телефон", 300, 5)
create_product("Ноутбук", 800, 3)
create_product("Наушники", 50, 10)

read_products()

update_product(1, 350)
read_products()

delete_product(2)
read_products()