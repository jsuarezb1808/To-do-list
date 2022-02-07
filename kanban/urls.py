from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #created apps urls
    path('',include('tasks.urls')),
    path('users/',include('users.urls'))
]
