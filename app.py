python
from flask import Flask
app = Flask(_name_)

@app.route("/")
def home():
    return "Tournament App is running!"

if _name_ == "_main_":
    app.run()
