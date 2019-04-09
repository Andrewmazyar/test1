# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from users.models import User

# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = 'users/users_page.html'
    context_object_name = 'users_list'