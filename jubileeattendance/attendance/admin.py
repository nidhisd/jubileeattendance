from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Participant, Attendance
admin.site.register(Participant)
admin.site.register(Attendance)


class ParticipantResource(resources.ModelResource):
    class Meta:
        model = Participant

class ParticipantAdmin(ImportExportModelAdmin):
    resource_class = ParticipantResource
