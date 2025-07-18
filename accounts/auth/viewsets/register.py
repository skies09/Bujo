from rest_framework import viewsets, status
from rest_framework.response import Response
from accounts.auth.serializers import RegisterSerializer

class RegisterViewSet(viewsets.ViewSet):
    def create(self, request):
        print("Request data:", request.data)  # logs input data
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors)  # logs errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

