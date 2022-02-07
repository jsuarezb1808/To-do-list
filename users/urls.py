from django.urls import path,re_path

from . import views

app_name='users'

urlpatterns=[
    re_path('^register/$',views.register,name='register'),
    re_path('^login/$',views.login_view,name='login'),
    re_path('^logout/$',views.logout_view,name='logout'),
]
