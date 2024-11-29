from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the Excel data
data = pd.read_excel('data/consolidated_data_final.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        # Search for exact and approximate matches
        matches = data[data.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
    else:
        matches = pd.DataFrame()

    return jsonify(matches.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
