import sqlite3

# 1. ESTABLISH CONNECTION
# This creates 'example.db' if it doesn't exist
connection = sqlite3.connect('example.db') 

# 2. CREATE A CURSOR
# The cursor is like a "pointer" that allows you to traverse the records
cursor = connection.cursor()

# 3. EXECUTE SQL COMMANDS
# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")

# 4. COMMIT (SAVE) CHANGES
# IMPORTANT: Data isn't saved until you commit!
connection.commit()

# 5. FETCH DATA (To verify it worked)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

# 6. CLOSE CONNECTION
connection.close()
x = input("enter:")
if x==7 :
    print("hello")
else :
    print("k")