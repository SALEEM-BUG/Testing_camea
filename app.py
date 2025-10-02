python
from flask import Flask, render_template

app = Flask(_app_)

@app.route('/')
def home():
    return "Welcome to the Tournament Website!"

if _name_ == '_main_':
    app.run(debug=True)
