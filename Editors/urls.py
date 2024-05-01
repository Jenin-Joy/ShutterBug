from django.contrib import admin
from django.urls import path,include
from Editors import views
app_name="webeditor"

urlpatterns = [
    path('Homepage/',views.homepage,name="Homepage"),
    
    path('MyProfile/', views.myprofile,name="MyProfile"),
    path('EditProfile/',views.editprofile,name="EditProfile"),
    path('ChangePassword/',views.changepassword,name="ChangePassword"),

    path('Post/',views.post,name="Post"),
    path('DeletePost/<int:pid>',views.deletepost,name="DeletePost"),
    # path('EditPost/<int:id>',views.editpost,name="EditPost"), 
     
    path('AddGallery/<int:id>',views.editoraddgallery,name="AddGallery"),
    path('DeleteGallery/<int:id>',views.editordeletegallery,name="DeleteGallery"),
    # path('EditGallery/<int:id>',views.editgallery,name="EditGallery"),

    path('SendComplaint/', views.editorcomplaint,name="SendComplaint"),
    path('DeleteComplaint/<int:id>', views.deleteeditorcomplaint,name="DeleteComplaint"),

    path('SendFeedback/', views.editorfeedback,name="SendFeedback"),
    path('DeleteFeedback/<int:id>', views.deleteeditorfeedback,name="DeleteFeedback"),

    path('ViewPhotographerBooking/',views.viewphotographerbooking,name="ViewPhotographerBooking"),
    path('AcceptPhotographer/<int:id>',views.acceptphotographerbooking,name="AcceptPhotographer"),  
    path('RejectPhotographer/<int:id>',views.rejectphotographerbooking,name="RejectPhotographer"),     
    path('AcceptedPhotographer/',views.acceptedphotographerbooking,name="AcceptedPhotographer"),  
    path('RejectedPhotographer/',views.rejectedphotographerbooking,name="RejectedPhotographer"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

]    