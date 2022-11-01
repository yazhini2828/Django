from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
     }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x1 = request.POST['first name:']
  x2 = request.POST['last name:']
  x3 = request.POST['Age:']
  x4 = request.POST['Email ID:']
  x5 = request.POST['Mobile Number:']
  x6 = request.POST['Location:']
  x7 = request.POST['Total Marks Scored:']
  x8 = request.POST['Preferred Course:'] 
  member = Members(firstname=x1, lastname=x2, age=x3, email_id=x4, mobile_no=x5, location=x6, total_marks_scored=x7, Preferred_course=x8)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def search_results(request): 
  template = loader.get_template('search_results.html')
  return HttpResponse(template.render({}, request))
