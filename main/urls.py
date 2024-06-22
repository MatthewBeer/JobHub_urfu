from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('submit_company_registration/', views.submit_company_registration, name='submit_company_registration'),
    path('submit_student_registration/', views.submit_student_registration, name='submit_student_registration'),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)