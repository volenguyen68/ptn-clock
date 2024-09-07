# app.py

from flask import Flask, render_template
from seok_ryu_clock import get_time

app = Flask(__name__)

@app.route('/')
def index():
    current_time = get_time()  # Lấy thời gian từ file seok_ryu_clock.py
    return render_template('index.html', time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
