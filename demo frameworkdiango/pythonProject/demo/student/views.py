from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .models import student as student_model
def index(request):
    student_list = student_model.objects.all().order_by('id')
    return render(request,'student/index.html',{'student_list':student_list})
