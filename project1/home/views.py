from django.shortcuts import render,HttpResponse,redirect
from home.models import Table

# Create your views here.
def home (request):
    
    if request.method == "POST":
        
        name=request.POST.get("name")
        
        phone=request.POST.get("phone")
       
        email=request.POST.get('email')
     
        subject=request.POST.get('subject')
        
        message=request.POST.get('message')
        
        
        contact=Table(name=name,phone=phone,email=email,subject=subject,message=message)
        contact.save()
        
        print("Saved!")
        
        
    data = Table.objects.all().values()
    return render(request, 'index.html', {'data': data})
    


    