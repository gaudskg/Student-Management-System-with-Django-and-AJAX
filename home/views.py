import imp
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    all_entries = Student.objects.all()
    # print(all_entries)
    # print("*************************")
    context = {'data': all_entries}
    return render(request,'index.html',context)

@csrf_exempt
def send_data(request):
    # id = request.POST['id']
    # print(id,"+****************************")
    
    
    if request.POST['stu_id'] != "":
        b = Student.objects.get(id = request.POST['stu_id'])
        b.name = request.POST['name']
        b.email = request.POST['email']
        b.branch = request.POST['branch']
        b.save()
    if request.POST['stu_id'] == "":
        email = request.POST['email']
        name = request.POST['name']
        branch = request.POST['branch']
        values = Student.objects.create(name=name,email=email,branch=branch)
        values.save()
        print(f"{name}*******{email}************{branch}")
    return JsonResponse({'status':200})


@csrf_exempt
def delete_data(request):
    student_id = request.POST['student_id']
    b = Student.objects.get(id = student_id)
    b.delete()
    return JsonResponse({'status':200})