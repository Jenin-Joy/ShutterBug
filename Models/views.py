from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Models.models import *
from Photographers.models import *
# Create your views here

def homepage(request):
    return render(request,"Models/Homepage.html")

def myprofile(request):
    modeldata = tbl_modelregistration.objects.get(id=request.session["mid"])  
    return render(request,"Models/MyProfile.html",{'modeldata':modeldata}) 

def editprofile(request):
    modeldata = tbl_modelregistration.objects.get(id=request.session["mid"]) 
    if request.method == "POST":
        modeldata.model_name=request.POST.get('txtmodel')
        modeldata.model_contact=int(request.POST.get('txtcontact'))
        modeldata.model_email=request.POST.get('txtemail')
        modeldata.model_address=request.POST.get('txtaddress')
        modeldata.save()
        return redirect("webmodel:MyProfile")
    else:
        return render(request,"Models/EditProfile.html",{'modeldata':modeldata})
    
def changepassword(request):
    modeldata=tbl_modelregistration.objects.get(id=request.session["mid"])
    password=modeldata.model_password
    currentpassword=request.POST.get('txtpassword')
    newpassword=request.POST.get('txtnewpassword')
    confirmpassword=request.POST.get('txtcpassword')
        # modeldata.model_password=request.POST.get('txtpassword')
    if currentpassword==password:
        if newpassword==confirmpassword:
            if request.method == "POST":
                modeldata.model_password=confirmpassword
                modeldata.save()
                return redirect("webguest:Login")
            else:
                return redirect("webmodel:ChangePassword")
        else:
            return redirect("webmodel:ChangePassword")
        
    else:
        return render(request,"Models/Changepassword.html",{"modeldata":modeldata})     

def modelpost(request):
    add = tbl_modelpost.objects.all()
    if request.method=="POST":
        image=request.FILES.get('file_image')
        caption=request.POST.get('txtcaption')
        tbl_modelpost.objects.create(post_image=image,post_caption=caption,model_id=tbl_modelregistration.objects.get(id=request.session["mid"]))
        return render(request,"Models/ModelPost.html",{'data':add})
    else:
        return render(request,"Models/ModelPost.html",{'data':add})
    
def deletemodelpost(request,id):
    tbl_modelpost.objects.get(id=id).delete()
    return redirect("webmodel:ModelPost") 

def modelpic(request,id):
    post = tbl_modelpost.objects.get(id=id)
    modelpic = tbl_modelpic.objects.filter(modelpost_id= post)
    if request.method=="POST":
        for image in request.FILES.getlist('file_image'):
            tbl_modelpic.objects.create(modelpost_image=image,modelpost_id=post)
        return render(request,"Models/ModelPic.html",{'data':modelpic,'post':post})
    else:
        return render(request,"Models/ModelPic.html",{'data':modelpic,'post':post})
    
def deletemodelpic(request,id):
    tbl_modelpic.objects.get(id=id).delete()
    return redirect("webmodel:ModelPost") 

def modelcomplaint(request):
    comp = tbl_complaint.objects.filter(model_id=request.session.get("mid"))
    if request.method=="POST":
        title=request.POST.get('txttitle')
        description=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_description=description,model_id=tbl_modelregistration.objects.get(id=request.session["mid"]))
        return render(request,"Models/SendComplaint.html",{'data':comp})
    else:
        return render(request,"Models/SendComplaint.html",{'data':comp})    
    
def deletemodelcomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("webmodel:SendComplaint") 

def modelfeedback(request):
    feed = tbl_feedback.objects.filter(model_id=request.session.get("mid"))
    if request.method=="POST":
        description=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_description=description,model_id=tbl_modelregistration.objects.get(id=request.session["mid"]))
        return render(request,"Models/SendFeedback.html",{'data':feed})
    else:
        return render(request,"Models/SendFeedback.html",{'data':feed})
    
def deletemodelfeedback(request,id):
    tbl_feedback.objects.get(id=id).delete()
    return redirect("webmodel:SendFeedback") 

def viewphotographerbooking(request):
    userdata=tbl_userregistration.objects.all()
    bookingdata=tbl_modelbooking.objects.filter(mbooking_vstatus='0')
    return render(request, "Models/ViewPhotographerBooking.html", {'userdata': userdata, 'bookingdata': bookingdata})  

def acceptphotographerbooking(request,id):
    bookingdata=tbl_modelbooking.objects.get(id=id)
    bookingdata.mbooking_vstatus = "1"
    bookingdata.save()
    return redirect("webmodel:Homepage")  

def rejectphotographerbooking(request,id):
    bookingdata=tbl_modelbooking.objects.get(id=id)
    bookingdata.mbooking_vstatus = "2"
    bookingdata.save()
    return redirect("webmodel:Homepage")  

def acceptedphotographerbooking(request):
    photographerdata=tbl_photographerregistration.objects.all()
    bookingdata = tbl_modelbooking.objects.filter(mbooking_vstatus='1')
    return render(request, "Models/AcceptedPhotographerBooking.html", {'bookingdata': bookingdata,'photographerdata': photographerdata})

def rejectedphotographerbooking(request):
    photographerdata=tbl_photographerregistration.objects.all()
    bookingdata = tbl_modelbooking.objects.filter(mbooking_vstatus='2')
    return render(request, "Models/RejectedPhotographerBooking.html", {'bookingdata': bookingdata,'photographerdata': photographerdata}) 
