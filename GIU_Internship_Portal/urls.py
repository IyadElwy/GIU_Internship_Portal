from django.contrib import admin
from django.urls import path, include

import GIU_Internship_Portal.views
from cvbuilder.views import CVExample
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler403, handler400, handler500

urlpatterns = [
                  path('', include('portal.urls')),
                  path('news/', include('news.urls')),
                  path('admin/', admin.site.urls),
                  path('cvexample/', CVExample.as_view(), name='cvexample'),
                  path('users/', include('users.urls')),
                  path('users/', include('django.contrib.auth.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'GIU_Internship_Portal.views.custom_error_404'
handler403 = 'GIU_Internship_Portal.views.custom_error_403'
handler400 = 'GIU_Internship_Portal.views.custom_error_404'
