# app.py (Flask app)

from flask import Flask, request, jsonify
import pandas as pd
from waste_collection_optimization import optimize_routes

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    optimized_routes = optimize_routes(data)
    return jsonify(optimized_routes)

if __name__ == '__main__':
    app.run(debug=True)
