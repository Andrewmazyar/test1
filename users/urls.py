from django.conf.urls import url
from users.views import UsersListView




urlpatterns = (
    url(r'^$', UsersListView.as_view(), name='users'),
)