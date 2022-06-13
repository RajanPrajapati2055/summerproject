# from os import uname

from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from app.models import Contact, Customer,Supplier,Medicine
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
 return render(request,'index.html')

def supplierdata(request):
    data=Supplier.objects.all()
    context={'view':data}
    return render(request,'supplierdata.html',context)


def About(request):
    return render(request, 'About.html')

def Product(request):
    data=Medicine.objects.all()
    context={'views':data}
    return render(request, 'Product.html',context)

def cart(request):
    return render(request, 'cart.html')

def customerdetail(request):
    data=Customer.objects.all()
    context={'views':data}
    return render(request, 'customerdetail.html',context)

# def handleLogin(request):
#     if request.method == "POST":
#         email=request.POST.get('email','')
#         password=request.POST.get('password','')
#         myuser=authenticate(email=email,password=password)
#         if myuser is not None:
#             if myuser.is_active:
#                 login(request, myuser)
#                 messages.success(request,'Successfully Logged In')
#                 return redirect("/")
#         else:
#             messages.error(request,'invalidate credential ')   
#             # return render(request,'Login.html') 
#     return render(request, 'Login.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/Dashboard')
            else:
                return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)



def signout(request):
    logout(request)
    return redirect('/')



# def signin(request):
    # form = AuthenticationForm()
    # if request.method == "POST":
    #     form = AuthenticationForm(data=request.POST)

    #     if form.is_valid():
    #         user = authenticate(
    #             email=form.cleaned_data['username'], 
    #             password=form.cleaned_data['password'])
    #         login(request, user)
    #         return redirect('/')

    # return render(request, 'signin.html', {'form': form})



# def handleLogout(request):
#     return render(request, 'login.html')

def Register(request):
    if request.method == "POST":
      uname=request.POST.get('uname')
      fname=request.POST.get('fname')
      lname=request.POST.get('lname')
      email=request.POST.get('email')
      password=request.POST.get('pass')
      confirmpassword=request.POST.get('cpass')
      myuser=User.objects.create_user(uname,email,password)
      myuser.save()




    return render(request, 'Register.html' )
    

def contact(request):
    if request.method=="POST":
        Name=request.POST.get('fname','')
        Phone=request.POST.get('phone','')
        Email=request.POST.get('email','')
        Dec=request.POST.get('dec','')
        Date=request.POST.get('date','')
        con=Contact(name=Name,phone=Phone,email=Email,desc=Dec,date=Date)
        # print(name=name, phone=phone, email=email, dec=dec, date=date)
        con.save()
        # messages.success(request, 'Your message have been sent.')
        
    return render(request, 'Contact.html')

def medicine(request):
    if request.method=="POST":
       Medicinename=request.POST.get('Mediname')
       Costprice=request.POST.get('cprice')
       Sellingprice=request.POST.get('sprice')
       Medicinecompanyname=request.POST.get('MedcoName')
    #    medi=Medicine(medicinename=Medicinename,costprice=Costprice,sellingprice=Sellingprice,medicinecompanyname=Medicinecompanyname)
    #    medi.save()
       Medicine.objects.create(medicinename=Medicinename,costprice=Costprice,sellingprice=Sellingprice,medicinecompanyname=Medicinecompanyname)
    return render(request,'Medicine.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

def supplier(request):
    if request.method=="POST":
        suppliername=request.POST.get('suppliername','')
        supplierontact=request.POST.get('suppliercontact','')
        supplieremail=request.POST.get('supplieremail','')
        supplieraddress=request.POST.get('supplieraddress','')
        
        sup=Supplier(Suppliername=suppliername,Supplierontact=supplierontact,Supplieremail=supplieremail,Supplieraddress=supplieraddress)
        sup.save()

    return render(request, 'Supplier.html')
