
# Import the Flask package.
from flask import Flask, jsonify
# Import the requests package.
import requests
from flask_cors import CORS

# Create the Flask app.
app = Flask(__name__)
CORS(app)

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

# Run the Flask app.
if __name__ == '__main__':
    app.run()
