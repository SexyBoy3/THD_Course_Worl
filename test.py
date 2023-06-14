import tkinter as tk
import psycopg2
from tkinter import messagebox

# Database connection details
DB_NAME = "LaptopsHardware"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"

# Create a database connection
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        messagebox.showerror("Error", str(e))


# Execute a SQL query and return the results
def execute_query(query, params=None):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return result
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
            conn.close()
        messagebox.showerror("Error", str(e))


# GUI Application
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Database Application")
        self.geometry("600x400")

        # Create a connection
        self.conn = create_connection()

        # Create a label and entry for query input
        self.query_label = tk.Label(self, text="Enter Query:")
        self.query_label.pack()
        self.query_entry = tk.Entry(self, width=50)
        self.query_entry.pack()

        # Create a button to execute the query
        self.execute_button = tk.Button(
            self, text="Execute", width=10, command=self.execute_query
        )
        self.execute_button.pack()

        # Create a text widget to display the query result
        self.result_text = tk.Text(self, height=10, width=80)
        self.result_text.pack()

    # Execute the query and display the result
    def execute_query(self):
        query = self.query_entry.get()
        result = execute_query(query)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, str(result))

    def __del__(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    app = Application()
    app.mainloop()