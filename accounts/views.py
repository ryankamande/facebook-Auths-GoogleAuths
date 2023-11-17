from django.shortcuts import render
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from accounts.serializer import RegistrationSerializer, UsersSerializer


# Create your views here.
class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                r = request.post('http://127.0.0.1:8000/api-auth/token/', data={
                    'username': new_user.email,
                    'password': request.data['password'],
                    'client_id': '8d51SEDXRMvyQ1CdV2XmCahgpPwhsL8kNTQ5gUL3',
                    'client_secret': 'BCkbh3Et1ZXO8VP9snGghJhfPLmVqbPygW0frFrEfJum1Eu7MAhnnYbuwUVjPV8lxeSeP80XmNncQGYGv6ZKjMbyP4peNIL2ljBPp8Fk9HmTxxG6CZ7xVLy3p29rZZ2o',
                    'grant_type': 'password'
                })
                return Response(r.json(), status=status.HTTP_201_CREATED)
            return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUsers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()
    serializer_class = UsersSerializer


class CurrentUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        return Response(serializer.data)
