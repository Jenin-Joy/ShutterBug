from django.shortcuts import render,redirect
from .models import *
from Guest.models import *
from User.models import *

# Create your views here.

def homepage(request):
    admindata=tbl_admin.objects.get(id=request.session["aid"])
    total_users = tbl_userregistration.objects.count()
    users = tbl_userregistration.objects.all()
    total_photographers = tbl_photographerregistration.objects.count()
    photographers = tbl_photographerregistration.objects.all()
    total_editors = tbl_editorregistration.objects.count()
    editors = tbl_editorregistration.objects.all()
    total_models = tbl_modelregistration.objects.count()
    models = tbl_modelregistration.objects.all()
    return render(request, "Admin/Homepage.html",{'admindata':admindata,'total_users': total_users,'users':users,'total_photographers': total_photographers,'photographers':photographers,'total_editors': total_editors,'editors':editors,'total_models': total_models,'models': models})

def index(request):
    return render(request,"Admin/index.html")

def districtInsertSelect(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtdistrict')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Admin/District.html",{'data':dis})
    else:
        return render(request,"Admin/District.html",{'data':dis})

def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("webadmin:districtInsertSelect")

def editdistrict(request,id):
    dis=tbl_district.objects.get(id=id)
    if request.method == "POST":
        dis.district_name=request.POST.get('txtdistrict')
        dis.save()
        return redirect("webadmin:districtInsertSelect")
    else:
        return render(request,"Admin/District.html",{'dis':dis})


def categoryInsertSelect(request):
    cat=tbl_category.objects.all()
    if request.method=="POST":
        cisName=request.POST.get('txtcategory')
        tbl_category.objects.create(category_name=cisName)
        return render(request,"Admin/Category.html",{'data':cat})
    else:
        return render(request,"Admin/Category.html",{'data':cat})
    
def deletecategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("webadmin:categoryInsertSelect")    

def editcategory(request,id):
    cat=tbl_category.objects.get(id=id)
    if request.method == "POST":
        cat.category_name=request.POST.get('txtcategory')
        cat.save()
        return redirect("webadmin:categoryInsertSelect")
    else:
        return render(request,"Admin/Category.html",{'cat':cat})
    
def adminInsertSelect(request):
    adm=tbl_admin.objects.all()
    if request.method=="POST":
        admName=request.POST.get('txtname')
        admContact=request.POST.get('txtcontact')
        admEmail=request.POST.get('txtemail')
        admPassword=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=admName,admin_contact=admContact,admin_email=admEmail,admin_password=admPassword)
        return render(request,"Admin/AdminRegistration.html",{'data':adm})
    else:
        return render(request,"Admin/AdminRegistration.html",{'data':adm})
    
def placeInsertSelect(request):
    dis=tbl_district.objects.all()
    pla=tbl_place.objects.all()
    if request.method=="POST":
        disId=tbl_district.objects.get(id=request.POST.get('txtdistrict'))
        plaName=request.POST.get('txtplace')
        tbl_place.objects.create(district_id=disId,place_name=plaName)
        return render(request,"Admin/Place.html",{'pla':pla,'dis':dis})
    else:
        return render(request,"Admin/Place.html",{'pla':pla,'dis':dis})    
    
def deleteplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect("webadmin:placeInsertSelect")  

def editplace(request,id):
    dis=tbl_district.objects.all()
    pla=tbl_place.objects.get(id=id) 
    if request.method == "POST":
        pla.place_name=request.POST.get('txtplace')
        disId=tbl_district.objects.get(id=request.POST.get('txtdistrict'))
        pla.district_id = disId
        pla.save()
        return redirect("webadmin:placeInsertSelect")
    else:
        return render(request,"Admin/Place.html",{'place':pla,'dis':dis})
    
def subInsertSelect(request):
    cat=tbl_category.objects.all()
    sub=tbl_subcategory.objects.all()
    if request.method=="POST":
        cisId=tbl_category.objects.get(id=request.POST.get('txtcategory'))
        subName=request.POST.get('txtsubcategory')
        tbl_subcategory.objects.create(category_id=cisId,subcategory_name=subName)
        return render(request,"Admin/Subcategory.html",{'sub':sub,'cat':cat})
    else:
        return render(request,"Admin/Subcategory.html",{'sub':sub,'cat':cat})     
    
def deletesubcategory(request,sid):
    tbl_subcategory.objects.get(id=sid).delete()
    return redirect("webadmin:subInsertSelect")    

def editsubcategory(request,id):
    cat=tbl_category.objects.all()
    sub=tbl_subcategory.objects.get(id=id) 
    if request.method == "POST":
        sub.subcategory_name=request.POST.get('txtsubcategory')
        catId=tbl_category.objects.get(id=request.POST.get('txtcategory'))
        sub.category_id = catId
        sub.save()
        return redirect("webadmin:subInsertSelect")
    else:
        return render(request,"Admin/Subcategory.html",{'cat':cat,'subcategory':sub})
    
