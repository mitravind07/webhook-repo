from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__, template_folder='templates')
events = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'push':
        event = {
            'type': 'push',
            'repo': data['repository']['full_name'],
            'pusher': data['pusher']['name'],
            'time': datetime.datetime.now().isoformat()
        }
        if event not in events:
            events.append(event)
    elif event_type == 'pull_request' and data['action'] == 'closed' and data['pull_request']['merged']:
        event = {
            'type': 'merge',
            'repo': data['repository']['full_name'],
            'user': data['pull_request']['user']['login'],
            'time': datetime.datetime.now().isoformat()
        }
        if event not in events:
            events.append(event)
    return jsonify({"message": "Event received"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events[-10:])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
