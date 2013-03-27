from django.shortcuts import redirect

from . import client


def login(request):
    return redirect(client.authorize_url)


def callback(request):
    code = request.GET['code']
    token = client.client.auth_code.get_token(code, redirect_uri='/')
    token.headers['Authorization']
    return redirect('home')
