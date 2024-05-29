import sqlite3

def reset_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    cursor.execute('''DROP TABLE IF EXISTS students''')
    cursor.execute('''CREATE TABLE students
                        (id INTEGER PRIMARY KEY, name TEXT,
                        age INTEGER, major TEXT)''')
    
    connection.commit()
    connection.close()

reset_database()

def insert_student(name, age, major):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    cursor.execute('''INSERT INTO students (name, age, major)
                        VALUES (?, ?, ?)''', (name, age, major))
    
    connection.commit()
    connection.close()

insert_student("kim", 20, "robotics")
insert_student("lee", 25, "computer engineering")

def query_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    connection.close()
    
    formatted_rows = [(row[0], row[1], row[2], row[3]) for row in rows]
    
    return formatted_rows

# Print the query result
print(query_students())

def update_student(student_id, name, age, major):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    cursor.execute('''UPDATE students SET name = ?,
                        age = ?, major = ? WHERE id = ?''',
                        (name, age, major, student_id))
    
    connection.commit()
    connection.close()

def delete_students(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    
    connection.commit()
    connection.close()
