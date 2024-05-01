from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Photographers.models import *
from Models.models import *
from User.models import *
from datetime import datetime
from django.db.models import Q
# Create your views here

def homepage(request):
    photographerdata = tbl_photographerregistration.objects.get(id=request.session["pid"])  
    return render(request,"Photographers/Homepage.html",{'photographerdata':photographerdata})

def myprofile(request):
    photographerdata = tbl_photographerregistration.objects.get(id=request.session["pid"])  
    return render(request,"Photographers/MyProfile.html",{'photographerdata':photographerdata}) 

def editprofile(request):
    photographerdata = tbl_photographerregistration.objects.get(id=request.session["pid"]) 
    if request.method == "POST":
        photographerdata.photographer_name=request.POST.get('txtphotographer')
        photographerdata.photographer_contact=int(request.POST.get('txtcontact'))
        photographerdata.photographer_email=request.POST.get('txtemail')
        photographerdata.photographer_address=request.POST.get('txtaddress')
        photographerdata.save()
        return redirect("webphotographer:MyProfile")
    else:
        return render(request,"Photographers/EditProfile.html",{'photographerdata':photographerdata})
    
def changepassword(request):
    photographerdata=tbl_photographerregistration.objects.get(id=request.session["pid"])
    password=photographerdata.photographer_password
    currentpassword=request.POST.get('txtpassword')
    newpassword=request.POST.get('txtnewpassword')
    confirmpassword=request.POST.get('txtcpassword')
        # photographerdata.photographer_password=request.POST.get('txtpassword')
    if currentpassword==password:
        if newpassword==confirmpassword:
            if request.method == "POST":
                photographerdata.photographer_password=confirmpassword
                photographerdata.save()
                return redirect("webguest:Login")
            else:
                return redirect("webphotographer:ChangePassword")
        else:
            return redirect("webphotographer:ChangePassword")
        
    else:
        return render(request,"Photographers/Changepassword.html",{"photographerdata":photographerdata})     

def post(request):
    post = tbl_post.objects.filter(photographer_id=request.session["pid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        caption=request.POST.get('txtcaption')
        image=request.FILES.get('file_image')
        amount=request.POST.get('txtamount')
        photographerdata = tbl_photographerregistration.objects.get(id=request.session["pid"])
        tbl_post.objects.create(post_title=title,post_caption=caption,post_image=image,post_amount=amount,photographer_id=photographerdata)
        return render(request,"Photographers/Post.html",{'data':post})
    else:
        return render(request,"Photographers/Post.html",{'data':post})
    
def deletepost(request,pid):
    tbl_post.objects.get(id=pid).delete()
    return redirect("webphotographer:Post")    

def editpost(request,id):
    post=tbl_post.objects.get(id=id)
    if request.method == "POST":
        post.post_title=request.POST.get('txttitle')
        post.post_caption=request.POST.get('txtcaption')
        post.post_amount=request.POST.get('txtamount')
        post.save()
        return redirect("webphotographer:Post")
    else:
        return render(request,"Photographers/Post.html",{'post':post})   
   
 

def photographercomplaint(request):
    comp = tbl_complaint.objects.filter(photographer_id=request.session.get("pid"))
    if request.method=="POST":
        title=request.POST.get('txttitle')
        description=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_description=description,photographer_id=tbl_photographerregistration.objects.get(id=request.session["pid"]))
        return render(request,"Photographers/SendComplaint.html",{'data':comp})
    else:
        return render(request,"Photographers/SendComplaint.html",{'data':comp})    
    
def deletephotographercomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("webphotographer:SendComplaint")

def photographerfeedback(request):
    feed = tbl_feedback.objects.filter(photographer_id=request.session.get("pid"))
    if request.method=="POST":
        description=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_description=description,photographer_id=tbl_photographerregistration.objects.get(id=request.session["pid"]))
        return render(request,"Photographers/SendFeedback.html",{'data':feed})
    else:
        return render(request,"Photographers/SendFeedback.html",{'data':feed})
    
def deletephotographerfeedback(request,id):
    tbl_feedback.objects.get(id=id).delete()
    return redirect("webphotographer:SendFeedback")  

def searcheditor(request):
    editorcategory = tbl_ecategory.objects.all()
    editor = tbl_editorregistration.objects.filter(editor_status=1)
    return render(request, "Photographers/SearchEditor.html", {'editorcategory': editorcategory,'editor': editor})