def photographercategory(request):
    pcat=tbl_pcategory.objects.all()
    if request.method=="POST":
        pcatName=request.POST.get('txtpcategory')
        tbl_pcategory.objects.create(pcategory_name=pcatName)
        return render(request,"Admin/PhotographerCategory.html",{'data':pcat})
    else:
        return render(request,"Admin/PhotographerCategory.html",{'data':pcat})    
    
def deletephotographercategory(request,id):
    tbl_pcategory.objects.get(id=id).delete()
    return redirect("webadmin:PhotographerCategory")    

def editphotographercategory(request,id):
    pcat=tbl_pcategory.objects.get(id=id)
    if request.method == "POST":
        pcat.pcategory_name=request.POST.get('txtpcategory')
        pcat.save()
        return redirect("webadmin:PhotographerCategory")
    else:
        return render(request,"Admin/PhotographerCategory.html",{'pcat':pcat})    
    
def editorcategory(request):
    ecat=tbl_ecategory.objects.all()
    if request.method=="POST":
        ecatName=request.POST.get('txtecategory')
        tbl_ecategory.objects.create(ecategory_name=ecatName)
        return render(request,"Admin/EditorCategory.html",{'data':ecat})
    else:
        return render(request,"Admin/EditorCategory.html",{'data':ecat})    
    
def deleteeditorcategory(request,id):
    tbl_ecategory.objects.get(id=id).delete()
    return redirect("webadmin:EditorCategory")    

def editeditorcategory(request,id):
    ecat=tbl_ecategory.objects.get(id=id)
    if request.method == "POST":
        ecat.ecategory_name=request.POST.get('txtecategory')
        ecat.save()
        return redirect("webadmin:EditorCategory")
    else:
        return render(request,"Admin/EditorCategory.html",{'ecat':ecat})   

def verifyeditor(request):
    editordata = tbl_editorregistration.objects.filter(editor_status='0')
    # placedata=tbl_place.objects.all()
    
    return render(request, "Admin/EditorVerification.html", {'editordata': editordata})

def accepteditor(request,id):
    edit = tbl_editorregistration.objects.get(id=id)
    edit.editor_status = "1"
    edit.save()
    return redirect("webadmin:EditorVerification")  

def rejecteditor(request,id):
    edit = tbl_editorregistration.objects.get(id=id)
    edit.editor_status = "2"
    edit.save()
    return redirect("webadmin:EditorVerification")  

def acceptededitor(request):
    editordata = tbl_editorregistration.objects.filter(editor_status='1')
    # placedata=tbl_place.objects.all()
    
    return render(request, "Admin/AcceptedEditor.html", {'editordata': editordata})

def rejectededitor(request):
    editordata = tbl_editorregistration.objects.filter(editor_status='2')
    # placedata=tbl_place.objects.all()
    
    return render(request, "Admin/RejectedEditor.html", {'editordata': editordata}) 

def verifymodel(request):
    disdata = tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    modeldata = tbl_modelregistration.objects.filter(model_status='0')
    
    return render(request, "Admin/ModelVerification.html", {'modeldata': modeldata,'disdata': disdata,'placedata': placedata})

def acceptmodel(request,id):
    mod = tbl_modelregistration.objects.get(id=id)
    mod.model_status = "1"
    mod.save()
    return redirect("webadmin:ModelVerification")  

def rejectmodel(request,id):
    mod = tbl_modelregistration.objects.get(id=id)
    mod.model_status = "2"
    mod.save()
    return redirect("webadmin:ModelVerification")  

def acceptedmodel(request):
    disdata = tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    modeldata = tbl_modelregistration.objects.filter(model_status='1')
    
    return render(request, "Admin/AcceptedModel.html", {'modeldata': modeldata,'disdata': disdata,'placedata': placedata})

def rejectedmodel(request):
    disdata = tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    modeldata = tbl_modelregistration.objects.filter(model_status='2')
    
    return render(request, "Admin/RejectedModel.html",{'modeldata': modeldata,'disdata': disdata,'placedata': placedata})  

def verifyphotographer(request):
    categorydata = tbl_pcategory.objects.all()
    photographerdata = tbl_photographerregistration.objects.filter(photographer_status='0')
    # placedata=tbl_place.objects.all()
    return render(request, "Admin/PhotographerVerification.html", {'photographerdata': photographerdata,'categorydata': categorydata})

def acceptphotographer(request,id):
    pho = tbl_photographerregistration.objects.get(id=id)
    pho.photographer_status = "1"
    pho.save()
    return redirect("webadmin:PhotographerVerification")  

