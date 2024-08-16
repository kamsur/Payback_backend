"""
Starting point of the program
"""

from flask import Flask


app = Flask(__name__)


@app.get("/add")  # adding records to database
def add():
    return "Addition"


@app.get("/")  # default home page
def main():
    return "Hello, World!"