def ajaxeditor(request):
    if request.GET.get("cid")!="":
        category = tbl_ecategory.objects.get(id=request.GET.get("cid"))
        editor = tbl_editorregistration.objects.filter(editor_category=category)
        return render(request,"Photographers/AjaxEditor.html",{"editor":editor})
    else:
        return render(request,"Photographers/AjaxEditor.html")

def searchmodel(request):
    disdata = tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    model = tbl_modelregistration.objects.filter(model_status=1)
    return render(request, "Photographers/SearchModeling.html", {'model': model,'disdata': disdata,'placedata': placedata})

def ajaxmodel(request):
    if request.GET.get("pid")!="":
        place = tbl_place.objects.get(id=request.GET.get("pid"))
        model = tbl_modelregistration.objects.filter(model_place=place)
        return render(request,"Photographers/AjaxModel.html",{"model":model})
    elif request.GET.get("did")!="":
        dis = tbl_district.objects.get(id=request.GET.get("did"))
        model = tbl_modelregistration.objects.filter(model_place__district_id=dis)
        return render(request,"Photographers/AjaxModel.html",{"model":model})
    else:
        return render(request,"Photographers/AjaxModel.html")
    
def photographeraddgallery(request,id):
    post = tbl_post.objects.get(id=id)
    gallery = tbl_addgallery.objects.filter(post_id= post)
    if request.method=="POST":
        caption=request.POST.get('txtcaption')
        for image in request.FILES.getlist('file_image'):
            tbl_addgallery.objects.create(addgallery_image=image,addgallery_caption=caption,post_id=post)
        return render(request,"Photographers/Addgallery.html",{'data':gallery,'post':post})
    else:
        return render(request,"Photographers/Addgallery.html",{'data':gallery,'post':post})
    
def photographerdeletegallery(request,id):
    tbl_addgallery.objects.get(id=id).delete()
    return redirect("webphotographer:Post") 

def editorviewpost(request,id):
    postdata=tbl_post.objects.get(id=id)
    return render(request,"Photographers/ViewPost.html",{'postdata':postdata})       
    
def editorviewmore(request,id):
    postdata=tbl_post.objects.get(id=id)
    viewmoredata=tbl_addgallery.objects.filter(post_id=postdata)
    return render(request,"Photographers/EditorViewMore.html",{'postdata':postdata,'viewmoredata':viewmoredata})  

def modelviewpost(request,id):
    postdata=tbl_modelpost.objects.filter(id=id)
    return render(request,"Photographers/ViewModelPost.html",{'postdata':postdata})       
    
def modelviewmore(request,id):
    postdata=tbl_modelpost.objects.get(id=id)
    viewmoredata=tbl_modelpic.objects.filter(modelpost_id=postdata)
    return render(request,"Photographers/ModelViewMore.html",{'postdata':postdata,'viewmoredata':viewmoredata}) 

def editorbooking(request,did):
    editordata=tbl_editorregistration.objects.get(id=did)
    photographerdata=tbl_photographerregistration.objects.get(id=request.session["pid"])
    if request.method=="POST":
        tbl_editorbooking.objects.create(booking_date=request.POST.get("for_date"),
                                               ebooking_description=request.POST.get("txtdescription"),
                                               editor_id=editordata,
                                               photographer_id=photographerdata)
        return redirect("webphotographer:SearchEditor")
    else:
        return render(request,"Photographers/EditorBooking.html")
    
def modelbooking(request,mid):
    modeldata=tbl_modelregistration.objects.get(id=mid)
    photographerdata=tbl_photographerregistration.objects.get(id=request.session["pid"])
    if request.method=="POST":
        tbl_modelbooking.objects.create(booking_date=request.POST.get("for_date"),
                                               mbooking_description=request.POST.get("txtdescription"),
                                               model_id=modeldata,
                                               photographer_id=photographerdata)
        return redirect("webphotographer:SearchModel")
    else:
        return render(request,"Photographers/ModelBooking.html")    
    
def vieweditorbooking(request):
    editordata=tbl_editorregistration.objects.all()
    bookingdata=tbl_editorbooking.objects.filter(photographer_id=request.session["pid"])
    return render(request, "Photographers/ViewMyEditorBooking.html", {'editordata': editordata, 'bookingdata': bookingdata})

