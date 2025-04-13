from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
def flowers():
    # Print debugging information
    print("Rendering flower.html template")
    print(f"Template folder: {os.path.join(app.root_path, 'templates')}")
    return render_template('flower.html')

if __name__ == '__main__':
    app.run(debug=True)