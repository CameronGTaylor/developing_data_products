from flask import Flask, render_template, request
from random import randint
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice')
def roll_dice():
    # all_3 = str(np.random.randint(1,7))+ ' ' + \
    #         str(np.random.randint(1,7))+ ' ' + \
    #         str(np.random.randint(1,7))
    # return all_3
    # return ('\r\n').join([str(randint(1,6)) for i in range(3)])
    rolls = [str(randint(1,6)) for i in range(3)]
    return render_template('roll_dice.html', rolls=rolls)

@app.route('/spam-finder')
def spam_or_ham_form():
    return render_template('spam_finder.html')

@app.route('/spam-finder', methods=['POST'])
def spam_or_ham_results():
    n = request.form['submission']
    result = predict(n)
    return render_template('spam_results.html', n=n,result=result)
