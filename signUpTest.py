import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "MySQLRootPassword",
    "database": "a1",
}

db = mysql.connector.connect(**db_config)

cursor = db.cursor()

# cursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# cursor.execute("DESCRIBE Person")
cursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Jerry", 30))
db.commit()
cursor.execute("SELECT * FROM Person")


for output in cursor:
    print(output)
