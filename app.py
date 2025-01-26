from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/echo', methods=['POST'])
def echo():
    # Check if the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400
    
    # Parse the JSON data from the request
    data = request.get_json()
    
    # Prepare the response
    response = {
        "message": "Data received successfully",
        "received_data": data
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
