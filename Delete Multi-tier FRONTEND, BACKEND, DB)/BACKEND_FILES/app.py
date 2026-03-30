from flask import Flask, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql-service",
    user="root",
    password="password",
    database="testdb"
)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchall()

    if result:
        return "Login Successful"
    else:
        return "Invalid Credentials"

app.run(host='0.0.0.0', port=3000)
