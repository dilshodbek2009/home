import sqlite3


class Databae:
    def __init__(self):
        self.connection = sqlite3.connect("dilshod.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key ,
                burger varchar not null ,
                lavash varchar not null ,
                hot_dog varchar ,
                shaurma varchar ,
                fries integer not null,
                snacks varchar not null )
        """)