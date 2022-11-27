from urllib import request
from xml.dom.expatbuilder import Rejecter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .models import*
from crudtest.models import big_form




# Create your views here.

def ajax(request):
     return render(request,'htmlpages/ajax.html')
@csrf_exempt
def aj(request):
    x = request.POST['a']
    x2 = request.POST['b']
    x3 = request.POST['c']
    x4 = request.POST['d']
    x5 = request.POST['e']
    registration(name=x,email=x2,password=x3,phn=x4,address=x5).save()
    return JsonResponse({'message':'value'})

def show(request):
    x = registration.objects.all()
    z = [{'id':i.id,'name':i.name,'email':i.email,'password':i.password,'phn':i.phn,'address':i.address}for i in x]
    return JsonResponse({'display':z})
@csrf_exempt   
def dele(request):
     a = request.POST['show_key']
     registration.objects.get(id=a).delete()
     return JsonResponse({'message':'value'})
@csrf_exempt   
def upd(request):
     w = request.POST['updating_key']
     y = registration.objects.get(id=w)
     lists = [{'id':y.id,'name':y.name,'email':y.email,'password':y.password,'phn':y.phn,'address':y.address}]
     return JsonResponse({'disp':lists})
@csrf_exempt   
def submit(request):
     u_key = request.POST['key']
     u_one = request.POST['one']
     u_two = request.POST['two']
     u_three = request.POST['three']
     u_four = request.POST['four']
     u_five = request.POST['five']
     print(u_one)
     registration.objects.filter (id=u_key).update(name=u_one,email=u_two,password=u_three,address=u_five)
     return JsonResponse({'disp':'updated successfully'})
# ////

def input_camel(request):
     return render(request,'htmlpages/camelinput.html')
@csrf_exempt
def camelwrk(request):
    x1 = request.POST['var1']
    x2 = request.POST['var2']
    x3 = request.POST['var3']
    x4 = request.POST['var4']
    x5 = request.POST['var5']
    x6 = request.POST['var6']
    input_property(p_name=x1,p_address=x2,p_landmark=x3,P_city=x4,p_state=x5,p_pincode=x6).save()
    return JsonResponse({'message':'ok'})

def camel(request):
     return render(request,'htmlpages/camelview.html')
def p_view(request):
    k = input_property.objects.all()
    j = [{'v1':i.id,'v2':i.p_name,'v3':i.p_address,'v4':i.p_landmark,'v5':i.P_city,'v6':i.p_state,'v7':i.p_pincode}for i in k]
    return JsonResponse({'display':j})

def otp(request):
     if request.method == 'POST':
          email = request.POST['eml']
          return render(request,'htmlpages/otp.html',{'email':email})
     else:
          return render(request,'htmlpages/otp.html',{})

#  /////request////    
def re(request):
    sample_request=big_form.objects.filter(approved='not approved')
    if request.method=='POST':
        selected_req=big_form.objects.get(id=request.POST['id'])
        if 'approve' in request.POST:
               selected_req.approved='accepted'
     #    if request.method.POST.get('reject') == 'Rejected'                 
        if 'reject' in request.POST:
               selected_req.approved='rejected'
        selected_req.save()
    return render (request,'htmlpages/request.html',{'viewre':sample_request})

def welcome(request):  
     return render(request,'htmlpages/welcom.html')

def info(request):  
     artist_info=big_form.objects.filter(approved='approved')
     return render(request,'htmlpages/info_artist.html',{"info":artist_info})
     
def log_a(request):  
     return render(request,'htmlpages/admin_signup.html')

def message(req):
     if req.method == 'POST':
          nam = req.POST['ms_name']
          ms = req.POST['msg']
          datas = contacts(msg_name=nam,message=ms).save()
     return render(req,'htmlpages/message.html',{'sented':'message sented'})

          