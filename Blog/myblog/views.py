from django.shortcuts import render,redirect
from django.http import HttpResponse
from myblog import dbcon
from .models import myblog ,category ,auther ,categoryblog ,comments
from django import forms
# from .forms import *
import os
def hello(request):
    if request.POST.get('name'):
        cid = request.POST.get('name')
        blogid = categoryblog.objects.filter( cid_id= cid)
        # print(getattr[blogid,'2'])
        blogs=[]
        for b in blogid:
            data = myblog.objects.get(id = b.bid_id)

            blogs.append(data)
        cat = category.objects.all()
        return render(request,'welcom.html',{'data':blogs,'category':cat})
    else :
        data = myblog.objects.all()
        cat = category.objects.all()
        return render(request,'welcom.html',{'data':data,'category':cat})

def addcateg(request):
    cat = category.objects.all()
    if request.POST.get('category'):
        catg = request.POST.get('category')
        category.objects.create(bcategory= catg)
        cat = category.objects.all()
        return render(request,'addcategoey.html',{'categories':cat})
    else :
        return render(request,'addcategoey.html',{'categories':cat})
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
        authobj=  auther.objects.get(email = email)
        if auther.objects.get(email = email):
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
        else:
            msg = " please register as an author"
            return render(request , 'createblog.html',{'category':cate, 'msg':msg})
    else:
        return render(request , 'createblog.html',{'category':cate, 'msg':msg})
