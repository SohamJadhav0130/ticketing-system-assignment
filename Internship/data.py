# data.py

# Sample static data for users (people)
people = [
    {"id": "user1", "name": "User 1", "tickets_assigned": []},
    {"id": "user2", "name": "User 2", "tickets_assigned": []},
    {"id": "user3", "name": "User 3", "tickets_assigned": []},
    # Add more users here
]

# Sample static data for tickets
tickets = [
    {"id": "ticket1", "issue_description": "Network issue", "assigned_to": "user1", "raised_by": "user2"},
    {"id": "ticket2", "issue_description": "Server error", "assigned_to": "user2", "raised_by": "user3"},
    # Add more tickets here
]

def get_user_by_id(user_id):
    for user in people:
        if user['id'] == user_id:
            return user
    return None

def assign_ticket_to_user(ticket_id, user_id):
    ticket = get_ticket_by_id(ticket_id)
    if ticket:
        user = get_user_by_id(user_id)
        if user:
            ticket['assigned_to'] = user_id
            user['tickets_assigned'].append(ticket_id)
            return True
    return False

def get_ticket_by_id(ticket_id):
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            return ticket
    return None
