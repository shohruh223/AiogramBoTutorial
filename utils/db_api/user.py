import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("user.db")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
        self.cursor.execute("""
        create table if not exists users(
            id integer primary key,
            fullname varchar not null,
            age integer,
            phone_number varchar,
            photo varchar
        )""")

    def add_user(self, fullname, age, phone_number, photo):
        self.cursor.execute("insert into users (fullname, age, phone_number, photo) values (?,?, ?,?)",
                            (fullname, age, phone_number, photo))
        self.connection.commit()

    def get_user(self, id):
        self.cursor.execute("select * from users where id=?", (id,))
        return self.cursor.fetchone()

    def all_user(self):
        self.cursor.execute("select * from users")
        return self.cursor.fetchall()

    def edit_user(self, id, fullname, age, phone_number, photo):
        self.cursor.execute("update users set fullname=?, age=?, phone_number=?, photo=? where id=?",
                            (fullname, age, phone_number, photo, id))
        self.connection.commit()

    def delete_user(self, id):
        self.cursor.execute("delete from users where id=?", (id,))
        self.connection.commit()

