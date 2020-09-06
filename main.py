import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from scrapper import christianity_text, islam_text, hinduism_text, buddhism_text


app = Flask("World Religions")


db = {}

@app.route("/")
def home():
  return render_template("index.html")


@app.route("/christianity")
def christianity():  
  fromDb = db.get("christianity")
  if fromDb:
    text = fromDb
  else:
    c_text = christianity_text()
    db["christianity"] = c_text
    text = db["christianity"]
  return render_template("christianity.html", db_text=text)


@app.route("/islam")
def islam():
  fromDb = db.get("islam")
  if fromDb:
    text = fromDb
  else:
    i_text = islam_text()
    db["islam"] = i_text
    text = db["islam"]
  return render_template("islam.html", db_text=text)


@app.route("/hinduism")
def hinduism():
  fromDb = db.get("hinduism")
  if fromDb:
    text = fromDb
  else:
    h_text = hinduism_text()
    db["hinduism"] = h_text
    text = db["hinduism"]
  return render_template("hinduism.html", db_text=text)


@app.route("/buddhism")
def buddhism():
  fromDb = db.get("buddhism")
  if fromDb:
    text = fromDb
  else:
    b_text = buddhism_text()
    db["buddhism"] = b_text
    text = db["buddhism"]
  return render_template("buddhism.html", db_text=text)








app.run(host = "0.0.0.0")