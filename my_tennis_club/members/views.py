from django.shortcuts import render
from django.template import loader
from .models import Member

def members(request):
    members = Member.objects.all()
    return render(request, 'allmembers.html', {'mymembers': members})

def details(request, id):
    mymember = Member.objects.get(id=id)
    return render(request, 'details.html', {'mymember': mymember})

def main(request):
    return render(request, 'main.html')

def testing(request):
  members = Member.objects.all()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'], 
    'members': members,  
  }
  return render(request, 'template.html', context)