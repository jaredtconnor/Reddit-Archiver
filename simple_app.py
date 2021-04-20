from flask import Flask, render_template, json
import mysql.connector
from getpass import getpass
import os


# Configuration
app = Flask(__name__)

db_connection = mysql.connector.connect(
    user = 'root', 
    password = getpass("Enter Password: "), 
    host = 'localhost',
    database = 'bsg'
)

# Routes 
@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/bsg-people')
def bsg_people(): 

    query = "SELECT * FROM bsg_people;"

    cur = db_connection.cursor()
    cur.execute(query)

    return json.dumps(cur.fetchall())

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4932)) 
    app.run(port=port, debug=False) 