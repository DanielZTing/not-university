import csv
from flask import Flask, render_template, request
app = Flask(__name__)

search = ""

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        global search
        search = request.form['locationInput']
        with open('static/addresses.csv', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['State'] in request.form['locationInput'] or row['Code'] in request.form['locationInput']:
                    return render_template('result.html', governor=row)

@app.route('/google')
def google():
    return render_template('google.html', search=search);
