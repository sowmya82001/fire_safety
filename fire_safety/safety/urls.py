from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('fire-incidents/', views.fire_incidents, name='fire_incidents'),
    path('emergency-response/', views.emergency_response, name='emergency_response'),
    path('fire-training/', views.fire_training, name='fire_training'),
    path('compliance-checks/', views.compliance_checks, name='compliance_checks'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forget-password/', views.forget_password_view, name='forget_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
]