def rejectphotographer(request,id):
    pho = tbl_photographerregistration.objects.get(id=id)
    pho.photographer_status = "2"
    pho.save()
    return redirect("webadmin:PhotographerVerification")  

def acceptedphotographer(request):
    photographerdata = tbl_photographerregistration.objects.filter(photographer_status='1')
    # placedata=tbl_place.objects.all()
    
    return render(request, "Admin/AcceptedPhotographer.html", {'photographerdata': photographerdata})

def rejectedphotographer(request):
    photographerdata = tbl_photographerregistration.objects.filter(photographer_status='2')
    # placedata=tbl_place.objects.all()
    
    return render(request, "Admin/RejectedPhotographer.html", {'photographerdata': photographerdata})   

def viewfeedback(request):
    # Get all feedback
    all_feedback = tbl_feedback.objects.all()
    # Filter user data
    userdata = tbl_userregistration.objects.all()
    
    if request.method=="POST":
        # Retrieve form data
        description = request.POST.get('txtfeedback')
        username = tbl_userregistration.objects.get(id=request.POST.get('txtusername'))
        email = tbl_userregistration.objects.get(id=request.POST.get('txtemail'))
        # Create new feedback object
        tbl_feedback.objects.create(
            feedback_description=description,
            user_username=username,
            user_email=email,
            user_id=tbl_userregistration.objects.get(id=request.session["uid"])
        )
        # Redirect to viewfeedback page after adding feedback
        return redirect("viewfeedback")
    else:
        # Filter feedback by users
        user_feedback = tbl_feedback.objects.filter(user_id__in=userdata)
        return render(request, "Admin/ViewFeedback.html", {'data': user_feedback, 'userdata': userdata})
 
    
def viewpfeedback(request):
    # Get all feedback
    all_feedback = tbl_feedback.objects.all()
    # Filter photographer data
    photographerdata = tbl_photographerregistration.objects.all()
    
    if request.method == "POST":
        # Retrieve form data
        description = request.POST.get('txtfeedback')
        username = tbl_photographerregistration.objects.get(id=request.POST.get('txtusername'))
        email = tbl_photographerregistration.objects.get(id=request.POST.get('txtemail'))
        # Create new feedback object
        tbl_feedback.objects.create(
            feedback_description=description,
            photographer_username=username,
            photographer_email=email,
            photographer_id=tbl_photographerregistration.objects.get(id=request.session["pid"])
        )
        # Redirect to viewpfeedback page after adding feedback
        return redirect("viewpfeedback")
    else:
        # Filter feedback by photographers
        photographer_feedback = tbl_feedback.objects.filter(photographer_id__in=photographerdata)
        return render(request, "Admin/ViewPhotographerFeedback.html", {'data': photographer_feedback, 'photographerdata': photographerdata})

def viewefeedback(request):
    # Get all feedback
    all_feedback = tbl_feedback.objects.all()
    # Filter photographer data
    editordata = tbl_editorregistration.objects.all()
    
    if request.method == "POST":
        # Retrieve form data
        description = request.POST.get('txtfeedback')
        username = tbl_editorregistration.objects.get(id=request.POST.get('txtusername'))
        email = tbl_editorregistration.objects.get(id=request.POST.get('txtemail'))
        # Create new feedback object
        tbl_feedback.objects.create(
            feedback_description=description,
            editor_username=username,
            editor_email=email,
            editor_id=tbl_editorregistration.objects.get(id=request.session["did"])
        )
        # Redirect to viewpfeedback page after adding feedback
        return redirect("viewefeedback")
    else:
        # Filter feedback by photographers
        editor_feedback = tbl_feedback.objects.filter(editor_id__in=editordata)
        return render(request, "Admin/ViewEditorFeedback.html", {'data': editor_feedback, 'editordata': editordata})
    
def viewmfeedback(request):
    # Get all feedback
    all_feedback = tbl_feedback.objects.all()
    # Filter photographer data
    modeldata = tbl_modelregistration.objects.all()
    
    if request.method == "POST":
        # Retrieve form data
        description = request.POST.get('txtfeedback')
        username = tbl_modelregistration.objects.get(id=request.POST.get('txtusername'))
        email = tbl_modelregistration.objects.get(id=request.POST.get('txtemail'))
        # Create new feedback object
        tbl_feedback.objects.create(
            feedback_description=description,
            model_username=username,
            model_email=email,
            model_id=tbl_modelregistration.objects.get(id=request.session["mid"])
        )
        # Redirect to viewpfeedback page after adding feedback
        return redirect("viewmfeedback")
    else:
        # Filter feedback by photographers
        model_feedback = tbl_feedback.objects.filter(model_id__in=modeldata)
        return render(request, "Admin/ViewModelFeedback.html", {'data': model_feedback, 'modeldata': modeldata})    


    
