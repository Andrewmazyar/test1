# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from users.models import User

from django.views.generic import TemplateView

# Create your views here.
class UsersListView(ListView):
    model = User
    template_name = 'users_page.html'
    context_object_name = 'users_list'
    queryset = User.objects.select_related('groups').all()


class MainPageView(TemplateView):
    template_name = 'base.html'