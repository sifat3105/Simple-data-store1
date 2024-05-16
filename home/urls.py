from django.urls import path 
from .views import home_func, delete_data, update_data

urlpatterns = [
    path('', home_func ,name='home'),
    path('delete/<int:id>/',delete_data, name='delete_data'),
    path('update/<int:id>/',update_data, name='update_data')
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)