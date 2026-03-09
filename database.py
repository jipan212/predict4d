import sqlite3
import csv
import os

DB = "data/numbers.db"
CSV = "data/history.csv"


def init_db():

    if not os.path.exists("data"):
        os.makedirs("data")

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS numbers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_number(num):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("INSERT INTO numbers (number) VALUES (?)",(num,))
    conn.commit()

    conn.close()

    update_csv()


def get_numbers():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT number FROM numbers")

    rows = cur.fetchall()

    conn.close()

    return [r[0] for r in rows]


def update_csv():

    numbers = get_numbers()

    with open(CSV,"w",newline="") as f:

        writer = csv.writer(f)
        writer.writerow(["number"])

        for n in numbers:
            writer.writerow([n])