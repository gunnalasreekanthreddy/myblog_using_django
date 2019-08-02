from django.shortcuts import render,redirect
from django.http import HttpResponse
from myblog import dbcon
from .models import myblog ,category ,auther ,categoryblog ,comments
from django import forms
import math, random
from .sendemail import *
# from .forms import *
import os
def hello(request):
    if request.POST.get('name'):
        cid = request.POST.get('name')
        blogid = categoryblog.objects.filter( cid_id= cid)
        # print(getattr[blogid,'2'])
        blog_list = []
        # Blog_author = []
        for b in blogid:
            data = myblog.objects.get(id = b.bid_id)
            # author_name= auther.objects.get(id = data.author_id)
            # Blog_author.append(author_name)
            blog_list.append(data)
        Blog_author = auther.objects.all()
        cat = category.objects.all()
        name = category.objects.get(id = cid)
        return render(request,'welcom.html',{'bloglist':blog_list,'authorlist':Blog_author,'category':cat , 'name':name})
    else :
        data = myblog.objects.all().order_by('-id')[:4]
        auth = auther.objects.all()
        cat = category.objects.all()
        name ="latest blogs"
        return render(request,'welcom.html',{'bloglist':data,'authorlist':auth,'category':cat,'name':name })

def addcateg(request):
    cat = category.objects.all()
    if request.POST.get('category'):
        catg = request.POST.get('category')
        ca = catg.lower()
        for c in cat:
            if ca == c.bcategory:
                msg = 'category already exist'
                return render(request,'addcategoey.html',{'categories':cat,'msg':msg})
        category.objects.create(bcategory= catg)
        cat = category.objects.all()
        msg = 'succesfully category added'
        return render(request,'addcategoey.html',{'categories':cat, 'msg':msg})
    else :
        msg= ''
        return render(request,'addcategoey.html',{'categories':cat , 'msg':msg})
# def addblogcategory(request):
#         if request.method == 'POST':
#             form = addblogcategory1(request.POST, request.FILES)
#
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')
#         else:
#             form = addblogcategory1()
#         return render(request, 'blogdetails.html', {'form' : form})
# def details(request):
#
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = BlogForm()
#     return render(request, 'blogdetails.html', {'form' : form})
# def addcatui(request):
#         catg = request.POST.get('category')
#         category.objects.create(bcategory= catg)
#         data = myblog.objects.all()
#         cat = category.objects.all()
#         return render(request,'welcom.html',{'data':data,'category':cat})
# def addblog(request):
#     return render(request,'createblog.html')
# def auth(request):
#     return render(request,'authername.html')
# def authui(request):
#     auth = request.POST.get('authname')
#     auther.objects.create(bauthor= auth)
#     return render(request,'authername.html')
def authcreate(request):
    if request.POST.get('email') :
        email = request.POST.get('email')
        name = request.POST.get('name')
        auther.objects.create(bauthor= name ,email= email)
        return render(request,'authercreate.html')
    else :
        return render(request,'authercreate.html')
def createblog(request):
    cate = category.objects.all()
    msg = ""
    if request.POST.get('email'):
        email = request.POST.get('email')
        print(email)
        au = auther.objects.all()
        for a in au :
            if email == a.email:
                authobj=  auther.objects.get(email = email)
                title = request.POST.get('title')
                print(title)
                cid = request.POST.get('category')
                image = request.POST.get('image')
                discription = request.POST.get('discription')
                aid=authobj.id
                print(aid)
                ccid=category.objects.get(id = cid)
                myblog.objects.create(author = authobj, btitle = title, bdiscription = discription , bimage = image)
                myblg = myblog.objects.get(author = authobj , btitle = title, bdiscription = discription , bimage = image)
                categoryblog.objects.create(bid = myblg , cid = ccid)
                return render(request , 'createblog.html',{'category':cate, 'msg':msg})

        msg = " please register as an author"
        return render(request , 'createblog.html',{'category':cate, 'msg':msg})
    else:
        return render(request , 'createblog.html',{'category':cate, 'msg':msg})

def email(request):
    OTP = ""
    if request.POST.get('email'):
        digits = "0123456789"
        for i in range(4) :
            OTP += digits[math.floor(random.random() * 10)]
        mail = request.POST.get('email')
        sendEmail(mail,OTP)
        return render(request,'otp.html',{'otp':OTP})
    elif request.POST.get('otp'):
        ot = request.POST.get('otp')
        pot = request.POST.get('potp')
        print("hi")
        print(ot)
        print("welcome")
        print(pot)
        if pot == ot :
            cate = category.objects.all()
            return render(request , 'createblog.html',{'category':cate})
        else:
            msg = "pleasen enter correct otp"
            return render(request , 'entermail.html',{'msg':msg})


    else:
        return render(request , 'entermail.html')
