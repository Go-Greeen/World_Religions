import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup


def christianity_text():
  url = "https://en.wikipedia.org/wiki/Christianity"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  c_text = soup.find("div",{"id":"mw-content-text"}).text
  return c_text


def islam_text():
  url = "https://en.wikipedia.org/wiki/Islam"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  i_text = soup.find("div",{"id":"mw-content-text"}).text
  return i_text



def hinduism_text():
  url = "https://en.wikipedia.org/wiki/Hinduism"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  h_text = soup.find("div",{"id":"mw-content-text"}).text
  return h_text



def buddhism_text():
  url = "https://en.wikipedia.org/wiki/Buddhism"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  b_text = soup.find("div",{"id":"mw-content-text"}).text
  return b_text