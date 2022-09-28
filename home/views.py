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
    if request.POST['stu_id'] != "":
        stu_id = request.POST['stu_id']
        b = Student.objects.get(id = stu_id)
        name = request.POST['name']
        branch = request.POST['name']
        email = request.POST['name']
        b.name = name
        b.email = email
        b.branch = branch
        b.save()
        data = {'name':name, 'email':email, 'branch':branch, 'id':stu_id}
        return JsonResponse(data)
    if request.POST['stu_id'] == "":
        email = request.POST['email']
        name = request.POST['name']
        branch = request.POST['branch']
        values = Student.objects.create(name=name,email=email,branch=branch)
        values.save()
        print(f"{name}*******{email}************{branch}")
        new_data = Student.objects.get(email=email)
        stu_id = new_data.id
        data = {'name':name, 'email':email, 'branch':branch, 'id':stu_id}
        return JsonResponse(data)


@csrf_exempt
def delete_data(request):
    student_id = request.POST['student_id']
    b = Student.objects.get(id = student_id)
    b.delete()
    return JsonResponse({'status':200})