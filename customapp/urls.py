from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Homepage),
    path('about/', Aboutpage),
    path('plans/add/', PlansAddpage),
    path('plans/', PlansAll),
    path('plans/delete/<int:id>/', PlansDelete, name="plan_del"),
    path('plans/update/<int:id>/', PlansUpdate, name="plan_upd"),
    path('members/', MembersView),
    path('members/add/',  MembersAddPage),
    path('members/delete/<int:id>/', MembersDelete, name="members_del"),
    path('members/update/<int:id>/', MembersUpdate, name="members_upd"),
    path('membersdetails/', Members_DetailsView),
    path('membersdetails/add/', Members_Details_AddPage),
    path('', LoginPage),
    path('logout/', Logout),
    path('signup/', SignupPage),
]