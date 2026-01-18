from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.GetHomePage),
    #Questions
     path('getaddquespage/',views.getaddquespage),
     path('getdeletequespage/',views.getdeletequespage),
     path('getshowallquespage/',views.getshowallquespage),
     path('getupdatequespage/',views.getupdatequespage),
     path('getcurdquespage/',views.getcurdquespage),

     path('add_ques/',views.add_ques),
     # path('delete_ques/<int:id>/',views.delete_ques , name='delete_ques'),
     path('showall_ques/',views.showall_ques, name='showall_ques'),
     path('update_updatepage/',views.update_updatepage),
     path('show_updatepage/',views.show_updatepage),
     path('show_deletepage/',views.show_deletepage),
     path('delete_deletepage/',views.delete_deletepage),
     path('add_curd/',views.add_curd),
     path('delete_curd/',views.delete_curd),
     path('update_curd/',views.update_curd),
     path('show_curd/',views.show_curd),

     #Stydent
     path('getaddstudpage/',views.getaddstudpage),
     path('getdeletestudpage/',views.getdeletestudpage),
     path('getshowallstudpage/', views.getshowallstudpage, name='getshowallstudpage'),  #not working
     path('getupdatestudpage/',views.getupdatestudpage),
     path('getcurdstudpage/',views.getcurdstudpage),
     path('GiveMeLoginPage/',views.GiveMeLoginPage),
     path('GiveMeRegisterPage/',views.GiveMeRegisterPage),


     path('add_stud/',views.add_stud),
     path('delete_stud/',views.delete_stud),
     path('show_delete_stud/',views.show_delete_stud),
     path('showall_stud/',views.showall_stud ,name="showall_stud"),
     path('update_stud/',views.update_stud),
     path('show_update_stud/',views.show_update_stud),
     path('add_curd/',views.add_curd),
     path('delete_curd/',views.add_curd),
     path('update_curd/',views.add_curd),
     path('show_curd/',views.add_curd),
     
     path('Login/',views.Login),
     path('Register/',views.Register),

    path('GetHomePage/',views.GetHomePage),
    path('StartTest/', views.StartTest),
    path('nextquestion/', views.NextQuestion),
    path('previousquestion/', views.PreviousQuestion),
    path('endtest/', views.End_Test),

    path('getallresultpage/',views.GetAllResultPage),
    path('logoutuser/', views.LogoutUser),


    path('admin_login/', views.admin_login),
    path('admin_registration/', views.admin_registration),
    path('admin_logout/', views.admin_logout),
    
    # Page Display URLs
    path('GetAdminRegister/', views.GetAdminRegister),
    path('GetAdminLogin/', views.GetAdminLogin),
    path('GetAdminHome/', views.GetAdminHome),
]

