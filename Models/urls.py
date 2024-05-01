from django.contrib import admin
from django.urls import path,include
from Models import views
app_name="webmodel"

urlpatterns = [
    
    path('Homepage/', views.homepage,name="Homepage"),
    
    path('MyProfile/', views.myprofile,name="MyProfile"),
    path('EditProfile/',views.editprofile,name="EditProfile"),
    path('ChangePassword/',views.changepassword,name="ChangePassword"),

    path('ModelPost/',views.modelpost,name="ModelPost"),
    path('DeleteModelPost/<int:id>',views.deletemodelpost,name="DeleteModelPost"),

    path('ModelPic/<int:id>',views.modelpic,name="ModelPic"),
    path('DeleteModelPic/<int:id>',views.deletemodelpic,name="DeleteModelPic"),

    path('SendComplaint/', views.modelcomplaint,name="SendComplaint"),
    path('DeleteComplaint/<int:id>', views.deletemodelcomplaint,name="DeleteComplaint"),

    path('SendFeedback/', views.modelfeedback,name="SendFeedback"),
    path('DeleteFeedback/<int:id>', views.deletemodelfeedback,name="DeleteFeedback"),

    path('ViewPhotographerBooking/',views.viewphotographerbooking,name="ViewPhotographerBooking"),

    # path('PhotographerVerification/',views.verifyphotographerbooking,name="PhotographerVerification"), 
    path('AcceptPhotographer/<int:id>',views.acceptphotographerbooking,name="AcceptPhotographer"),  
    path('RejectPhotographer/<int:id>',views.rejectphotographerbooking,name="RejectPhotographer"),     
    path('AcceptedPhotographer/',views.acceptedphotographerbooking,name="AcceptedPhotographer"),  
    path('RejectedPhotographer/',views.rejectedphotographerbooking,name="RejectedPhotographer"),
    
]