from flask import Flask, render_template, json
import mysql.connector
from getpass import getpass
import os

# Configuration
app = Flask(__name__)

# Connection settings for AWS MySql instance
db_connection = mysql.connector.connect(
    user = 'admin', 
    password = getpass("Enter Password: "), 
    host = 'cs340db.cl02izp609gp.us-west-2.rds.amazonaws.com',
    database = 'classicModels'
)

# Routes 
@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/customer')
def bsg_people(): 

    query = "SELECT * FROM customers;"

    cur = db_connection.cursor()
    cur.execute(query)

    return json.dumps(cur.fetchall())

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4932)) 
    app.run(port=port, debug=False) 