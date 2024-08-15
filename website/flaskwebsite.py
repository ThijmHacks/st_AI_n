from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='./')

@app.route('/flaskhome')
def index():
    return render_template("index.html")

app.run(host="127.0.0.1", port=80)