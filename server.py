from flask import Flask,render_template,request,redirect,session
import random
app = Flask(__name__)
app.secret_key = 'Kylo'


@app.route('/')
def index():
    if session.get('attempt') is None:
        session['attempt'] = 0
    if session['attempt'] >= 5:
        return render_template('you_lose.html')
    if session.get('random') is None:
        session['random'] = random.randint(1,100)
        return render_template('index.html')
    if session['number'] > session['random']:
        return render_template('too_high.html')
    elif session['number'] < session['random']:
        return render_template('too_low.html')
    elif session['number'] == session['random']:
        return render_template('correct.html')
    else:
        return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['number'] = int(request.form.get('number'))
    session['attempt'] += 1
    print(session['number'])
    return redirect('/')

@app.route('/playAgain', methods=['POST'])
def playAgain():
    session['random'] = random.randint(1,100)
    session['attempt'] = 0
    return render_template('index.html')

@app.route('/exit',)
def exit():
    session['random'] = None
    session['attempt'] = 0
    return redirect('/')











if __name__ == '__main__':
    app.run(debug=True)