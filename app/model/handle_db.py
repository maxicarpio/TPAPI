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
        try:
            print("Connecting to the database...")
            self._conn = sqlite3.connect("scholarships.db")
            self._cursor = self._conn.cursor()
            print("Database connected successfully.")
        except sqlite3.Error as ERROR: #Handle any SQLite errors
            print(f"Error connecting to database: {ERROR}")

    def get_all(self):
        """
        Get all scholarships from the database.
        Args:
            None
        Returns:
            list: A list of tuples containing all scholarships.
        """
        try:
            print("Fetching all the data from the database...")
            data = self._cursor.execute("SELECT * FROM scholarships")
            return data.fetchall() #Fetch all scholarships from the database
            print("All Data fetched successfully.")
        except sqlite3.Error as ERROR: #Handle any SQLite errors
            print(f"Error fetching data: {ERROR}")

    def get_only(self, id_scholarship: int):
        """
        Get a specific scholarship from the database.
        Args:
            id_scholarship (int): The id of the scholarship to retrieve.
        Returns:
            Tuple: A tuple containing the scholarship data.
        """
        try:
            print("Fetching data from the database...")
            data = self._cursor.execute(
                "SELECT * FROM scholarships WHERE  id = ?",(id_scholarship,)
            )

            print("Data fetched successfully.")
            return data.fetchone() #Fetch a specific scholarship from the database

        except sqlite3.Error as ERROR: #Handle any SQLite errors
            print(f"Error fetching data: {ERROR}")
            raise
    
    def insert(self, data_scholarship: dict):
        """
        Insert a new scholarship into the database.
        Args:
            data_scholarship (dict): A dictionary containing scholarship data.
            Example:
                {
                    "name": "Scholarship Name",
                    "description": "Scholarship Description",
                    "price": "1000",
                    "image": "images/example.png"
                }
        Returns:
            None
        """
        try:
            print("Inserting data into the database...")
            # Check if the table exists, if not create it
            self._cursor.execute(
                "INSERT INTO scholarships (name, description, price, image) VALUES (?, ?, ?, ?)",
                (
                    data_scholarship['name'],
                    data_scholarship['description'],
                    data_scholarship['price'],
                    data_scholarship['image'],
                ),
            )
            self._conn.commit() #Commit the changes to the database
            print("Data inserted successfully.")
        except sqlite3.Error as ERROR: #Handle any SQLite errors
            print(f"Error inserting data: {ERROR}")
            raise

    def delete_all(self):
        """
        Delete all scholarships from the database.
        Args:
            None
        Returns:
            None
        """
        try:
            print("Deleting all data from the database...")
            self._cursor.execute("DELETE FROM scholarships")
            self._cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'scholarships';") #Reset the auto-increment counter for the scholarships table
            #This is important to reset the ID counter after deleting all records
            self._conn.commit()
            print("All data deleted successfully.")
        except sqlite3.Error as ERROR: #Handle any SQLite errors
            print(f"Error deleting all data: {ERROR}")
            raise

    def delete_only(self, id_scholarship: int):
        """
        Delete a specific scholarship from the database.
        Args:
            id_scholarship (int): The ID of the scholarship to delete.
        Returns:
            None
        """
        try:
            print("Deleting data from the database...")
            self._cursor.execute(
                "DELETE FROM scholarships WHERE id = ?",(id_scholarship,)
            )
            self._conn.commit()
            print("Data deleted successfully.")
        except sqlite3.Error as ERROR: #Handle any SQLite errors
            print(f"Error deleting data: {ERROR}")
            raise

    def modify(self, scholarship_id: int, data_scholarship: dict):
        """
        Modify an existing scholarship in the database.
        Args:
            scholarship_id (int): The ID of the scholarship to modify.
            data_scholarship (dict): A dictionary containing updated scholarship data.
            Example:
                {
                    "name": "Updated Scholarship Name",
                    "description": "Updated Scholarship Description",
                    "price": "2000",
                    "image": "images/updated_example.png"
                }
        Returns:
            None
        """
        try:
            print("Checking if the scholarship exists...")
            existing_scholarship = self.get_only(scholarship_id)
            
            print("Modifying data in the database...")
            self._cursor.execute(
                "UPDATE scholarships SET name = ?, description = ?, price = ?, image = ? WHERE id = ?",
            (
                data_scholarship['name'],
                data_scholarship['description'],
                data_scholarship['price'],
                data_scholarship['image'],
                scholarship_id, #ID of the scholarship to be modified, this does not change
            ))
            self._conn.commit()
            print("Data modified successfully.")
        except sqlite3.Error as ERROR: #Handle any SQLite errors
            print(f"Error modifying data: {ERROR}")
            raise

    def __del__(self):
        """
        Close the database connection when the object is deleted.
        Args:
            None
        Returns:
            None
        """
        print("Closing the database connection...")
        self._conn.close()
        print("Connection closed.")