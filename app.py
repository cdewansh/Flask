from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder="templates")

todos = [{'todo':"Sample todo", "Done": False}]

""" '@' decorator function in Python
use: defines a route in a Flask application, and when a user accesses the root URL, 
it calls the index function, which renders an HTML template and passes a variable (todos) 
to that template, which can be used to display dynamic data in the web page"""
@app.route('/')
def index():
    return render_template("index.html", todos = todos)


# Code is executed only when file is excuted as main file.
if __name__ == "__main__":
    app.run(debug=True)