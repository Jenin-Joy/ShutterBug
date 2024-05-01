from django.contrib import admin
from django.urls import path,include
from User import views
app_name="webuser"

urlpatterns = [
    
    path('Homepage/', views.homepage,name="Homepage"),

    path('MyProfile/', views.myprofile,name="MyProfile"),
    path('EditProfile/', views.editprofile,name="EditProfile"),
    path('ChangePassword/', views.changepassword,name="ChangePassword"),

    path('SendFeedback/', views.userfeedback,name="SendFeedback"),
    path('DeleteFeedback/<int:id>', views.deleteuserfeedback,name="DeleteFeedback"),

    path('SendComplaint/', views.usercomplaint,name="SendComplaint"),
    path('DeleteComplaint/<int:id>', views.deleteusercomplaint,name="DeleteComplaint"),

    path('SearchPhotographer/', views.searchphotographer,name="SearchPhotographer"),
    path('ajaxphotographer/',views.ajaxphotographer,name="ajaxphotographer"),

    path('PhotographerBooking/<int:pid>',views.photographerbooking,name="PhotographerBooking"),
    path('ViewPhotographerBooking/',views.viewphotographerbooking,name="ViewPhotographerBooking"),

    path('ViewGallery/<int:id>', views.viewgallery,name="ViewGallery"),
    path('ViewPost/<int:id>', views.viewpost,name="ViewPost"),

    path('Payment/<int:id>',views.photographerpayment,name="Payment"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    # path('Post/',views.post,name="post"),
    path('ajaxlike/',views.ajaxlike,name="ajaxlike"),
    path('ajaxcomment/',views.ajaxcomment,name="ajaxcomment"),
    path('ajaxgetcommant/',views.ajaxgetcommant,name="ajaxgetcommant"),
]