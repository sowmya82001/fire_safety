from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fire-incidents/', views.fire_incidents, name='fire_incidents'),
    path('emergency-response/', views.emergency_response, name='emergency_response'),
    path('fire-training/', views.fire_training, name='fire_training'),
    path('compliance-checks/', views.compliance_checks, name='compliance_checks'),
]
