import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/cover-letter/')
def coverletter():
    return render_template('cover-letter.html')

@app.route('/bios/')
def bios():
    return render_template('bios.html', page_title='Mike Dronov Resume')

@app.route('/restream/')
def restream():
    return render_template('restream.html')

@app.route('/volga-dnepr/')
def volgadnepr():
    return render_template('volga-dnepr.html', page_title='Junior system engineer [Volga-Dnepr] [2012-2013]')