# def viewcomplaint(request):
#     photographercomp = tbl_complaint.objects.filter(user_id=None,editor_id=None,model_id=None)
#     usercomp = tbl_complaint.objects.filter(photographer_id=None,editor_id=None,model_id=None)
#     editorcomp = tbl_complaint.objects.filter(user_id=None,photographer_id=None,model_id=None)
#     modelcomp = tbl_complaint.objects.filter(user_id=None,editor_id=None,photographer_id=None)
#     userdata = tbl_userregistration.objects.all()
#     editordata = tbl_editorregistration.objects.all()
#     photographerdata = tbl_photographerregistration.objects.all()
#     modeldata = tbl_modelregistration.objects.all()

#     return render(request,"Admin/ViewComplaint.html",{'photographercomp':photographercomp,'usercomp':usercomp,'editorcomp':editorcomp,'modelcomp':modelcomp,'userdata':userdata,'editordata':editordata,'photographerdata':photographerdata,'modeldata':modeldata})    

def viewcomplaint(request):
    userdata = tbl_userregistration.objects.all()
    usercomplaintdata = tbl_complaint.objects.filter(user_id__in=userdata, complaint_status=0)
    return render(request, "Admin/ViewComplaint.html", {'usercomplaintdata': usercomplaintdata})

def viewpcomplaint(request):
    photographerdata = tbl_photographerregistration.objects.all()
    photographercomplaintdata = tbl_complaint.objects.filter(photographer_id__in=photographerdata, complaint_status=0)
    return render(request, "Admin/ViewPhotographerComplaint.html", {'photographercomplaintdata': photographercomplaintdata})

def viewecomplaint(request):
    editordata = tbl_editorregistration.objects.all()
    editorcomplaintdata = tbl_complaint.objects.filter(editor_id__in=editordata, complaint_status=0)
    return render(request, "Admin/ViewEditorComplaint.html", {'editorcomplaintdata': editorcomplaintdata})

def viewmcomplaint(request):
    modeldata = tbl_modelregistration.objects.all()
    modelcomplaintdata = tbl_complaint.objects.filter(model_id__in=modeldata, complaint_status=0)
    return render(request, "Admin/ViewModelComplaint.html", {'modelcomplaintdata': modelcomplaintdata})
    
def reply(request,id):
    admindata=tbl_admin.objects.get(id=request.session["aid"])
    complaintdata = tbl_complaint.objects.get(id=id,complaint_status=0)
    if request.method=="POST":
        complaintdata.complaint_reply=request.POST.get('txtreply')
        complaintdata.complaint_status = 1
        complaintdata.save()
        return render(request,"Admin/Reply.html",{'complaintdata':complaintdata}) 
    else:
        return render(request,"Admin/Reply.html",{'complaintdata':complaintdata,'admindata':admindata})
    
def repliedcomplaint(request):
    admindata=tbl_admin.objects.get(id=request.session["aid"])
    userdata=tbl_userregistration.objects.all()
    usercomplaintdata=tbl_complaint.objects.filter(user_id__in=userdata,complaint_status=1) 
    return render(request, "Admin/RepliedComplaint.html", {'userdata': userdata,'admindata':admindata,'usercomplaintdata':usercomplaintdata})  

def repliedecomplaint(request):
    admindata=tbl_admin.objects.get(id=request.session["aid"])
    editordata=tbl_editorregistration.objects.all()
    editorcomplaintdata=tbl_complaint.objects.filter(editor_id__in=editordata,complaint_status=1) 
    return render(request, "Admin/RepliedEditorComplaint.html", {'editordata': editordata,'admindata':admindata,'editorcomplaintdata':editorcomplaintdata}) 

def repliedpcomplaint(request):
    admindata=tbl_admin.objects.get(id=request.session["aid"])
    photographerdata=tbl_photographerregistration.objects.all()
    photographercomplaintdata=tbl_complaint.objects.filter(photographer_id__in=photographerdata,complaint_status=1) 
    return render(request, "Admin/RepliedPhotographerComplaint.html", {'photographerdata': photographerdata,'admindata':admindata,'photographercomplaintdata':photographercomplaintdata})

def repliedmcomplaint(request):
    admindata=tbl_admin.objects.get(id=request.session["aid"])
    modeldata=tbl_modelregistration.objects.all()
    modelcomplaintdata=tbl_complaint.objects.filter(model_id__in=modeldata,complaint_status=1) 
    return render(request, "Admin/RepliedModelComplaint.html", {'modeldata': modeldata,'admindata':admindata,'modelcomplaintdata':modelcomplaintdata})  