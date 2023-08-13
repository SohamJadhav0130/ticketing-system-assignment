from flask import Flask  #type:ignore
from flask import Flask, request, jsonify
from data import people, tickets


app = Flask(__name__)

@app.route('/people', methods=['GET'])
def get_people():
    return jsonify(people)

@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)


@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    if not data or 'issue_description' not in data or 'raised_by' not in data:
        return jsonify({'error': 'Incomplete data'}), 400
    
    # Check if the raised_by user exists
    raised_by = data['raised_by']
    if not any(user['id'] == raised_by for user in people):
        return jsonify({'error': 'Raised by user not found'}), 404
    
    # Assign the ticket using Round Robin
    assigned_to = people[len(tickets) % len(people)]['id']
    
    new_ticket = {
        'id': len(tickets) + 1,
        'issue_description': data['issue_description'],
        'assigned_to': assigned_to,
        'raised_by': data['raised_by']
    }
    
    tickets.append(new_ticket)
    return jsonify(new_ticket), 201

