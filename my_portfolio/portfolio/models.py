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
    authority = models.CharField(max_length=100)
    date_earned = models.DateField()
    verification_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
