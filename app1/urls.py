from django.urls import path,re_path
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.login,name='login'),
    path('studens',views.studens, name='studens'),
    path('sales',views.sales, name='sales'),
    path('newlyleades',views.newlyleades,name='newlyleades'),
    path('currentleadss',views.currentleadss,name='currentleadss'),
    path('previousleadss',views.previousleadss,name='previousleadss'),
    path('previousdash',views.previousdash,name='previousdash'),
    path('statuscurrent',views.statuscurrent,name='statuscurrent'),
    #dilashad
    path('dashboard',views.dashboard, name='dashboard' ),
    path('team_leader_clints',views.team_leader_clints,name='team_leader_clints'),
    path('status_progress',views.status_progress,name='status_progress'),

   
    # # Eldho Mathew
    path('signupp',views.signupp,name='signupp'),
    path('newlyassignleads',views.newlyassignleads, name='newlyassignleads' ),
    path('status1',views.status1, name='status1' ),
    # # Sambhu v pillai
    path('home',views.home, name='home' ),
    path('currentleads',views.currentleads, name='currentleads' ),
    path('previousleads',views.previousleads, name='previousleads' ),
    path('councilornewlyprofile',views.councilornewlyprofile,name='councilornewlyprofile'),
    path('status2',views.status2, name='status2' ),

    re_path(r'^DocumentOfficer_newly_assigned_leads$', views.DocumentOfficer_newly_assigned_leads, name='DocumentOfficer_newly_assigned_leads'),
    re_path(r'^DocumentOfficer_Previous_leads$', views.DocumentOfficer_Previous_leads, name='DocumentOfficer_Previous_leads'),
    # re_path(r'^admin_login$', views.admin_login, name='admin_login'),
    re_path(r'^DocumentOfficer_dashboard$', views.DocumentOfficer_dashboard, name='DocumentOfficer_dashboard'),
    re_path(r'^DocumentOfficer_index$', views.DocumentOfficer_index, name='DocumentOfficer_index'),
    re_path(r'^DocumentOfficer_Accsetting$', views.DocumentOfficer_Accsetting, name='DocumentOfficer_Accsetting'),
    re_path(r'^DocumentOfficer_CurrentLeads_table$', views.DocumentOfficer_CurrentLeads_table, name='DocumentOfficer_CurrentLeads_table'),
    re_path(r'^DocumentOfficer_CanadaDocuments$', views.DocumentOfficer_CanadaDocuments, name='DocumentOfficer_CanadaDocuments'),
    re_path(r'^DocumentOfficer_UKDocuments$', views.DocumentOfficer_UKDocuments, name='DocumentOfficer_UKDocuments'),
    re_path(r'^DocumentOfficer_Previous_CanadaDocuments$', views.DocumentOfficer_Previous_CanadaDocuments, name='DocumentOfficer_Previous_CanadaDocuments'),
    re_path(r'^DocumentOfficer_Previous_UKDocuments$', views.DocumentOfficer_Previous_UKDocuments, name='DocumentOfficer_Previous_UKDocuments'),
    
]