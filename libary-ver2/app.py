from flask import Flask, redirect, url_for
from book import Book
from libary import Library 
from manager import Manager 
from customer import Customer 
app = Flask()

@app.route("/",methods=["GET","POST"])
def 


@app.route("/customers",methods=["GET"])

@app.route("/library",methods=["GET"])