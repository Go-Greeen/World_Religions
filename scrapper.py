import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup


def christianity_text():
  url = "https://en.wikipedia.org/wiki/Christianity#:~:text=Christianity%20is%20an%20Abrahamic%20monotheistic,chronicled%20in%20the%20New%20Testament."
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  c_text = soup.find("div",{"id":"mw-content-text"}).text
  return c_text