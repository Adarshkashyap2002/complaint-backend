from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def create_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "username and password required"})

    if User.objects.filter(username=username).exists():
        return Response({"error": "user already exists"})

    User.objects.create_user(username=username, password=password)

    return Response({"message": "user created"})