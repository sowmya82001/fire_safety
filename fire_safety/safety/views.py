from django.shortcuts import render, get_object_or_404
from .models import FireIncident, EmergencyResponse, FireTraining, ComplianceCheck

def home(request):
    return render(request, "safety/home.html")

def fire_incidents(request):
    incidents = FireIncident.objects.all()
    return render(request, "safety/fire_incidents.html", {"incidents": incidents})

def emergency_response(request):
    responses = EmergencyResponse.objects.all()
    return render(request, "safety/emergency_response.html", {"responses": responses})

def fire_training(request):
    trainings = FireTraining.objects.all()
    return render(request, "safety/fire_training.html", {"trainings": trainings})

def compliance_checks(request):
    checks = ComplianceCheck.objects.all()
    return render(request, "safety/compliance_checks.html", {"checks": checks})
