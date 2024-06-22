"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from main.views import index, submit_student_registration, submit_company_registration, recomendation, page_not_found, style,show_post,recomendationcompanies, student_detail, innovatech,digitallabs,unit,itbox,addpage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('main.urls')),
    path('', index, name = 'home'),
    path('studentregistration/', submit_student_registration, name = 'student_registration'),
    path('companyregistration/', submit_company_registration, name = 'company_registration'),
    path('recomendation/', recomendation, name = 'recomendation'),
    path('recomendationcompanies/', recomendationcompanies, name = 'recomendationcompanies'),
    path('style/', style, name='style'),
    path('student/<int:pk>/', student_detail, name='student_detail'),
    path('innovatech/', innovatech, name = 'innovatech'),
    path('digitallabs/', digitallabs, name = 'digitallabs'),
    path('itbox/', itbox, name = 'itbox'),
    path('unit/', unit, name = 'unit'),
    path('addpage/', addpage, name = 'addpage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = page_not_found