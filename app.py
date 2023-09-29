from flask import Flask,render_template,redirect,request,session,url_for
import mysql.connector


#conn=mysql.connector.connect(host="localhost",port='3306',database='abu',user='root',password='jnpw7708')
 
 
#cursor=conn.cursor()
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

''''

@app.route('/home')
def home():
    return render_template('index.html',username=session['username'])
        


@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor.execute('SELECT * FROM employee WHERE username=%s AND password=%s',(username,password))
        record=cursor.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for(index))
        else:
            msg='Incorrect username / password. Try it again..!'
    '''