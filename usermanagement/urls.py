from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

from usermanagement import views

urlpatterns = [
    url(r'^succes/$', TemplateView.as_view(template_name="user/succes.html")),
    url(r'^create_account/$', views.create_account),
    url(r'^login/$', login, {'template_name':'user/login.html'}),
    url(r'^logout/$', logout, {'next_page': '/user/login/'}),
    url(r'^profile/$', login_required(TemplateView.as_view(template_name="user/profile.html"))),
]