def viewmodelbooking(request):
    modeldata=tbl_modelregistration.objects.all()
    bookingdata=tbl_modelbooking.objects.all()
    return render(request, "Photographers/ViewMyModelBooking.html", {'modeldata': modeldata, 'bookingdata': bookingdata})   

# def viewuserbooking(request):
#     userdata=tbl_userregistration.objects.all()
#     bookingdata=tbl_photographerbooking.objects.all()
#     return render(request, "Photographers/ViewUserBooking.html", {'userdata': userdata, 'bookingdata': bookingdata})  

def viewuserbooking(request):
    userdata=tbl_userregistration.objects.all()
    bookingdata = tbl_photographerbooking.objects.filter(pbooking_vstatus='0')
    return render(request, "Photographers/ViewUserBooking.html", {'userdata': userdata,'bookingdata': bookingdata})

def acceptuserbooking(request,id):
    bookingdata=tbl_photographerbooking.objects.get(id=id)
    bookingdata.pbooking_vstatus = "1"
    bookingdata.save()
    return redirect("webphotographer:Homepage")  

def rejectuserbooking(request,id):
    bookingdata=tbl_photographerbooking.objects.get(id=id)
    bookingdata.pbooking_vstatus = "2"
    bookingdata.save()
    return redirect("webphotographer:Homepage")  

def accepteduserbooking(request):
    userdata=tbl_userregistration.objects.all()
    bookingdata = tbl_photographerbooking.objects.filter(pbooking_vstatus='1')
    
    return render(request, "Photographers/AcceptedUserBooking.html", {'bookingdata': bookingdata,'userdata': userdata})

def rejecteduserbooking(request):
    userdata=tbl_userregistration.objects.all()
    bookingdata = tbl_photographerbooking.objects.filter(pbooking_vstatus='2')
    
    return render(request, "Photographers/RejectedUserBooking.html", {'bookingdata': bookingdata,'userdata': userdata})

def editorpayment(request,id):
    bookingdata=tbl_editorbooking.objects.get(id=id)
    if request.method=="POST":
        bookingdata.ebooking_vstatus=3
        bookingdata.save()
        return redirect("webphotographer:ViewEditorBooking")
    else:
        return render(request,"Photographers/Payment.html",{'bookingdata':bookingdata})

def modelpayment(request,id):
    bookingdata=tbl_modelbooking.objects.get(id=id)
    if request.method=="POST":
        bookingdata.mbooking_vstatus=3
        bookingdata.save()
        return redirect("webphotographer:ViewModelBooking")
    else:
        return render(request,"Photographers/Payment.html",{'bookingdata':bookingdata})  

###############################################################################################################################
    
def chatpage(request,id):
    user  = tbl_userregistration.objects.get(id=id)
    return render(request,"photographers/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_photographerregistration.objects.get(id=request.session["pid"])
    to_user = tbl_userregistration.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"photographers/Chat.html")
        

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_photographerregistration.objects.get(id=request.session["pid"])
    chat_data = tbl_chat.objects.filter((Q(photographer_from=user) | Q(photographer_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"photographers/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(photographer_from=request.session["pid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(photographer_to=request.session["pid"]))).delete()
    return render(request,"photographers/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


def editorchatpage(request,id):
    ebk = tbl_editorbooking.objects.get(id=id)
    user  = tbl_editorregistration.objects.get(id=ebk.editor_id_id)
    return render(request,"photographers/Photographer_chat.html",{"user":user})

def editorajaxchat(request):
    from_user = tbl_photographerregistration.objects.get(id=request.session["pid"])
    print(request.POST.get("tid"))
    to_user = tbl_editorregistration.objects.get(id=request.POST.get("tid"))
    tbl_epchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_user,editor_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"photographers/Photographer_chat.html")
        

def editorajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_photographerregistration.objects.get(id=request.session["pid"])
    chat_data = tbl_epchat.objects.filter((Q(photographer_from=user) | Q(photographer_to=user)) & (Q(editor_from=tid) | Q(editor_to=tid))).order_by('chat_time')
    return render(request,"photographers/Photographer_chat_view.html",{"data":chat_data,"tid":int(tid)})

def editorclearchat(request):
    tbl_epchat.objects.filter(Q(photographer_from=request.session["pid"]) & Q(editor_to=request.GET.get("tid")) | (Q(editor_from=request.GET.get("tid")) & Q(photographer_to=request.session["pid"]))).delete()
    return render(request,"photographers/Photographer_clear_chat.html",{"msg":"Chat Deleted Sucessfully...."})