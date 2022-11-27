from django.shortcuts import render

# Create your views here.

def goog(req):
    return render(req,'page/google_sign.html')