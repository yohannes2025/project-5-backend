# drf_api/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productivity_app.urls')),
    path('api/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # catch-all for frontend
    path('', TemplateView.as_view(template_name='index.html')),
]
