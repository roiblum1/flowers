from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def flowers():
    # Print debugging information
    print("Rendering flower.html template")
    return render_template('flower.html')

@app.route('/apology')
def apology():
    # Print debugging information
    print("Rendering index.html template")
    return render_template('index.html')

@app.route('/more', endpoint='more')
def flowers2():
    return render_template('flower2.html')

@app.route('/heart', endpoint='heart')
def heart():
    return render_template('heart.html')

if __name__ == '__main__':
    app.run(debug=True)