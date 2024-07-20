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

def sidemenu_page(request):
    sidemenus = SideMenu.objects.all()
    
    context = {
        'sidemenus': sidemenus,
    }
    
    return render(request, 'sidemenu.html', context)

def skill_page(request):
    skills = Skill.objects.all()
    
    context = {
        'skills': skills,
    }
    
    return render(request, 'skill.html', context)

def project_page(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    
    return render(request, 'project.html', context)

def certification_page(request):
    certifications = Certification.objects.all()
    
    context = {
        'certifications': certifications,
    }
    
    return render(request, 'certification.html', context)
