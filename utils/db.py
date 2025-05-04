import sqlite3

conn = sqlite3.connect("qa_history.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS history (question TEXT, answer TEXT)")
conn.commit()

def store_qa(question, answer):
    cursor.execute("INSERT INTO history (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()

def get_history():
    cursor.execute("SELECT question, answer FROM history ORDER BY rowid DESC")
    return cursor.fetchall()
