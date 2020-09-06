import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from scrapper import christianity_text

db = {}
app = Flask("World Religions")




@app.route("/")
def home():
  return render_template("index.html")


@app.route("/christianity")
def christianity():
  c_text = christianity_text()
  db[christianity] = c_text
  text = db[christianity]
  return render_template("christianity.html", db_text=text)


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