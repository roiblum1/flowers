from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def flowers():
    # Print debugging information
    print("Rendering flower.html template")
    print(f"Template folder: {os.path.join(app.root_path, 'templates')}")
    return render_template('flower.html')

@app.route('/apology')
def apology():
    # Print debugging information
    print("Rendering index.html template")
    print(f"Template folder: {os.path.join(app.root_path, 'templates')}")
    return render_template('index.html')

@app.route('/more', endpoint='more')
def flowers2():
    return render_template('flower2.html')

if __name__ == '__main__':
    app.run(debug=True)