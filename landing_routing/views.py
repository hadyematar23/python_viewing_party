from django.shortcuts import render
from students.models import Student

# Create your views here.
def home(request):
  students = Student.objects.all()
  return render(request, 'landing_routing/home.html', {"users": students})