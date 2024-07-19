from django.shortcuts import render
from .models import Skill, Project, Certification, SideMenu

def main_page(request):
    sidemenus = SideMenu.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'sidemenus': sidemenus,
        'skills': skills,
        'projects': projects,
        'certifications': certifications,
    }
    
    return render(request, 'main.html', context)
