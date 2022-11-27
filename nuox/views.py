from django.shortcuts import render,redirect
from nuox.models import nuox_sign
from nuox.models import staff
from nuox.models import items


# Create your views here.

def login(req):
    if req.method == 'POST':
        email = req.POST['email']
        phn = req.POST['phn']
        psd = req.POST['psd']
        nuox_sign(email=email,phone=phn,password=psd).save()
    return render(req,'pages\login.html')

def sign(req):
    if req.method =='POST':
        user = req.POST['user']
        psd = req.POST['psd']
        try:
            if '@' in user:
                x=nuox_sign.objects.get(email=user,password=psd)
                req.session['mysession']=x.id
                return redirect('welcome')
            else:
                x=nuox_sign.objects.get(phone=user,password=psd)
                req.session['mysession']=x.id
                return redirect('welcome') 
        except nuox_sign.DoesNotExist:
            return render(req,'pages\sigin.html',{'message':"wrong username"})
    return render(req,'pages\sigin.html')

def welcome(req):
    return render(req,'pages\welcome.html')    
    
def staffs(req):
    if req.method == 'POST':
        f_name = req.POST['f_name']
        l_name = req.POST['l_name']
        email = req.POST['email']
        phn = req.POST['phn']
        psd = req.POST['psd']
        staff(f_name=f_name,l_name=l_name,email=email,phone=phn,password=psd).save()
    return render(req,'pages\staff.html',{"your data have been submitted":"msg"})

def show_staff(req):
    show = staff.objects.all()
    return render(req,'pages\show_staff.html',{'view':show})

def edit_staff(req,id):
    x = staff.objects.get(id=id)
    return render(req,'pages\edit_staff.html',{'v':x})

def update_staff(req,id):
    if req.method == 'POST':
        f = req.POST['f_name']
        l = req.POST['l_name']
        eml = req.POST['email']
        phn = req.POST['phn']
        psd = req.POST['psd']
        staff.objects.filter(id=id).update(f_name=f,l_name=l,email=eml,phone=phn,password=psd)
        return redirect('show_staff')

def delete_staff(req,id):
    staff.objects.get(id=id).delete()
    return redirect('show_staff')

def logout(req):
    req.session.delete('mysession')
    del req.session['mysession']
    return redirect('sign')

def item(req):
    # if req.method == 'POST':
    #     p_name = req.POST['p_name']
    #     rate = req.POST['rate']
    #     des = req.POST['description']
    #     items(product_name=p_name,rate=rate,description=des).save()


    return render(req,'pages\items.html')




   

