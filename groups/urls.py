from django.conf.urls import url
from groups.views import GroupsListView




urlpatterns = (
    url(r'^$', GroupsListView.as_view(), name='groups'),
)


