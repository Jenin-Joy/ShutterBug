from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Photographers.models import *
from Editors.models import *
from datetime import datetime
from django.db.models import Q
# Create your views here

def homepage(request):
    editordata = tbl_editorregistration.objects.get(id=request.session["did"])  
    return render(request,"Editors/Homepage.html",{'editordata':editordata})

def myprofile(request):
    editordata = tbl_editorregistration.objects.get(id=request.session["did"])  
    return render(request,"Editors/MyProfile.html",{'editordata':editordata}) 

def editprofile(request):
    editordata = tbl_editorregistration.objects.get(id=request.session["did"]) 
    if request.method == "POST":
        editordata.editor_name=request.POST.get('txteditor')
        editordata.editor_contact=int(request.POST.get('txtcontact'))
        editordata.editor_email=request.POST.get('txtemail')
        editordata.editor_address=request.POST.get('txtaddress')
        editordata.save()
        return redirect("webeditor:MyProfile")
    else:
        return render(request,"Editors/EditProfile.html",{'editordata':editordata})
    
def changepassword(request):
    editordata=tbl_editorregistration.objects.get(id=request.session["did"])
    password=editordata.editor_password
    currentpassword=request.POST.get('txtpassword')
    newpassword=request.POST.get('txtnewpassword')
    confirmpassword=request.POST.get('txtcpassword')
        # editordata.editor_password=request.POST.get('txtpassword')
    if currentpassword==password:
        if newpassword==confirmpassword:
            if request.method == "POST":
                editordata.editor_password=confirmpassword
                editordata.save()
                return redirect("webguest:Login")
            else:
                return redirect("webeditor:ChangePassword")
        else:
            return redirect("webeditor:ChangePassword")
        
    else:
        return render(request,"Editors/Changepassword.html",{"editordata":editordata})     

def post(request):
    post = tbl_post.objects.filter(editor_id=request.session["did"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        caption=request.POST.get('txtcaption')
        image=request.FILES.get('file_image')
        amount=request.POST.get('txtamount')
        editordata = tbl_editorregistration.objects.get(id=request.session["did"])
        tbl_post.objects.create(post_title=title,post_caption=caption,post_image=image,post_amount=amount,editor_id=editordata)
        return render(request,"Editors/Post.html",{'data':post})
    else:
        return render(request,"Editors/Post.html",{'data':post})
    
def deletepost(request,pid):
    tbl_post.objects.get(id=pid).delete()
    return redirect("webeditor:Post")    

def editpost(request,id):
    post=tbl_post.objects.get(id=id)
    if request.method == "POST":
        post.post_title=request.POST.get('txttitle')
        post.post_caption=request.POST.get('txtcaption')
        post.post_amount=request.POST.get('txtamount')
        post.save()
        return redirect("webeditor:Post")
    else:
        return render(request,"Editors/Post.html",{'post':post})    
 

def editorcomplaint(request):
    comp = tbl_complaint.objects.filter(editor_id=request.session.get("did"))
    if request.method=="POST":
        title=request.POST.get('txttitle')
        description=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_description=description,editor_id=tbl_editorregistration.objects.get(id=request.session["did"]))
        return render(request,"Editors/SendComplaint.html",{'data':comp})
    else:
        return render(request,"Editors/SendComplaint.html",{'data':comp})    
    
def deleteeditorcomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("webeditor:SendComplaint")    

def editorfeedback(request):
    feed = tbl_feedback.objects.filter(editor_id=request.session.get("did"))
    if request.method=="POST":
        description=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_description=description,editor_id=tbl_editorregistration.objects.get(id=request.session["did"]))
        return render(request,"Editors/SendFeedback.html",{'data':feed})
    else:
        return render(request,"Editors/SendFeedback.html",{'data':feed})
    
def deleteeditorfeedback(request,id):
    tbl_feedback.objects.get(id=id).delete()
    return redirect("webeditor:SendFeedback")   

def editoraddgallery(request,id):
    post = tbl_post.objects.get(id=id)
    gallery = tbl_addgallery.objects.filter(post_id=id)
    if request.method=="POST":
        caption=request.POST.get('txtcaption')
        for image in request.FILES.getlist('file_image'):
            tbl_addgallery.objects.create(addgallery_image=image,addgallery_caption=caption,post_id=post)
        return render(request,"Editors/Addgallery.html",{'data':gallery,'post':post})
    else:
        return render(request,"Editors/Addgallery.html",{'data':gallery,'post':post})
    
def editordeletegallery(request,id):
    tbl_addgallery.objects.get(id=id).delete()
    return redirect("webeditor:Post") 

def viewphotographerbooking(request):
    userdata=tbl_userregistration.objects.all()
    bookingdata=tbl_editorbooking.objects.filter(ebooking_vstatus='0')
    return render(request, "Editors/ViewPhotographerBooking.html", {'userdata': userdata, 'bookingdata': bookingdata})  

def acceptphotographerbooking(request,id):
    bookingdata=tbl_editorbooking.objects.get(id=id)
    bookingdata.ebooking_vstatus = "1"
    bookingdata.save()
    return redirect("webeditor:Homepage")  

def rejectphotographerbooking(request,id):
    bookingdata=tbl_editorbooking.objects.get(id=id)
    bookingdata.ebooking_vstatus = "2"
    bookingdata.save()
    return redirect("webeditor:Homepage")  

def acceptedphotographerbooking(request):
    photographerdata=tbl_photographerregistration.objects.all()
    bookingdata = tbl_editorbooking.objects.filter().exclude(ebooking_vstatus='2')
    
    return render(request, "Editors/AcceptedPhotographerBooking.html", {'bookingdata': bookingdata,'photographerdata': photographerdata})

def rejectedphotographerbooking(request):
    photographerdata=tbl_photographerregistration.objects.all()
    bookingdata = tbl_editorbooking.objects.filter(ebooking_vstatus='2')
    
    return render(request, "Editors/RejectedPhotographerBooking.html", {'bookingdata': bookingdata,'photographerdata': photographerdata})



###############################################################################################################################

def chatpage(request,id):
    user  = tbl_photographerregistration.objects.get(id=id)
    return render(request,"Editors/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_editorregistration.objects.get(id=request.session["did"])
    to_user = tbl_photographerregistration.objects.get(id=request.POST.get("tid"))
    tbl_epchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),editor_from=from_user,photographer_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Editors/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_editorregistration.objects.get(id=request.session["did"])
    chat_data = tbl_epchat.objects.filter((Q(editor_from=user) | Q(editor_to=user)) & (Q(photographer_from=tid) | Q(photographer_to=tid))).order_by('chat_time')
    return render(request,"Editors/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_epchat.objects.filter(Q(editor_from=request.session["did"]) & Q(photographer_to=request.GET.get("tid")) | (Q(photographer_from=request.GET.get("tid")) & Q(editor_to=request.session["did"]))).delete()
    return render(request,"Editors/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})