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

@app.route('/skills/')
def skills():
    return render_template('skills.html')

@app.route('/undev/')
def undev():
    return render_template('undev.html', page_title="Jr Software Engineer | Undev | 2014-2015")

@app.route('/restream1/')
def restream1():
    return render_template('restream1.html', page_title="Software Engineer | Restream | 2015-2016")

@app.route('/restream2/')
def restream2():
    return render_template('restream2.html', page_title="Linux Engineer | Restream | 2016-2018")

@app.route('/restream3/')
def restream3():
    return render_template('restream3.html', page_title="Lead Linux Engineer | Restream | 2018-2021")

@app.route('/restream4/')
def restream4():
    return render_template('restream4.html', page_title="DevOps Engineer | Restream | 2021-2022")

@app.route('/zeal-group/')
def zealgroup():
    return render_template('zeal-group.html', page_title="Senior System Engineer | Zeal Group | 2021-2022")

@app.route('/volga-dnepr/')
def volgadnepr():
    return render_template('volga-dnepr.html', page_title='Junior system engineer | Volga-Dnepr | 2012-2013')

@app.route('/sre/')
def sre():
    return render_template('sre.html', page_title='SRE and incidents')