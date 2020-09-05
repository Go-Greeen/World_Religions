import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

db = []
app = Flask("World Religions")




@app.route("/")
def home():
  return render_template("index.html")


@app.route("/christianity")
def christianity():
  return render_template("christianity.html")


@app.route("/islam")
def islam():
  return render_template("islam.html")


@app.route("/hinduism")
def hinduism():
  return render_template("hinduism.html")


@app.route("/buddhism")
def buddhism():
  return render_template("buddhism.html")








app.run(host = "0.0.0.0")