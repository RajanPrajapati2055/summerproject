# from os import uname

from email import message
from multiprocessing import context
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from app.models import Contact, Customer,Supplier,Medicine,Prescription,Cart
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files import File as DjangoFile
from app.forms import ImageForm
import requests
from django.http import JsonResponse

# Create your views here.
def index(request):
 return render(request,'index.html')

def supplierdata(request):
    data=Supplier.objects.all()
    context={'view':data}
    return render(request,'supplierdata.html',context)

def feedback(request):
    data=Contact.objects.all()
    context={'show':data}
    return render(request,'Feedback.html',context)

def About(request):
    return render(request, 'About.html')

def Order(request):
 return render(request,'Order.html')

def Product(request):
    data=Medicine.objects.all()
    context={'views':data}
    return render(request, 'Product.html',context)

# def cart(request):
#     return render(request, 'cart.html')

def medicineupdate(request):
    return render(request, 'medicineupdate.html')

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
                return redirect('/Dashboard')
        else:
            messages.info(request, 'Username OR password is having error')

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
      message.success(request, 'Congratulations!! Register Successfull')

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

# this function add the medicine
def medicine(request):
    if request.method=="POST":
       Medicinename=request.POST.get('Mediname')
       Costprice=request.POST.get('cprice')
       Sellingprice=request.POST.get('sprice')
       Medicinecompanyname=request.POST.get('MedcoName')
       Medicine.objects.create(medicinename=Medicinename,costprice=Costprice,sellingprice=Sellingprice,medicinecompanyname=Medicinecompanyname)
       return render(request,'Medicine.html')

    else:
        return render(request,'Medicine.html')

#this is update for Medicine
def updatemedicine(request, id = ''):
    if request.method=="POST":
       Medicinename=request.POST.get('Mediname')
       Costprice=request.POST.get('cprice')
       Sellingprice=request.POST.get('sprice')
       Medicinecompanyname=request.POST.get('MedcoName')
       Medicine.objects.filter(pk=id).update(medicinename=Medicinename,costprice=Costprice,sellingprice=Sellingprice,medicinecompanyname=Medicinecompanyname)

       return render(request,'medicineupdate.html')

    else:
        pi = Medicine.objects.get(pk=id)
        # print(pi.medicinename)
        # print(pi.costprice)

        return render(request, 'medicineupdate.html', {'medicine': pi})


#this function deletes the medicine data
def delete_medicine(request, id):
    if request.method =='POST':
        pi = Medicine.objects.get(pk=id)
        pi.delete()
        return redirect('/Product')


def Dashboard(request):
    return render(request, 'Dashboard.html')

def supplier(request):
    if request.method=="POST":
        suppliername=request.POST.get('suppliername','')
        suppliercontact=request.POST.get('suppliercontact','')
        supplieremail=request.POST.get('supplieremail','')
        supplieraddress=request.POST.get('supplieraddress','')
        
        sup=Supplier(Suppliername=suppliername,Suppliercontact=suppliercontact,Supplieremail=supplieremail,Supplieraddress=supplieraddress)
        sup.save()

    return render(request, 'Supplier.html')

#this function deletes the Supplier data
def delete_supplier(request, id):
    if request.method =='POST':
        pi = Supplier.objects.get(pk=id)
        pi.delete()
        return redirect('/supplierdata')

#this is update for Supplier
def update_supplier(request, id = ''):
    if request.method=="POST":
       suppliername=request.POST.get('suppliername')
       supplieremail=request.POST.get('supplieremail')
       suppliercontact=request.POST.get('suppliercontact')
       supplieraddress=request.POST.get('supplieraddress')
       Supplier.objects.filter(pk=id).update(Suppliername=suppliername,Suppliercontact=suppliercontact,Supplieraddress=supplieraddress,Supplieremail=supplieremail)

    #    return redirect(request,'supplierdata.html')
       return render(request,'supplierupdate.html')


    else:
        pi = Supplier.objects.get(pk=id)
        # print(pi.medicinename)
        # print(pi.costprice)

        return render(request, 'supplierupdate.html', {'supplier': pi})




def add_to_cart(request, id):
    user = request.user
    qty=request.POST.get('qty')
    medicine_id = id
    customer = Customer.objects.get(fullname=user)
    medicine = Medicine.objects.get(id=medicine_id )
    Cart(customer=customer, medicine=medicine, quantity=qty).save()
    return redirect('/cartshow')



def show_cart(request):
    totalitem = 0
    user = request.user
    customer = Customer.objects.get(fullname=user)
    cart = Cart.objects.filter(customer=customer)
    totalitem = len(Cart.objects.filter(customer=customer))

    print(cart)
    amount = 0.0
    shipping_amount = 100.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.customer == customer]
    # print(cart_product)
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.medicine.sellingprice)
            amount += tempamount
            totalamount = amount + shipping_amount

        return render(request, 'cart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
    else:
        return render(request, 'emptycart.html', {'totalitem': totalitem})

def remove_cart(request, id):
    medicine = Medicine.objects.get(pk=id)
    # cart = Cart(request)
    # Cart.objects.delete()
    pi = Cart.objects.get(medicine=medicine)
    pi.delete()
    return redirect('/cartshow')


def Payment(request):
 return render(request,'payment.html')


def prescriptions(request):
    if request.method=="POST":
        Doctorname=request.POST.get('doctorname','')
        Hospitalname=request.POST.get('hospitalname','')
        Hospitalcontact=request.POST.get('hospitalcontact','')
        Hospitaladdress=request.POST.get('hospitaladdress','')
        uploaded_file = request.FILES['prescriptionimage']

        pre=Prescription(DoctorName=Doctorname,HospitalName=Hospitalname,HospitalContact=Hospitalcontact,HospitalAddress=Hospitaladdress,Photo=uploaded_file)
        pre.save()
        # form = ImageForm(request.POST, request.FILES)  
        # if form.is_valid():
        #     form.save()
        #     return redirect("/")
        # hello=Prescription(DoctorName=Doctorname,HospitalName=Hospitalname,HospitalContact=Hospitalcontact,HospitalAddress=Hospitaladdress,Photo=form)
        # hello.save()

          
        #image = Prerequest.FILES('image')
        #request.FILES('prescriptionimage','')

       # image = Prescription(request.POST,'prescriptionimage' ,request.FILES)
        
        
        
    return render(request, 'prescription.html')

def Khaltirequest(request):

    return render(request,'khaltirequest.html')    
def Khaltiverify(request):
    token=request.GET.get("token")
    amount=request.GET.get("amount")
    id=request.GET.get("id")
    print(token,amount,id)


    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
    "token":token,
    "amount": amount
    }
    headers = {
    "Authorization": "Key test_public_key_ff7becf08dcc40eebcf523921e397147"
    }

    response = requests.post(url, payload, headers = headers)
    resp_dict=response.postjson()
    if resp_dict.get("idx"):
      success=True
      payment =Payment.objects.all()
      payment.save()
    else:
      success=False

    data={
        "success":success
    } 
    return JsonResponse(data)   
       