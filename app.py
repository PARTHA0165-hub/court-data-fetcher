from flask import Flask, render_template, request
from scraper import fetch_case_details
from db import init_db, log_query

app = Flask(__name__)

# Initialize DB
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        result = fetch_case_details(case_type, case_number, filing_year)

        # Save to DB
        log_query(case_type, case_number, filing_year, result['raw'])

        return render_template('result.html', data=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
