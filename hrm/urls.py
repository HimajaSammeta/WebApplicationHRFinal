"""
URL configuration for hrm project.

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
from django.contrib import admin
from django.urls import path, include
from HRadministrator import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inital_page, name='inital_page'),
    path('cand-login', views.login_user, name='login-user'),
    path('admin-login', views.admin_login, name='admin-login'),
    path('signup', views.signup_user, name='signup-user'),
    path('HRadministrator/', include('HRadministrator.urls')),
    path('candidate/', include('candidate.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
