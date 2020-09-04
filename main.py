import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

db = []
app = Flask("World Religions")

@app.route("/")
def home():
  return render_template("index.html")









app.run(host = "0.0.0.0")