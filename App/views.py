from django.shortcuts import render, redirect
from App.models import contact, Drone
# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email = request.POST['email']
        data = contact(name=name,phone=phone,email=email)
        data.save()
    
    contexdata = contact.objects.all()
    contex = {'name' : contexdata}
    
    return render(request,'booking.html',contex) 

def readdata(request):
    ad = contact.objects.all()
    print (ad)
    context = {'bookings':ad}
    return render(request,'data.html', context)


def delete(request,id):
    delete = contact.objects.get(pk=id)
    delete=delete.delete()
    return redirect('read')

def update(request,id):
    per = contact.objects.get(pk=id)

    context = {
        'Bookings':per
    }
    return render(request,'update.html', context)

def save(request,id): 
    if request.method == 'POST':
        
        name=request.POST['name']
        phone=request.POST['phone']
        email = request.POST['email']
        data = contact(id=id,name=name,phone=phone,email=email)
        data.save()
        return redirect('read')
    
    




