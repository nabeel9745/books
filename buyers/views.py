from random import random
from django.core.files.storage import FileSystemStorage
from statistics import quantiles
from django.shortcuts import render,redirect
from .decrators import auth_user
# Create your views here.

from .models import *

def reg(request):
    if request.method =='POST':
        a= int(request.POST["first"])
        b= int(request.POST["second"])
        c=a*b
        return render(request,'pages/reg.html',{'result':c})

    return render(request,'pages/reg.html')

def seller(request):
    if request.method == 'POST':
        name=request.POST['s_name']
        email=request.POST['s_email']
        password=request.POST['s_password']
        phn=request.POST['s_phn']
        address=request.POST['s_address']
        sellers(name=name,email=email,password=password,phn=phn,address=address).save()
    return render(request,'pages/seller.html')
  
@auth_user
def show(request):
    x = sellers.objects.all()
    return render(request,'pages/show.html',{'show':x})

def login(request):
    if request.method == 'POST':
        name = request.POST['s_name']
        password = request.POST['s_password']
        try :
            x = sellers.objects.get(name = name,password = password)
            request.session['mysession']=x.id
            return redirect('show')
        except sellers.DoesNotExist:
             return render(request,'pages/loginpg.html',{'message':'wrong input'})
    return render(request,'pages/loginpg.html')

def logout(request):
    del request.session['mysession']
    return redirect('login')

def product(request):
     z = request.session['mysession']
     if request.method == 'POST':
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['des']
        image=request.FILES['img']
        a =str(random())+image.name
        b = FileSystemStorage()
        b.save(a,image)
        products(name=name,price=price,description=description,image=a,seeler_id_id=z).save()

     return render(request,'pages/product.html')

def p_show(request):
    q = products.objects.all()
    return render(request,'pages/product_show.html',{'display':q})


# def show2(request):
#     x = products.objects.all()
#     return render(request,'pages/show2.html',{'show':x})

# def show2(request):
#     x = products.objects.all()
#     return render(request,'pages/show2.html',{'show':x})

# def show3(request):
#     x = products.objects.all()
#     return render(request,'pages/show3.html',{'show':x})

# def delete(request,id):
#     products.objects.get(id=id).delete()
#     return redirect('show2')

# def update(request,id):
#     x = products.objects.get(id=id)
#     return render(request,'pages/updating.html',{'update_list':x})  

# def editing(request,id):
#     if request.method == 'post':
#         name=request.post['proname']
#         price=request.post['pro_price']
#         type=request.post['pro_type']
#         quantity=request.post['pro_quantity']
#         products.objects.filter(id=id).update(name=name,price=price,type=type,quantity=quantity)

#         return redirect('show3')

# def login(request):
#        if request.method == 'POST':
#         user = request.POST['proname']
#         password = request.POST['password']
#         try :
#             z = registration.objects.get(email = user,password = password)
            # request.session['mysession'] = z.id
#             return redirect('retrive')
#         except registration.DoesNotExist:
#              return render(request,'common/loginpg.html',{'message':'wrong input'})
#     return render(request,'common/loginpg.html')

# def logout(request):
#     # request.session.delete('mysession')
#     del request.session['mysession']
#     return redirect('login')



