from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def Homepage(request):
    return render(request, "Home.html") 

@login_required(login_url='/')
def Aboutpage(request):
    return render(request, "About.html")


def Enquiriespage(request):
    return render(request, "Enquiries.html")

@login_required(login_url='/')
def Memberspage(request):
    return render(request, "Members.html")

 # plans
@login_required(login_url='/')
def PlansAddpage(request):
    contextA = {
        "plansadd_form":Plans_Form()
    }
    if request.method=="POST":
        A = Plans_Form(request.POST)
        if A.is_valid():
            A.save()
            return redirect('/plans/')
    return render(request, "PlansAdd.html", contextA)

@login_required(login_url='/')
def PlansAll(request):
    contextB = {
        "all_plans":Plans.objects.all()
    }
    return render(request, "PlansView.html", contextB)

@login_required(login_url='/')
def PlansDelete(request, id):
    deleteplan = Plans.objects.get(id=id)
    deleteplan.delete()
    return redirect('/plans/')

@login_required(login_url='/')
def PlansUpdate(request, id):
    updateplan = Plans.objects.get(id=id)
    contextC = {
        "plansadd_form":Plans_Form(instance=updateplan)
    }
    if request.method=='POST':
        updatepl = Plans_Form(request.POST, instance=updateplan)
        if updatepl.is_valid:
            updatepl.save()
            return redirect('/plans/')
    return render(request, "PlansAdd.html", contextC)


 #Members
@login_required(login_url='/') 
def MembersView(request):
    contextC = {
        "membersview":Members.objects.all()
    }
    return render(request, "MembersView.html", contextC)

@login_required(login_url='/')
def MembersAddPage(request):
    contextE = {
        "membersadd_form":Members_Form()
    }
    if request.method=="POST":
        plansmodel = Plans.objects.get(id=request.POST['Plan'])
        amount = float(plansmodel.Price) 
        membersmodel = Members(Mobile=request.POST['Mobile'], user=request.POST['user'],
                        Address=request.POST['Address'], Amount=amount,
                        Plan_id=request.POST['Plan'] )
        membersmodel.save()
        return redirect('/members/') 
    return render(request, "MembersAdd.html", contextE)  

@login_required(login_url='/')
def MembersDelete(request, id):
    deletemember = Members.objects.get(id=id)
    deletemember.delete()
    return redirect('/members/')  

@login_required(login_url='/')
def MembersUpdate(request, id):
    membersmodel = Members.objects.get(id=id)
    contextF = {
        "membersadd_form":Members_Form(instance=membersmodel)
    }
    if request.method=='POST':
        plansmodel2 = Plans.objects.get(id=request.POST['Plan'])
        amount = float(plansmodel2.Price) 
        memberfiltered = Members.objects.filter(id=id)
        memberfiltered.update(Mobile=request.POST['Mobile'], user=request.POST['user'],
                        Address=request.POST['Address'], Amount=amount,
                        Plan_id=request.POST['Plan']) 
        return redirect('/members/')
    return render(request, "MembersAdd.html", contextF)
 
    
 #Members Details  
@login_required(login_url='/')  
def Members_DetailsView(request):
    a = Members_Details.objects.all()
    b = Members.objects.all()
    zipped_data = zip(a,b)
    contextD = {
        "members_detailsview_form":zipped_data
    }
    return render(request, "Members_DetailsView.html", contextD)    

@login_required(login_url='/')
def Members_Details_AddPage(request):
    contextG = {
        "members_detailsadd_form":Members_Details_Form()
    }
    if request.method=="POST":
        md_form = Members_Details_Form(request.POST)
        if md_form.is_valid():
            md_form.save()
            return redirect('/membersdetails/')
    return render(request, "Members_DetailsAdd.html", contextG)


 #Login
def LoginPage(request):
    contextH ={
        "errormessage": ""
     }
    if request.method=="POST":
        e_user = authenticate(username= request.POST['usrnme'], 
                             password= request.POST['psswrd']) 
        if e_user is not None:
            login(request, e_user)
            if e_user.role==1:
                return redirect('/home/')
            if e_user.role==2:
                return redirect('/home/')
        else:
            contextI ={
                "errormessage": "Invalid username or password"
            }
            return render(request, 'Login.html', contextI)
    return render(request, 'Login.html', contextH)     

def Logout(request):
    logout(request)
    return redirect('/')

 
 #Signup
def SignupPage(request):
    contextJ ={
        "err":""
    }
    if request.method=="POST":
        userA_model = User_A.objects.filter(username=request.POST['usrnme'])
        if len(userA_model)>0:
            contextK ={
                "err":"username already exist!"
            }
            return render(request, 'Signup.html', contextK)
        else:
            newuser = User_A(username=request.POST['usrnme'], email=request.POST['eml'], role=request.POST['rle'])
            newuser.set_password(request.POST['psswrd'])                 
            newuser.save()
            return redirect("/")
    return render(request, 'Signup.html', contextJ)    