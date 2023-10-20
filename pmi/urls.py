from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('data/', views.data, name='data')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)