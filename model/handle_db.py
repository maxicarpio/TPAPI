import sqlite3


class HandleDB():
    def __init__(self):
        self._conn = sqlite3.connect("./scholarships.db")
        self._cursor = self._conn.cursor()

    def get_all(self):
        data = self._cursor.execute("SELECT * FROM scholarships")
        return data.fetchall()

    def get_only(self, data_scholarship):
        data = self._cursor.execute("SELECT * FROM scholarships WHERE  name = -'{}'".format(data_scholarship))

        return data.fetchone()
    
    def insert(self, data_scholarship):
        self._cursor.execute("INSERT INTO scholarships VALUES ('{}','{}','{}','{}','{}')".format(
            data_scholarship['id'],
            data_scholarship['name'],
            data_scholarship['description'],
            data_scholarship['price'],
            data_scholarship['image']
        ))
        self._conn.commit()

    def __del__(self):
        self._conn.close()


db = HandleDB()
data = {
    'id': 2,
    'image': '/images/govuk.jpeg',
    'name': 'Regional Student Competition',
    'description': 'Description 1',
    'price': 1000
}
db.insert(data)
print(db.get_all())