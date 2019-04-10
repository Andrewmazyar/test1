# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from groups.models import Group

# Create your views here.
class GroupsListView(ListView):
    model = Group
    template_name = 'groups_page.html'
    context_object_name = 'groups_list'


