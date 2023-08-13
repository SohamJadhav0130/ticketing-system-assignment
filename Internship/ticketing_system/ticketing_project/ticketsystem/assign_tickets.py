import os
import django
import random

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticketing_project.settings')

# Initialize Django
django.setup()
from ticketsystem.models import User, Ticket,AssignedTicket

# Retrieve all users from the database
users = User.objects.all()

if not users:
    print("No users found in the database.")
else:
    # Retrieve the index of the last assigned user
    last_assigned_user = User.objects.filter(assigned_tickets_count__gt=0).last()
    last_assigned_index = last_assigned_user.id - 1 if last_assigned_user else 0

    # Calculate the next user index based on Round Robin
    next_user_index = (last_assigned_index + 1) % len(users)
    assigned_user = users[next_user_index]

    # Select a random user who is not the assigned user
    other_users = [user for user in users if user != assigned_user]
    raised_by_user = random.choice(other_users)

    # Generate a unique ID for the new ticket
    existing_ticket_count = Ticket.objects.count()
    unique_id = f"#{existing_ticket_count + 1}"

    # Create a new ticket in the database
    new_ticket = Ticket.objects.create(
        unique_id=unique_id,
        issue_description="Sample issue description",
        assigned_to=assigned_user,
        raised_by=raised_by_user
    )

    # Update the assigned user's assigned ticket count and list of assigned tickets
    assigned_user.assigned_tickets_count += 1
    assigned_user.assigned_tickets.add(new_ticket)
    assigned_user.save()
    
    # Assuming you have assigned_user and new_ticket objects
    AssignedTicket.objects.create(user=assigned_user, ticket=new_ticket)

    print(f"Ticket {new_ticket.unique_id} assigned to User {assigned_user.unique_id}")
