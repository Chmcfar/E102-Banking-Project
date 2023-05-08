import unittest
import mysql.connector

# Define the database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MySQLRootPassword',
    'database': 'a1',
}


class TestDatabaseInteraction(unittest.TestCase):
    def setUp(self):
        # Connect to the testing database
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

        # Create a test table
        self.cursor.execute(
            "CREATE TABLE test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

        # Insert some test data
        self.cursor.execute(
            "INSERT INTO test_table (name, age) VALUES ('Alice', 25), ('Bob', 30)")

    def tearDown(self):
        # Drop the test table
        self.cursor.execute("DROP TABLE test_table")

        # Close the database connection
        self.cursor.close()
        self.connection.close()

    def test_query(self):
        # Test a query that should return two rows
        self.cursor.execute("SELECT * FROM test_table")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 2)

    def test_insert(self):
        # Test inserting a new row into the test table
        self.cursor.execute(
            "INSERT INTO test_table (name, age) VALUES ('Charlie', 35)")
        self.connection.commit()

        # Test that the row was inserted correctly
        self.cursor.execute("SELECT * FROM test_table WHERE name='Charlie'")
        row = self.cursor.fetchone()
        self.assertIsNotNone(row)


if __name__ == '__main__':
    unittest.main()
