from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='demo.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='demo.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='demo.html'), name='contact'),
    path('services/', TemplateView.as_view(template_name='demo.html'), name='services'),
    path('services/web-development/', TemplateView.as_view(template_name='demo.html'), name='web_development'),
    path('services/mobile-apps/', TemplateView.as_view(template_name='demo.html'), name='mobile_apps'),
    path('products/', TemplateView.as_view(template_name='demo.html'), name='products'),
    path('blog/', TemplateView.as_view(template_name='demo.html'), name='blog'),
]