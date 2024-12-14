from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import hashlib
import sqlite3
import os
import sys

app = Flask(__name__)
app.secret_key = 'cow'

parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.insert(0, parent_dir)
from chat import chatWithGPT
def checkUserOnly(username):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '..', 'userdata.db')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ?", (username,))
    if cur.fetchone():
        # print(f"Login Successful! Welcome, {username}")
        return True
    else:
        # print(f"Invalid username or password")
        return False
def checkUserAndPass(username, password):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '..', 'userdata.db')
    password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
    if cur.fetchone():
        # print(f"Login Successful! Welcome, {username}")
        """ Logic for succesful login """
        return True
    else:
        # print(f"Invalid username or password")
        return False

def addUser(username, password):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '..', 'userdata.db')
    password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    return


@app.route("/")
def index():
    #
    return render_template("web.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['username']  # Get username from form input
        password = request.form['password']
        if (checkUserAndPass(username, password)):
            print(f"logic for user entry")
            print(url_for('menu'))

            return redirect('/menu')

    return render_template("login.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")
@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if not checkUserOnly(username):
            addUser(username, password)
            flash("Register successful!", "success")
            # return jsonify({"status": "success", "message": "Registration successful!"})
        else:
            flash("Register failed!", "notsuccess")
            # return jsonify({"status": "exists", "message": "User already exists!"})

    return render_template("login.html")

@app.route("/pers1", methods=['POST', 'GET'] )
def pers1():
    if request.method == 'POST':
        message = request.form['userInput']
        print(f"message fetched, it was: {message}")
        bot_response = chatWithGPT("pers1", message)
        print(f"Bot: {bot_response.choices[0].message.content}")

    return render_template("pers1.html")



app.run(host="0.0.0.0", port=80)