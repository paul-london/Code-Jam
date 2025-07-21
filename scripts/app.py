import os
from flask import Flask, request, jsonify, send_from_directory
from scripts.map import plot_route_on_map

app = Flask(__name__, static_folder='dist', static_url_path='')

# Serve React frontend
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# API endpoint for dropdown selection (POST)
@app.route('/api/map', methods=['POST'])
def create_map():
    data = request.get_json()
    home_state = data.get("state")
    plot_route_on_map(home_state)
    # Return URL of generated map file
    return jsonify({"url": "/maps/usa_roadtrip_map.html"})

# Serve generated map files (GET)
@app.route('/maps/<path:filename>')
def serve_maps(filename):
    # Adjust the path as needed; '../maps' means folder parallel to your Flask app folder
    return send_from_directory('../maps', filename)

if __name__ == '__main__':
    app.run(debug=True)
