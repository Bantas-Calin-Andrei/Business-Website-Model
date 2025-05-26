from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from contact import views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contact_view, name='home'),
    path('blog/', blog_views.blog_view, name='blog'),
    path('blog-admin/', blog_views.blog_admin_view, name='blog-admin'),
]
