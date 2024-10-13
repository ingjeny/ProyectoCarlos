from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from analysis import analyze_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/informe')
def informe():
    analysis_result = analyze_data()
    return render_template('informe.html', resultado=analysis_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

