from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('url', views.current_url_view_good),
    path('agent', views.ua_display_good),
    path('meta', views.display_meta),
    path('search', views.search),
   ]