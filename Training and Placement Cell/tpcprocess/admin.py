from django.contrib import admin
from .models import Student, Company, EligiCriteria, CandidateList

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(EligiCriteria)
admin.site.register(CandidateList)
