from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('addcity/',views.addcity,name='addcity'),
    path('guest/',views.guest,name='guest'),
    path('gifts/',views.gifts,name='gifts'),
    path('addstaff/',views.addstaff,name='addstaff'),
    path('addstaff/updates/<int:id>',views.updates,name='updates'),
    path('gifts/deletgift/<int:id>',views.deletgift,name='deletgift'),
    path('carriers/jobdelete/<int:id>',views.jobdelete,name='jobdelete'),


    path('carriers/',views.carriers,name='carriers'),
    path('addcity/update/<int:id>',views.update,name='update'),
    path('appointment',views.appointment,name='adminappointment'),
    path('addcity/delete/<int:id>',views.delete,name='delete'),
    path('appointment/deleted/<int:id>',views.deleted,name='deleted'),
    path('addservice/',views.addservice,name='addservice'),
    path('addservice/modify/<int:id>',views.modify,name='modify'),
    path('addservice/deletes/<int:id>',views.deletes,name='deletes'),







    # path('edit/<int:city_id>',views.edit,name='edit')

]
