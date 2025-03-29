import sqlite3

class HandleDB():
    """"
    Class to handle the database operations.
    Attributes:
        _conn (sqlite3.Connection): SQLite connection object.
        _cursor (sqlite3.Cursor): SQLite cursor object.
    """
    def __init__(self):
        """
        Initialize the database connection and cursor.
        Args:
            None
        Returns:
            None
        """
        self._conn = sqlite3.connect("scholarships.db")
        self._cursor = self._conn.cursor()

    def get_all(self):
        """
        Get all scholarships from the database.
        Args:
            None
        Returns:
            list: A list of tuples containing all scholarships.
        """
        data = self._cursor.execute("SELECT * FROM scholarships")
        return data.fetchall()

    def get_only(self, data_scholarship: str):
        """
        Get a specific scholarship from the database.
        Args:
            data_scholarship (str): The name of the scholarship to retrieve.
        Returns:
            uple: A tuple containing the scholarship data.
        """
        data = self._cursor.execute("SELECT * FROM scholarships WHERE  name = -'{}'".format(data_scholarship))

        return data.fetchone()
    
    def insert(self, data_scholarship: dict):
        """
        Insert a new scholarship into the database.
        Args:
            data_scholarship (dict): A dictionary containing scholarship data.
        Returns:
            None
        """
        self._cursor.execute("INSERT INTO scholarships VALUES ('{}','{}','{}','{}','{}')".format(
            data_scholarship['id'],
            data_scholarship['name'],
            data_scholarship['description'],
            data_scholarship['price'],
            data_scholarship['image']
        ))
        self._conn.commit()

    def delete_all(self):
        """
        Delete all scholarships from the database.
        Args:
            None
        Returns:
            None
        """
        self._cursor.execute("DELETE FROM scholarships")
        self._conn.commit()

    def delete_only(self, data_scholarship):
        
        self._cursor.execute("DELETE FROM scholarships WHERE name = '{}'".format(data_scholarship))
        self._conn.commit()

    def modify(self, data_scholarship):
        self._cursor.execute("UPDATE scholarships SET name = '{}', description = '{}', price = '{}', image = '{}' WHERE id = '{}'".format(
            data_scholarship['name'],
            data_scholarship['description'],
            data_scholarship['price'],
            data_scholarship['image'],
            data_scholarship['id']
        ))
        self._conn.commit()

    def __del__(self):
        self._conn.close()

db = HandleDB()
db.get_all()