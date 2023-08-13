# ticketing/views.py

from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework import status #type:ignore
from .models import User, Ticket
from itertools import cycle
from .serializers import TicketSerializer

class CreateTicketView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        issue = request.data.get('issue')

        if not user_id or not issue:
            return Response({
                "message": "Both 'user_id' and 'issue' are required fields.",
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(unique_id=user_id)
        except User.DoesNotExist:
            return Response({
                "message": f"User with ID '{user_id}' does not exist.",
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)

        assigned_users = User.objects.filter(assigned_tickets__isnull=False)
        if not assigned_users:
            return Response({
                "message": "No users available for ticket assignment.",
                "success": False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user_cycle = cycle(assigned_users)
        assigned_user = next(user_cycle)
        new_ticket = Ticket.objects.create(issue_description=issue, assigned_to=assigned_user, raised_by=user)

        serializer = TicketSerializer(new_ticket)
        assigned_user.refresh_from_db()

        response_data = {
            "ticket_id": new_ticket.unique_id,
            "assigned_to": assigned_user.unique_id
        }

        return Response({
            "message": "Ticket successfully created.",
            "success": True,
            "data": response_data
        }, status=status.HTTP_201_CREATED)
