from flask import Flask, request, jsonify

app = Flask(__name__)

ban_requests = []

@app.route('/kickban', methods=['POST'])
def kickban():
    data = request.json
    
    if "userId" not in data or "action" not in data or "reason" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    ban_requests.append({
        "userId": data['userId'],
        "action": data['action'],
        "reason": data['reason']
    })
    
    return jsonify({"status": "Request received"}), 200

@app.route('/kickban', methods=['GET'])
def get_kickban_requests():
    if ban_requests:
        return jsonify(ban_requests.pop(0))
    else:
        return jsonify({"status": "No pending requests"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
