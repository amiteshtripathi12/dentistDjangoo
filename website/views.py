from django.shortcuts import render
from .models import formgroup
#from .models import Pigga
from .models import service
from django.contrib import messages
from .models import WorkingTime
from .models import Menu
from .models import Chefs
from .models import Testmonials

def home(request):
    Service = service.objects.all()
    workingtime = WorkingTime.objects.all()
    menu = Menu.objects.all()
    chefs = Chefs.objects.all()
    test = Testmonials.objects.all()
    context = {'WorkingTime':workingtime,'service':Service,'Menu':menu,'Chefs':chefs,'Testmonials':test}

    return render(request,'home.html',context) 


def components(request):
    Service = service.objects.all()
    return render(request,'components.html',{'service':Service})


def location(request):
    return render(request,'location.html',{})

def table(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone= request.POST['phone']
        date = request.POST['date']
        seats = request.POST['seats']

        form = formgroup(name=name,phone=phone,date=date,seats=seats)
        form.save()
        messages.info(request, " Your id has been successfully created")
        return render(request,'home.html',{})
    else:
        return render(request,'home.html')