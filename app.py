import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/bios/')
def bios():
    return render_template('bios.html')

@app.route('/restream/')
def restream():
    return render_template('restream.html')