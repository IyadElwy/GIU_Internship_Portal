from django.contrib import admin
from django.urls import path, include
from cvbuilder.views import CVExample

urlpatterns = [
    path('', include('portal.urls')),
    path('admin/', admin.site.urls),
    path('cvexample/', CVExample.as_view(), name='cvexample'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
