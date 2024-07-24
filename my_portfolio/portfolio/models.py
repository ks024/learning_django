from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SideMenu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Certification(models.Model):
    title = models.CharField(max_length=200)
    authority = models.CharField(max_length=100, blank=True, null=True)
    date_earned = models.DateField(blank=True, null=True)
    verification_url = models.URLField(max_length=200, blank=True, null=True)
    parent_certification = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child_certification_set')

    def __str__(self):
        return self.title
