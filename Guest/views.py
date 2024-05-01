from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request,"Guest/index.html")

def logout_view(request):
    logout(request)
    return redirect('webguest:index')  # Redirect to the homepage after logout

def contact(request):
    return render(request,"Guest/contact.html")

def about(request):
    return render(request,"Guest/about.html")

def services(request):
    return render(request,"Guest/services.html")

def single(request):
    return render(request,"Guest/single.html")

def modelreg(request):
    dis = tbl_district.objects.all()
    modeldata=tbl_modelregistration.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtmodel')
        contact=int(request.POST.get('txtcontact'))
        email=request.POST.get('txtemail')
        address=request.POST.get('txtaddress')
        gender=request.POST.get('gender')
        place=tbl_place.objects.get(id=request.POST.get('txtplace'))
        photo=request.FILES.get('file_photo')
        proof=request.FILES.get('file_proof')
        password=request.POST.get('txtpassword')
        cpassword=request.POST.get('txtcpassword')
        tbl_modelregistration.objects.create(model_name=name,model_contact=contact,model_email=email,model_address=address,model_gender=gender,model_place=place,model_photo=photo,model_proof=proof,model_password=password,model_cpassword=cpassword)
        return render(request,"Guest/ModelRegistration.html",{'data':modeldata,"district":dis})
    else:
        return render(request,"Guest/ModelRegistration.html",{'data':modeldata,"district":dis})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("disd"))
    pla = tbl_place.objects.filter(district_id=dis)
    return render(request,"Guest/AjaxPlace.html",{"place":pla})

def editorreg(request):
    dis = tbl_district.objects.all()
    cat = tbl_ecategory.objects.all()
    editordata=tbl_editorregistration.objects.all()
    if request.method=="POST":
        name=request.POST.get('txteditor')
        email=request.POST.get('txtemail')
        contact=int(request.POST.get('txtcontact'))
        address=request.POST.get('txtaddress')
        photo=request.FILES.get('file_photo')
        proof=request.FILES.get('file_proof')
        username=request.POST.get('txtusername')
        active=request.POST.get('active')
        gender=request.POST.get('gender')
        place=tbl_place.objects.get(id=request.POST.get('txtplace'))
        category=tbl_ecategory.objects.get(id=request.POST.get('txtecategory'))
        password=request.POST.get('txtpassword')
        cpassword=request.POST.get('txtcpassword')
        tbl_editorregistration.objects.create(editor_name=name,editor_email=email,editor_contact=contact,editor_address=address,editor_photo=photo,editor_proof=proof,editor_username=username,editor_active=active,editor_gender=gender,editor_place=place,editor_password=password,editor_cpassword=cpassword,editor_category=category)
        return render(request,"Guest/EditorRegistration.html",{'data':editordata,"district":dis,"category":cat})
    else:
        return render(request,"Guest/EditorRegistration.html",{'data':editordata,"district":dis,"category":cat})
    
def photographerreg(request):
    dis = tbl_district.objects.all()
    cat = tbl_pcategory.objects.all()
    photographerdata=tbl_photographerregistration.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtphotographer')
        contact=int(request.POST.get('txtcontact'))
        email=request.POST.get('txtemail')
        address=request.POST.get('txtaddress')
        gender=request.POST.get('gender')
        username=request.POST.get('txtusername')
        photo=request.FILES.get('file_photo')
        proof=request.FILES.get('file_proof')        
        active=request.POST.get('active')        
        place=tbl_place.objects.get(id=request.POST.get('txtplace'))
        category=tbl_pcategory.objects.get(id=request.POST.get('txtpcategory'))
        password=request.POST.get('txtpassword')
        cpassword=request.POST.get('txtcpassword')
        tbl_photographerregistration.objects.create(photographer_name=name,photographer_contact=contact,photographer_email=email,photographer_address=address,photographer_gender=gender,photographer_username=username,photographer_photo=photo,photographer_proof=proof,photographer_active=active,photographer_place=place,photographer_category=category,photographer_password=password,photographer_cpassword=cpassword)
        return render(request,"Guest/PhotographerRegistration.html",{'data':photographerdata,"district":dis,"category":cat})
    else:
        return render(request,"Guest/PhotographerRegistration.html",{'data':photographerdata,"district":dis,"category":cat})  

def userreg(request):
    dis = tbl_district.objects.all()
    cat = tbl_category.objects.all()
    userdata=tbl_userregistration.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtuser')
        contact=int(request.POST.get('txtcontact'))
        email=request.POST.get('txtemail')
        gender=request.POST.get('gender')
        address=request.POST.get('txtaddress')
        photo=request.FILES.get('file_photo')
        username=request.POST.get('txtusername')                        
        active=request.POST.get('active')        
        place=tbl_place.objects.get(id=request.POST.get('txtplace'))
        password=request.POST.get('txtpassword')
        cpassword=request.POST.get('txtcpassword')
        tbl_userregistration.objects.create(user_name=name,user_contact=contact,user_email=email,user_gender=gender,user_address=address,user_photo=photo,user_username=username,user_active=active,user_place=place,user_password=password,user_cpassword=cpassword)
        return render(request,"Guest/UserRegistration.html",{'data':userdata,"district":dis,"category":cat})
    else:
        return render(request,"Guest/UserRegistration.html",{'data':userdata,"district":dis,"category":cat})   

def login(request):
    if request.method == "POST":
        email=request.POST.get('txtemail')
        password=request.POST.get('txtpassword')
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        editorcount = tbl_editorregistration.objects.filter(editor_email=email,editor_password=password,editor_status=1).count()
        photographercount = tbl_photographerregistration.objects.filter(photographer_email=email,photographer_password=password,photographer_status=1).count()
        usercount = tbl_userregistration.objects.filter(user_email=email,user_password=password).count()
        modelcount = tbl_modelregistration.objects.filter(model_email=email,model_password=password,model_status=1).count()

        if editorcount > 0:
            editor = tbl_editorregistration.objects.get(editor_email=email,editor_password=password,editor_status=1)
            request.session["did"] = editor.id
            return redirect("webeditor:Homepage")
        
        elif photographercount > 0:
            photographer = tbl_photographerregistration.objects.get(photographer_email=email,photographer_password=password,photographer_status=1)
            request.session["pid"] = photographer.id
            return redirect("webphotographer:Homepage")
        
        elif usercount > 0:
            user = tbl_userregistration.objects.get(user_email=email,user_password=password)
            request.session["uid"] = user.id
            return redirect("webuser:Homepage")   

        elif modelcount > 0:
            model = tbl_modelregistration.objects.get(model_email=email,model_password=password,model_status=1)
            request.session["mid"] = model.id
            return redirect("webmodel:Homepage")  

        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"] = admin.id
            return redirect("webadmin:Homepage")      
             
        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,"Guest/Login.html")  

          
       