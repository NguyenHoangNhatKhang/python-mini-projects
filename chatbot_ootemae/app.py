from flask import Flask,render_template,url_for,redirect,request,jsonify
import openai 
import json 
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("API_KEY")

with open("chatbot_ootemae/ex.json",'r') as f:
    school_data = json.load(f)


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
@app.route("/chat-answer",methods=["POST"])
def chat_answer():
    # dict 
    data = request.get_json() 
    user_message = data.get("message","")
    prompt =f"""
    あなたは大手前大学に関する質問に答えるチャットボットです。
以下の学校データに基づいて、日本語で正確かつ親切に答えてください。

'大手前大学に関する情報'
{json.dumps(school_data,ensure_ascii=False)}
'質問'
{user_message}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages = [
            {"role":"system","content":"あんたは大手前大学のAI",
             "role":"user","content":prompt}
        ]
    )
    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)