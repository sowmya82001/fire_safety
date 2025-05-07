from django.contrib import admin
from .models import FireIncident, EmergencyResponse, FireTraining, ComplianceCheck

admin.site.register(FireIncident)
admin.site.register(EmergencyResponse)
admin.site.register(FireTraining)
admin.site.register(ComplianceCheck)
