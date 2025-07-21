from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method =="POST":
        email = request.form.get('email')
        password = request.form.get('password')
        # call func name not url 
        if email == "admin@otemae.ac.jp" and password == "123":
            return redirect(url_for('chatGui')) 
        else:
            return render_template('login.html',error="❌ Wrong Password") 
    return render_template("login.html")

@app.route('/login/main')
def chatGui():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)