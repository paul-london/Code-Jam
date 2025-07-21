from flask import Flask, request, jsonify
from scripts.map import plot_route_on_map  # import your function

app = Flask(__name__)

@app.route('/', methods=['POST'])
def create_map():
    data = request.get_json()
    home_state = data.get("state")

    # Call your existing function
    plot_route_on_map(home_state)

    # Return file path to React (for iframe)
    return jsonify({"url": f"../usa_roadtrip_map.html"})

if __name__ == '__main__':
    app.run(debug=True)
