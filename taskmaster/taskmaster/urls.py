from django.contrib import admin
from django.urls import path, include
from tasks.views import homepage
from django.contrib.auth import views as auth_views
from tasks.views import register_view
from tasks.views import custom_logout_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('tasks/', include('tasks.urls')),
    path('accounts/logout/', custom_logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register_view, name='register'),  
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
