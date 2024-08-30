from flask import Flask, request, jsonify

app = Flask(__name__)

commands_queue = []

@app.route('/kickban', methods=['POST'])
def kickban():
    data = request.get_json()

    user_id = data.get('userId')
    action = data.get('action')
    reason = data.get('reason', '')

    if not user_id or not action:
        return jsonify({'error': 'Invalid data'}), 400

    commands_queue.append(data)

    return jsonify({'message': f'{action.capitalize()} action received for user {user_id}'}), 200

@app.route('/kickban', methods=['GET'])
def process_command():
    if commands_queue:
        command = commands_queue.pop(0)
        return jsonify(command), 200
    else:
        return jsonify({'message': 'No commands to process'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
