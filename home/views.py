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
    if request.method == "POST":
        email = request.POST['name']
        name = request.POST['name']
        branch = request.POST['branch']
        print(f"{name}*******{email}************{branch}")
        return JsonResponse({'status':200})