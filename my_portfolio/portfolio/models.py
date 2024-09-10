from django.db import models
from django.utils.timezone import now

class Skill(models.Model):
    name = models.SlugField(max_length=100, unique=True)  # Use SlugField for better string handling
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SideMenu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.description[:50]}..."  # Truncate description if it's too long for display purposes

class Certification(models.Model):
    title = models.CharField(max_length=200, unique=True)
    authority = models.CharField(max_length=100, blank=True, null=True)
    date_earned = models.DateField(blank=True, null=True, default=now)
    verification_url = models.URLField(max_length=200, blank=True, null=True)
    parent_certification = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child_certification_set')

    def __str__(self):
        return f"{self.title} {self.authority} {self.parent_certification}" if self.parent_certification else f"{self.title} {self.authority}"
