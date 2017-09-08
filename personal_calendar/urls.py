from django.conf.urls import url

from personal_calendar import views

urlpatterns = [
    url(r'^create/$', views.create),
    url(r'^(\d+)/details/$', views.details),
    url(r'^liste/$', views.liste),
    url(r'^(\d+)/delete/$', views.delete),
    url(r'^(\d+)/participant/(\d+)/delete/$', views.delete_participant),
    url(r'^(\d+)/update/$', views.update),
]
