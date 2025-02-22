from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    print("Home route accessed")
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True, host='127.0.0.1', port=5000)
