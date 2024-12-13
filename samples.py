import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "mikesito", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "LoreSol", hashlib.sha256("holahola".encode()).hexdigest()
username3, password3 = "JoseJose", hashlib.sha256("subway3x1".encode()).hexdigest()
username4, password4 = "bruhXxX", hashlib.sha256("iliketoads".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()