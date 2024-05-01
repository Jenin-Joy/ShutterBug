from django.contrib import admin
from django.urls import path,include
from Admin import views
app_name="webadmin"

urlpatterns = [
    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('Deletedistrict/<int:did>',views.deletedistrict,name="DeleteDistrict"),
    path('EditDistrict/<int:id>',views.editdistrict,name="EditDistrict"),

    path('Category/', views.categoryInsertSelect,name="categoryInsertSelect"),
    path('Deletecategory/<int:cid>',views.deletecategory,name="DeleteCategory"),
    path('EditCategory/<int:id>',views.editcategory,name="EditCategory"),

    path('Subcategory/', views.subInsertSelect,name="subInsertSelect"),
    path('Deletesubcategory/<int:sid>',views.deletesubcategory,name="DeleteSubcategory"),
    path('EditSubcategory/<int:id>',views.editsubcategory,name="EditSubcategory"),

    path('PhotographerCategory/', views.photographercategory,name="PhotographerCategory"),
    path('DeletePhotographerCategory/<int:id>',views.deletephotographercategory,name="DeletePhotographerCategory"),
    path('EditPhotographerCategory/<int:id>',views.editphotographercategory,name="EditPhotographerCategory"),

    path('EditorCategory/', views.editorcategory,name="EditorCategory"),
    path('DeleteEditorCategory/<int:id>',views.deleteeditorcategory,name="DeleteEditorCategory"),
    path('EditEditorCategory/<int:id>',views.editeditorcategory,name="EditEditorCategory"),

    path('Admin/', views.adminInsertSelect,name="adminInsertSelect"),

    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('Deleteplace/<int:pid>',views.deleteplace,name="DeletePlace"),
    path('editplace/<int:id>',views.editplace,name="editplace"),

    path('PhotographerCategory/', views.photographercategory,name="PhotographerCategory"),
    path('DeletePhotographerCategory/<int:pid>',views.deletephotographercategory,name="DeletePhotographerCategory"),
    path('EditPhotographerCategory/<int:id>',views.editphotographercategory,name="EditPhotographerCategory"),

    path('EditorCategory/', views.editorcategory,name="EditorCategory"),
    path('DeleteEditorCategory/<int:eid>',views.deleteeditorcategory,name="DeleteEditorCategory"),
    path('EditEditorCategory/<int:id>',views.editeditorcategory,name="EditEditorCategory"), 

    path('EditorVerification/',views.verifyeditor,name="EditorVerification"), 
    path('AcceptEditor/<int:id>',views.accepteditor,name="AcceptEditor"),  
    path('RejectEditor/<int:id>',views.rejecteditor,name="RejectEditor"),     
    path('AcceptedEditor/',views.acceptededitor,name="AcceptedEditor"),  
    path('RejectedEditor/',views.rejectededitor,name="RejectedEditor"),

    path('ModelVerification/',views.verifymodel,name="ModelVerification"), 
    path('AcceptModel/<int:id>',views.acceptmodel,name="AcceptModel"),  
    path('RejectModel/<int:id>',views.rejectmodel,name="RejectModel"),     
    path('AcceptedModel/',views.acceptedmodel,name="AcceptedModel"),  
    path('RejectedModel/',views.rejectedmodel,name="RejectedModel"),
    
    path('PhotographerVerification/',views.verifyphotographer,name="PhotographerVerification"), 
    path('AcceptPhotographer/<int:id>',views.acceptphotographer,name="AcceptPhotographer"),  
    path('RejectPhotographer/<int:id>',views.rejectphotographer,name="RejectPhotographer"),     
    path('AcceptedPhotographer/',views.acceptedphotographer,name="AcceptedPhotographer"),  
    path('RejectedPhotographer/',views.rejectedphotographer,name="RejectedPhotographer"),

    path('ViewFeedback/',views.viewfeedback,name="ViewFeedback"),
    path('ViewPhotographerFeedback/',views.viewpfeedback,name="ViewPhotographerFeedback"),
    path('ViewEditorFeedback/',views.viewefeedback,name="ViewEditorFeedback"),
    path('ViewModelFeedback/',views.viewmfeedback,name="ViewModelFeedback"),

    path('ViewComplaint/',views.viewcomplaint,name="ViewComplaint"),
    path('ViewPhotographerComplaint/',views.viewpcomplaint,name="ViewPhotographerComplaint"),
    path('ViewEditorComplaint/',views.viewecomplaint,name="ViewEditorComplaint"),
    path('ViewModelComplaint/',views.viewmcomplaint,name="ViewModelComplaint"),

    path('RepliedComplaint/',views.repliedcomplaint,name="RepliedComplaint"),
    path('RepliedPhotographerComplaint/',views.repliedpcomplaint,name="RepliedPhotographerComplaint"),
    path('RepliedEditorComplaint/',views.repliedecomplaint,name="RepliedEditorComplaint"),
    path('RepliedModelComplaint/',views.repliedmcomplaint,name="RepliedModelComplaint"),

    path('Homepage/',views.homepage,name="Homepage"),

    path('index/',views.index,name="index"),

    path('Reply/<int:id>',views.reply,name="Reply"),



]