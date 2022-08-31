from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='yash1234'
app.config['MYSQL_DB']='flask_api_db'
mysql = MySQL(app)



@app.route('/')
def index():
    Category='Dog'
    ID='5'
    Type='GSD'
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO pets_info(Category, ID, Type) VALUES(%s, %s, %s)", (Category, ID, Type))
    mysql.connection.commit()
    cur.close()
    return "Success"
   
if __name__ == '__main__':
    app.run(debug=True)