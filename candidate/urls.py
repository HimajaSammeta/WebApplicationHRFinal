from django.urls import path
from candidate import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homepage/', views.candidate_home, name='homepage'),
    path('dashboard/', views.candidate_dashboard, name='dashboard'),
    path('profile', views.candidate_profile, name='profile'),
    path('openpositions', views.candidate_openpositions, name='openpositions'),
    path('requisition', views.candidate_requisition, name='requisition'),
    path('cfeedback', views.candidate_cfeedback, name='cfeedback'),
    path('feedbackDB', views.candidate_feedbackDB, name='feedbackDB'),
    path('changepassword', views.candidate_changepassword, name='changepassword'),
    path('changepasswordDB', views.candidate_changepasswordDB, name='changepasswordDB'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
