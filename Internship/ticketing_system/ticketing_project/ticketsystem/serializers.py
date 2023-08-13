from rest_framework import serializers #type:ignore
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['unique_id', 'issue_description', 'assigned_to', 'raised_by']
