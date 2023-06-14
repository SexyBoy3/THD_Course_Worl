import psycopg2
import tkinter as tk
connection = psycopg2.connect(
    user="postgres",
    password="1234",
    host="localhost",
    database="LaptopsHardware"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM public." +'"' + "Laptops" + '"' + " ORDER BY " + '"'+ "Model" + '"'+  " ASC ")
results = cursor.fetchall()
for rows in results:
    print(rows)

window = tk.Tk()

# Создайте текстовое поле (Text) или таблицу (Table) для отображения данных
text_field = tk.Text(window)
text_field.pack()

# Выведите данные в текстовом поле
for row in rows:
    text_field.insert(tk.END, str(row) + "\n")

# Запустите основной цикл tkinter
window.mainloop()
