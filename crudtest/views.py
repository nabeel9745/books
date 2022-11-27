from contextlib import redirect_stdout
from urllib import request
from django.shortcuts import render,redirect
from sellers.models import contacts


# Create your views here.

from .models import *
# from artist_app.models import Artist

     
def form(request):
     hoi=''
     if request.method == 'POST':
          form_name = request.POST['name']
          form_email = request.POST['email']
          form_password = request.POST['password']
          form_phn = request.POST['phn']
          form_address = request.POST['address']
          big_form(name=form_name,email=form_email,password=form_password,phn=form_phn,address=form_address).save()
          hoi = 'form have submitted the admin must approve to signin'
     return render(request,'crudpages/crudform.html',{'msg':hoi})
  
def c_show(request):
     v = big_form.objects.all()
     return render(request,'crudpages/crudshow.html',{'viewform':v})

def dele(request,id):
     d = big_form.objects.get(id=id).delete()
     return redirect ('crudshow')

def upd(request,id):
     u = big_form.objects.get(id=id)
     return render(request,'crudpages/crudupdation.html',{'toupd':u})

def editing(request,id):
     if request.method == 'POST':
          u_name = request.POST['e_name']
          u_email = request.POST['e_email']
          u_psd = request.POST['e_password']
          u_phn = request.POST['e_phn'] 
          u_address = request.POST['e_address']
          big_form.objects.filter(id=id).update(name=u_name,email=u_email,password=u_psd,phn=u_phn,address=u_address)
          return redirect('crudshow')
     
def log(req):
     error=""
     error1=""
     if req.method == 'POST':
          eml = req.POST['eml']
          psd = req.POST['psd']
          try :
               lg_val = big_form.objects.get(email=eml,password=psd)
               approve = lg_val.approved
               if approve == 'approved':
                    req.session['login_session']=lg_val.id
                    return redirect('a')
               else:
                    error="admin should approve"
                    return render (req,'crudpages/log.html',{'error1':error})
          except:
               error1="invalid email id or password"
     return render(req,'crudpages/log.html',{'error':error1})


def a(request):
    u=request.session['login_session']
    prof_details=big_form.objects.get(id=u)
    return render (request,'crudpages/abcd.html',{'prof':prof_details})

def logout(req):
     del req.session['login session']
     return redirect('log')

def accepted(request,id):  
     b = request.session['login_session']
     k = big_form.objects.get(id=b)
     return render(request,'crudpages/accepted.html',{'acc':k})

# def accepted(request,id):  
#      lg = big_form.objects.get(id=id)
#      approve = lg.approved
#      if approve == 'approved':
#           return render(request,'crudpages/accepted.html',{'acc':lg})
#      else:
#           return render(request,'crudpages/accepted.html')

def reply(req):
     messages_are = contacts.objects.all()
     return render(req,'crudpages/replay.html',{'v':messages_are})

def real_replay(req):
     if req.method == 'POST':
          re = req.POST['reply']
          store = contacts.objects.get(replay=re).save()
     return render(req,'crudpages/replay.html')





 



    
     



