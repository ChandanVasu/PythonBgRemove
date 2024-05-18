from flask import Flask, jsonify, make_response ,Response, request
import requests
from rembg import remove
import json

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')

@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')

@app.route('/remove_background', methods=['GET'])
def remove_background():
    url = request.args.get('url')
    
    if not url:
        return Response(json.dumps({'error': 'Missing URL parameter'}), status=400, mimetype='application/json')

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')
    
    input_data = response.content

    try:
        output_data = remove(input_data)
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), status=500, mimetype='application/json')

    return Response(output_data, status=200, mimetype='image/png')

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(debug=True)
