from django.contrib import admin
from django.urls import path,include
from Photographers import views
app_name="webphotographer"

urlpatterns = [
    path('Homepage/',views.homepage,name="Homepage"),
    
    path('MyProfile/', views.myprofile,name="MyProfile"),
    path('EditProfile/',views.editprofile,name="EditProfile"),
    path('ChangePassword/',views.changepassword,name="ChangePassword"),
    
    path('Post/',views.post,name="Post"),
    path('DeletePost/<int:pid>',views.deletepost,name="DeletePost"),
    # path('EditPost/<int:id>',views.editpost,name="EditPost"),  

    path('AddGallery/<int:id>',views.photographeraddgallery,name="AddGallery"),
    path('DeleteGallery/<int:id>',views.photographerdeletegallery,name="DeleteGallery"),
    # path('EditGallery/<int:id>',views.editgallery,name="EditGallery"), 

    path('MyProfile/', views.myprofile,name="MyProfile"),

    path('SendComplaint/', views.photographercomplaint,name="SendComplaint"),
    path('DeleteComplaint/<int:id>', views.deletephotographercomplaint,name="DeleteComplaint"),

    path('SendFeedback/', views.photographerfeedback,name="SendFeedback"),
    path('DeleteFeedback/<int:id>', views.deletephotographerfeedback,name="DeleteFeedback"),

    path('SearchEditor/', views.searcheditor,name="SearchEditor"),
    path('ajaxeditor/',views.ajaxeditor,name="ajaxeditor"),
    path('EditorBooking/<int:did>',views.editorbooking,name="EditorBooking"),
    path('ViewEditorBooking/',views.vieweditorbooking,name="ViewEditorBooking"),

    path('SearchModel/', views.searchmodel,name="SearchModel"),
    path('ajaxmodel/',views.ajaxmodel,name="ajaxmodel"),
    path('ModelBooking/<int:mid>',views.modelbooking,name="ModelBooking"),
    path('ViewModelBooking/',views.viewmodelbooking,name="ViewModelBooking"),

    path('ViewUserBooking/',views.viewuserbooking,name="ViewUserBooking"),

    path('EditorViewMore/<int:id>', views.editorviewmore,name="EditorViewMore"),
    path('EditorViewPost/<int:id>', views.editorviewpost,name="EditorViewPost"),

    path('ViewModelPost/<int:id>', views.modelviewpost,name="ViewModelPost"),
    path('ModelViewMore/<int:id>', views.modelviewmore,name="ModelViewMore"),

    # path('UserVerification/',views.verifyuserbooking,name="UserVerification"), 
    path('AcceptUser/<int:id>',views.acceptuserbooking,name="AcceptUser"),  
    path('RejectUser/<int:id>',views.rejectuserbooking,name="RejectUser"),     
    path('AcceptedUser/',views.accepteduserbooking,name="AcceptedUser"),  
    path('RejectedUser/',views.rejecteduserbooking,name="RejectedUser"),

    path('EPayment/<int:id>',views.editorpayment,name="EPayment"),
    path('MPayment/<int:id>',views.modelpayment,name="MPayment"),


    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('editorchatpage/<int:id>',views.editorchatpage,name="editorchatpage"),
    path('editorajaxchat/',views.editorajaxchat,name="editorajaxchat"),
    path('editorajaxchatview/',views.editorajaxchatview,name="editorajaxchatview"),
    path('editorclearchat/',views.editorclearchat,name="editorclearchat"),
]    