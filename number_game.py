from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'
import random

@app.route('/')
def home():
    try:
	print "test"
        session['temp'] == 1
    except:
        session['guess'] = random.randrange(0,101)
        session['temp'] = 1
        session['number_test'] = None
    return render_template('number.html')

@app.route('/check', methods=['POST'])
def test():
    session['number_test'] = int(request.form['number_guess'])
    return redirect('/')

@app.route('/replay', methods=['POST'])
def play_again():
    session.clear()
    return redirect('/')

app.run(debug=True)
