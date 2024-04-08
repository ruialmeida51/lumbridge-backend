import sqlite3

DB_FILE = 'expenses.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    try:
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error initializing database:", e)

# Call init_db() when this module is imported
init_db()

def get_expenses():
    try:
        conn = get_db_connection()
        expenses = conn.execute('SELECT * FROM expenses').fetchall()
        conn.close()
        return expenses
    except sqlite3.Error as e:
        print("Error getting expenses:", e)
        return []

# Function to add an expense to the database
def add_expense(description, amount):
    conn = get_db_connection()
    conn.execute('INSERT INTO expenses (description, amount) VALUES (?, ?)', (description, amount))
    conn.commit()
    conn.close()

# Function to delete an expense from the database
def delete_expense(expense_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()