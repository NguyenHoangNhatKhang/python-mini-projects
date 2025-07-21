from flask import Flask , redirect , url_for ,render_template, request
app = Flask(__name__)
@app.route('/index')
def hello_world():
    return render_template('home.html',content="kahng dep trai",cars="kelvin")

@app.route('/user/<name>')
def hello_user(name):
    if name =="admin":
        return redirect(url_for('hello_admin'))
    return f"hello  {name}"

@app.route('/login',methods=["POST","GET"])
def login():
    if request
    return render_template('login.html')

@app.route('/admin')
def hello_admin():
    return "hello admin"
if __name__ == "__main__":
    app.run(debug=True)