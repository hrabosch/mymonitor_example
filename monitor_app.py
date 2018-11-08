from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('monitor.html', info = os.uname())

if __name__ == '__main__':
    app.run()