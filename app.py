import csv
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        with open('static/addresses.csv', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['State'] in request.form['location'] or row['Code'] in request.form['location']:
                    return render_template('result.html', governor=row)
