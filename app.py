from flask import Flask, request, jsonify

# App initialization
app = Flask(__name__)

# Routes
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "Backend is running"})

@app.route('/submit-repo/', methods=['POST'])
def submit_repo():
    data = request.json
    if not data or 'github_link' not in data:
        return jsonify({"error": "GitHub link is required"}), 400

    github_link = data['github_link']

    # Basic validation for GitHub URL
    if not github_link.startswith("https://github.com/"):
        return jsonify({"error": "Invalid GitHub link"}), 400

    # Placeholder response
    return jsonify({"message": "Repository submitted successfully", "repo": github_link})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
