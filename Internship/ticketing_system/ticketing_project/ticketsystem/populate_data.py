from ticketsystem.models import User, Ticket
import random

def create_sample_data():
    user_count = User.objects.count()
    
    for i in range(1, 11):
        unique_id = f'#{user_count + i}'
        name = f'User {i}'
        person = User.objects.create(unique_id=unique_id, name=name)
    
        issue_description = f'Ticket issue {i}'
        assigned_to = random.choice(User.objects.all())
        raised_by = random.choice(User.objects.all())

        ticket = Ticket.objects.create(
            unique_id=unique_id,
            issue_description=issue_description,
            assigned_to=assigned_to,
            raised_by=raised_by
        )
        print(f"Created User: {person} and Ticket: {ticket}")

create_sample_data()
