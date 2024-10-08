import mysql.connector

# Function to create a connection to the database
def create_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Krishna3_6_9',
        database='school_db'
    )

# Admin login function
def admin_login(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE user_name=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

# CRUD operations for student table
def add_student(conn, name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark, class_teacher):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO student (name, age, sex, class, fees, rank, english_mark, python_mark, math_mark, class_teacher)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark, class_teacher))
    conn.commit()
    cursor.close()

def view_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    for row in cursor.fetchall():
        print(row)
    cursor.close()

def update_student(conn, sno, name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark, class_teacher):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE student SET name=%s, age=%s, sex=%s, class=%s, fees=%s, rank=%s,
        english_mark=%s, python_mark=%s, math_mark=%s, class_teacher=%s WHERE sno=%s
    """, (name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark, class_teacher, sno))
    conn.commit()
    cursor.close()

def delete_student(conn, sno):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE sno=%s", (sno,))
    conn.commit()
    cursor.close()

# Main function with user interface
def main():
    conn = create_connection()

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if not admin_login(conn, username, password):
        print("Invalid credentials")
        return

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            sex = input("Enter sex (Male/Female): ")
            class_name = input("Enter class: ")
            fees = float(input("Enter fees: "))
            rank = int(input("Enter rank: "))
            english_mark = int(input("Enter English mark: "))
            python_mark = int(input("Enter Python mark: "))
            math_mark = int(input("Enter Math mark: "))
            class_teacher = input("Enter class teacher's name: ")
            add_student(conn, name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark, class_teacher)
            print("Student added successfully.")

        elif choice == '2':
            print("Viewing all students:")
            view_students(conn)

        elif choice == '3':
            sno = int(input("Enter student number to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            sex = input("Enter new sex (Male/Female): ")
            class_name = input("Enter new class: ")
            fees = float(input("Enter new fees: "))
            rank = int(input("Enter new rank: "))
            english_mark = int(input("Enter new English mark: "))
            python_mark = int(input("Enter new Python mark: "))
            math_mark = int(input("Enter new Math mark: "))
            class_teacher = input("Enter new class teacher's name: ")
            update_student(conn, sno, name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark, class_teacher)
            print("Student updated successfully.")

        elif choice == '4':
            sno = int(input("Enter student number to delete: "))
            delete_student(conn, sno)
            print("Student deleted successfully.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == '__main__':
    main()
