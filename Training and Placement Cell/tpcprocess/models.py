from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User, default=1)
    u_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=100)
    live_kt = models.IntegerField()
    dead_kt = models.IntegerField()
    profile = models.TextField(max_length=4000)
    passing_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    user = models.ForeignKey(User, default=1)
    c_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class EligiCriteria(models.Model):
    company = models.ForeignKey(Company, default=1)
    description = models.TextField(max_length=2000, null=True)
    tech_skills = models.TextField(max_length=2000, null=True)
    min_cgpa = models.CharField(max_length=100, null=True)
    live_kt_allowed = models.BooleanField(default=True)
    backlog_allowed = models.BooleanField(default=True)

    def __str__(self):
        return str(self.company) + ' Eligibility Criteria'


class CandidateList(models.Model):
    company = models.ForeignKey(Company, default=1)
    student = models.ForeignKey(Student, default=1)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.company) + ' - ' + str(self.student)
