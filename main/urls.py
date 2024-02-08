from app import views
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
