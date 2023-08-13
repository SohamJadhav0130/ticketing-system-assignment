from django.db import models

# Create your models here.
# ticketing/models.py

from django.db import models

class User(models.Model):
    unique_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    assigned_tickets_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"User {self.unique_id}: {self.name}"

class Ticket(models.Model):
    unique_id = models.CharField(max_length=10, unique=True)
    issue_description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets')
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='raised_tickets')

    def __str__(self):
        return f"Ticket {self.unique_id}: {self.issue_description}"

class AssignedTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)