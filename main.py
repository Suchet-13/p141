from flask import Flask, jsonify, request
import csv
import pandas as pd
from storage import all_articles, liked_articles, not_liked_articles

app = Flask(__name__)

with open('csv/articles.csv', "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]