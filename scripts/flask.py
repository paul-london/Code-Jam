from flask import Flask, request, jsonify
from map import plot_route_on_map  # import your function

app = Flask(__name__)

@app.route('/api/map', methods=['POST'])
def create_map():
    data = request.get_json()
    home_state = data.get("state")

    # Call your existing function
    plot_route_on_map(home_state)

    # Option 1: Return file path to React (for iframe)
    return jsonify({"url": f"/maps/map.html"})

    # Option 2: Return full HTML string
    # with open("map.html", "r") as f:
    #     return f.read()

if __name__ == '__main__':
    app.run(debug=True)
