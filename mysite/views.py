from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def logoutauth(request):
    auth_logout(request)
    return Response(None,status=status.HTTP_200_OK)

@api_view(['POST'])
def loginauth(request):
    user_loggedin = 'Guest'
    displayName = "xiaozhu"
    errors_list = []
    context = {'username': user_loggedin, 'displayName': displayName, 'state': False}
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        usergo = authenticate(username=username, password=password)
        print('authuser', usergo)
        if usergo is not None:
            auth_login(request, usergo)
            uu = request.user
            user_loggedin = usergo.username
            displayName = usergo.first_name
            context = {'username': user_loggedin, 'displayName': displayName, 'state': True}
            return Response(context, status=status.HTTP_200_OK)
        return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
def checklogin(request):

    user_loggedin = 'xxiaozhu'
    displayName = "xiaozhu xiaozhu"
    context = {'username': user_loggedin, 'displayName': displayName, 'state': False}
    uu = request.user
    if uu:
        usergo = User.objects.filter(username=uu).first()
        if usergo is not None:
            user_loggedin = usergo.username
            displayName = usergo.first_name
            context = {'username': user_loggedin, 'displayName': displayName, 'state': True}
        return Response(context,status=status.HTTP_200_OK)
    return Response(context, status=status.HTTP_200_OK)

