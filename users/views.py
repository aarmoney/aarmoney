from django.shortcuts import render
from django.contrib.auth import get_user_model

def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'users/user_list.html', {'users': users})
