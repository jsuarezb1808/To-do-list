from django.urls import path,re_path

from . import views

#allows to specify specific tasks views by using[APP_NAME]:[PATH_NAME] on template
app_name='tasks'

urlpatterns=[
    path('',views.showtasks,name='home'),
    path('new/',views.newtask,name='create'),
    re_path('(?P<slug>[\w-]+)/$',views.taskDetail,name='detail'),
    re_path('(?P<slug>[\w-]+)/$',views.taskUpdate,name='update'),
    #r indicates a regular expresion
    #^ indicates that cannot exist something before the url
    #$ cannot exist something after the indicated url
    #(?P<[NAME]>) the name of what we are getting from the template and sending to the view
    #[\w-]+
        #\w means any character or number can be included
        #- middle lines can be included
        #+ any length can be used


]
