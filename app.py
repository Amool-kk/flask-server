
# Import the Flask package.
from flask import Flask, jsonify, request, send_file
# Import the requests package.
import requests
import csv
from datetime import datetime, timedelta
from flask_cors import CORS
import os

# Create the Flask app.
app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# Add a route for the /data endpoint.
@app.route('/data', methods=['GET'])
def get_data():
    # Get data from the Dune API.
    dune_data = get_dune_data()
    # Return the data as JSON.
    if dune_data:
        return jsonify(dune_data)
    else:
        return jsonify({'error': 'No data was received.'})

def get_dune_data():
    # Get data from the Dune API.
    response = requests.get('https://api.dune.com/api/v1/query/2666003/results?api_key=nwYKzCgdVxidaMIWbJcHu00FvJEsvQPA')
    # Get the response as JSON.
    if response.status_code != 200:
        # There was an error.
        print('Error: Did not receive data from API.')
        return False
    else:
        return response.json()
    
    
# Define function to export market data
def export_ethereum_market_data(start_date=None, num_days=365):
    if start_date is None:
        start_date = datetime.now() - timedelta(days=num_days)
    end_date = start_date + timedelta(days=num_days)

    url = f"https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=usd&from={int(start_date.timestamp())}&to={int(end_date.timestamp())}"
    print(url)
    response = requests.get(url)
    data = response.json()
    

    headers = ['Date', 'Price', 'Total Volume', 'Market Cap']
    rows = []

    for index, (price, volume, market_cap) in enumerate(zip(data['prices'], data['total_volumes'], data['market_caps'])):
        date = (start_date + timedelta(days=index)).strftime('%Y-%m-%d')
        row = [date, price, volume, market_cap]
        rows.append(row)
        
        
    # Create the folder if it doesn't exist
    folder_path = 'data'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"ethereum_market_data_{start_date.strftime('%Y%m%d')}_to_{end_date.strftime('%Y%m%d')}.csv"
    file_path = os.path.join(folder_path, filename)
    print(filename, file_path)
    
    with open(file_path, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(rows)
        
    return file_path

@app.route('/export-ethereum-data', methods=['GET'])
def export_ethereum_data():
    start_date_str = request.args.get('start_date')
    num_days = request.args.get('num_days')

    if not num_days:
        return 'num_days is a required parameter', 400

    try:
        num_days = int(num_days)
    except ValueError:
        return 'Invalid num_days, please use an integer', 400

    if num_days < 1:
        return 'num_days must be greater than 0', 400

    if start_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        except ValueError:
            return 'Invalid start date, please use YYYY-MM-DD format', 400
    else:
        start_date = None

    try:
        filename = export_ethereum_market_data(start_date=start_date, num_days=num_days)
        message = f"CSV file successfully exported."
        response = {
        'message': message,
        'file_path': filename
        }

        return jsonify(response)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()

    
    

# Run the Flask app.
if __name__ == '__main__':
    app.run()
