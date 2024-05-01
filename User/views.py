from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
# Create your views here

def homepage(request):
    userdata = tbl_userregistration.objects.get(id=request.session["uid"]) 
    return render(request,"User/Homepage.html",{'userdata':userdata})

def myprofile(request):
    userdata = tbl_userregistration.objects.get(id=request.session["uid"])  
    return render(request,"User/MyProfile.html",{'userdata':userdata})  

def editprofile(request):
    userdata = tbl_userregistration.objects.get(id=request.session["uid"]) 
    if request.method == "POST":
        userdata.user_name=request.POST.get('txtuser')
        userdata.user_contact=int(request.POST.get('txtcontact'))
        userdata.user_email=request.POST.get('txtemail')
        userdata.user_address=request.POST.get('txtaddress')
        userdata.save()
        return redirect("webuser:MyProfile")
    else:
        return render(request,"User/EditProfile.html",{'userdata':userdata})
    
def changepassword(request):
    userdata=tbl_userregistration.objects.get(id=request.session["uid"])
    password=userdata.user_password
    currentpassword=request.POST.get('txtpassword')
    newpassword=request.POST.get('txtnewpassword')
    confirmpassword=request.POST.get('txtcpassword')
        # userdata.user_password=request.POST.get('txtpassword')
    if currentpassword==password:
        if newpassword==confirmpassword:
            if request.method == "POST":
                userdata.user_password=confirmpassword
                userdata.save()
                return redirect("webguest:Login")
            else:
                return redirect("webuser:ChangePassword")
        else:
            return redirect("webuser:ChangePassword")
        
    else:
        return render(request,"User/Changepassword.html",{"userdata":userdata})    
    
def userfeedback(request):
    feed = tbl_feedback.objects.filter(user_id=request.session.get("uid"))
    if request.method=="POST":
        description=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_description=description,user_id=tbl_userregistration.objects.get(id=request.session["uid"]))
        return render(request,"User/SendFeedback.html",{'data':feed})
    else:
        return render(request,"User/SendFeedback.html",{'data':feed})
    
def deleteuserfeedback(request,id):
    tbl_feedback.objects.get(id=id).delete()
    return redirect("webuser:SendFeedback")     
    
def usercomplaint(request):
    comp = tbl_complaint.objects.filter(user_id=request.session.get("uid"))
    if request.method=="POST":
        title=request.POST.get('txttitle')
        description=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_description=description,user_id=tbl_userregistration.objects.get(id=request.session["uid"]))
        return render(request,"User/SendComplaint.html",{'data':comp})
    else:
        return render(request,"User/SendComplaint.html",{'data':comp})    
    
def deleteusercomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("webuser:SendComplaint")     

def searchphotographer(request):
    photographercategory = tbl_pcategory.objects.all()
    photographer = tbl_photographerregistration.objects.filter(photographer_status=1)
    return render(request, "User/SearchPhotographer.html", {'photographercategory': photographercategory,'photographer': photographer})

def ajaxphotographer(request):
    if request.GET.get("cid")!="":
        category = tbl_pcategory.objects.get(id=request.GET.get("cid"))
        photographer = tbl_photographerregistration.objects.filter(photographer_category=category)
        return render(request,"User/AjaxPhotographer.html",{"photographer":photographer})
    else:
        return render(request,"User/AjaxPhotographer.html")
    
# def viewpost(request,id):
#     postdata=tbl_post.objects.get(id=id)
#     return render(request,"User/ViewPost.html",{'postdata':postdata})       
    
def viewgallery(request,id):
    postdata=tbl_post.objects.get(id=id)
    viewgallerydata=tbl_addgallery.objects.filter(post_id=postdata)
    return render(request,"User/ViewGallery.html",{'postdata':postdata,'viewgallerydata':viewgallerydata})    
    
def photographerbooking(request,pid):
    photographerdata=tbl_photographerregistration.objects.get(id=pid)
    userdata=tbl_userregistration.objects.get(id=request.session["uid"])
    if request.method=="POST":
        tbl_photographerbooking.objects.create(booking_date=request.POST.get("for_date"),
                                               pbooking_description=request.POST.get("txtdescription"),
                                               photographer_id=photographerdata,
                                               user_id=userdata)
        return redirect("webuser:SearchPhotographer")
    else:
        return render(request,"User/PhotographerBooking.html")
    
def viewphotographerbooking(request):
    photographerdata=tbl_photographerregistration.objects.all()
    bookingdata=tbl_photographerbooking.objects.all()
    return render(request, "User/ViewMyPhotographerBooking.html", {'photographerdata': photographerdata, 'bookingdata': bookingdata})

def photographerpayment(request,id):
    bookingdata=tbl_photographerbooking.objects.get(id=id)
    if request.method=="POST":
        bookingdata.pbooking_vstatus=3
        bookingdata.save()
        return redirect("webuser:ViewPhotographerBooking")
    else:
        return render(request,"User/Payment.html",{'bookingdata':bookingdata})
    
#############################################################################################
    
def chatpage(request,id):
    user  = tbl_photographerregistration.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_userregistration.objects.get(id=request.session["uid"])
    to_user = tbl_photographerregistration.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,photographer_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_userregistration.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(photographer_from=tid) | Q(photographer_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(photographer_to=request.GET.get("tid")) | (Q(photographer_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

################################################################################################

def viewpost(request,id):
    post = tbl_post.objects.get(id=id)
    like = tbl_like.objects.filter(post=post).count()
    condotion = 0
    if like > 0:
        condition = 1
    else:
        condition = 0
    return render(request,"User/ViewPost.html",{"postdata":post,"count":like,"condition":condition})

def ajaxlike(request):
    likecount = tbl_like.objects.filter(user=request.session["uid"],post=request.GET.get("postid")).count()
    if likecount > 0:
        tbl_like.objects.get(user=request.session["uid"],post=request.GET.get("postid")).delete()
        count = tbl_like.objects.filter(user=request.session["uid"],post=request.GET.get("postid")).count()
        return JsonResponse({"color":1,"count":count})
    else:
        tbl_like.objects.create(user=tbl_userregistration.objects.get(id=request.session["uid"]),post=tbl_post.objects.get(id=request.GET.get("postid")))
        count = tbl_like.objects.filter(user=request.session["uid"],post=request.GET.get("postid")).count()
        return JsonResponse({"color":0,"count":count})

def ajaxcomment(request):
    tbl_commant.objects.create(user=tbl_userregistration.objects.get(id=request.session["uid"]),post=tbl_post.objects.get(id=request.GET.get("postid")),comment_content=request.GET.get("content"))
    comment = tbl_commant.objects.filter(post=request.GET.get("postid"))
    return render(request,"User/AjaxComment.html",{"comment":comment})

def ajaxgetcommant(request):
    comment = tbl_commant.objects.filter(post=request.GET.get("postid"))
    return render(request,"User/AjaxComment.html",{"comment":comment})
