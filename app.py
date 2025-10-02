python
from flask import Flask, render_template, request
import base64
import os

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image_data = request.form['image']
    image_data = image_data.replace('data:image/png;base64,', '')
    image_data = base64.b64decode(image_data)

    filename = 'static/captured/image.png'
    with open(filename, 'wb') as f:
        f.write(image_data)

    return 'Saved'

if _name_ == '_main_':
    app.run(debug=True)
