from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hank_aaron')
def hank_aaron():
    return render_template('hank_aaron.html')

@app.route('/chipper_jones')
def chipper_jones():
    return render_template('chipper_jones.html')

@app.route('/greg_maddux')
def greg_maddux():
    return render_template('greg_maddux.html')

@app.route('/freddie_freeman')
def freddie_freeman():
    return render_template('freddie_freeman.html')

@app.route('/ronald_acuna')
def ronald_acuna():
    return render_template('ronald_acuna.html')
