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
    path('IT_head_document_officers_list',views.IT_head_document_officers_list,name='IT_head_document_officers_list'),
    path('IT_head_DocumentOfficer1',views.IT_head_DocumentOfficer1,name='IT_head_DocumentOfficer1'),
    path('IT_head_DocumentOfficer2',views.IT_head_DocumentOfficer2,name='IT_head_DocumentOfficer2'),
    path('IT_head_DocumentOfficer3',views.IT_head_DocumentOfficer3,name='IT_head_DocumentOfficer3'),
    path('IT_head_DocumentOfficer_newly_assign_leads',views.IT_head_DocumentOfficer_newly_assign_leads,name='IT_head_DocumentOfficer_newly_assign_leads'),
    path('IT_head_DocumentOfficer_current_leads',views.IT_head_DocumentOfficer_current_leads,name='IT_head_DocumentOfficer_current_leads'),
    path('IT_head_DocumentOfficer_previous_leads',views.IT_head_DocumentOfficer_previous_leads,name='IT_head_DocumentOfficer_previous_leads'),
     path('IT_head_DocumentOfficer_current_canadaDocuments',views.IT_head_DocumentOfficer_current_canadaDocuments,name='IT_head_DocumentOfficer_current_canadaDocuments'),
    path('IT_head_Teamlead_currentlead',views.IT_head_Teamlead_currentlead,name='IT_head_Teamlead_currentlead'),
    path('IT_head_Teamlead_previoslead',views.IT_head_Teamlead_previoslead,name='IT_head_Teamlead_previoslead'),
    
    path('IT_head_DocumentOfficer_current_UKDocuments',views.IT_head_DocumentOfficer_current_UKDocuments,name='IT_head_DocumentOfficer_current_UKDocuments'),
    
    path('IT_head_DocumentOfficer_previous_UKDocuments',views.IT_head_DocumentOfficer_previous_UKDocuments,name='IT_head_DocumentOfficer_previous_UKDocuments'),
    
    path('IT_head_DocumentOfficer_previous_canadaDocuments',views.IT_head_DocumentOfficer_previous_canadaDocuments,name='IT_head_DocumentOfficer_previous_canadaDocuments'),
    
    
    path('IT_head_add_lead',views.IT_head_add_lead,name='IT_head_add_lead'),
    
    
    
    path('Team_Lead_dashboard',views.Team_Lead_dashboard,name='Team_Lead_dashboard'),
    path('Team_Lead_current_leads',views.Team_Lead_current_leads,name='Team_Lead_current_leads'),
    path('Team_Lead_previous_leads',views.Team_Lead_previous_leads,name='Team_Lead_previous_leads'),
    path('Team_Lead_new_leads',views.Team_Lead_new_leads,name='Team_Lead_new_leads'),
    path('Team_Lead_current_canadaDocuments',views.Team_Lead_current_canadaDocuments,name='Team_Lead_current_canadaDocuments'),
    path('Team_Lead_current_UKDocuments',views.Team_Lead_current_UKDocuments,name='Team_Lead_current_UKDocuments'),
    path('Team_Lead_previous_canadaDocuments',views.Team_Lead_previous_canadaDocuments,name='Team_Lead_previous_canadaDocuments'),
    path('Team_Lead_previous_UKDocuments',views.Team_Lead_previous_UKDocuments,name='Team_Lead_previous_UKDocuments'),
    
    
    
    
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
    
    
     #shebin shaji Admin section
    path('load_admin',views.load_admin,name='load_admin'),
    path('load_leads',views.load_leads,name='load_leads'),
    path('load_concilors',views.load_concilors,name='load_concilors'),
    path('load_docofficers',views.load_docofficers,name='load_docofficers'),
    path('load_documets',views.load_documets,name='load_documets'),
    path('current_lead',views.current_lead,name='current_lead'),
    path('load_completed',views.load_completed,name='load_completed'),
    path('load_cuttentdoc',views.load_cuttentdoc,name='load_cuttentdoc'),
    path('load_priviousdoc',views.load_priviousdoc,name='load_priviousdoc'),
    path('load_admin_profile',views.load_admin_profile,name='load_admin_profile'),
    path('load_previous_lead',views.load_previous_lead,name='load_previous_lead'),
    path('load_previous_consilers',views.load_previous_consilers,name='load_previous_consilers'),
    path('load_admin_clients_more',views.load_admin_clients_more,name='load_admin_clients_more'),
    path('load_admin_client_compstatus',views.load_admin_client_compstatus,name='load_admin_client_compstatus'),
    path('load_admin_client_currentstatus',views.load_admin_client_currentstatus,name='load_admin_client_currentstatus'),

    #yamuna
    path('load_hr_dashboard',views.load_hr_dashboard,name='load_hr_dashboard'),
    path('attendance',views.attendance,name='attendance'),
    path('attendancecard',views.attendancecard,name='attendancecard'),
    path('addteamlead',views.addteamlead,name='addteamlead'),
    path('load_studcounslerprofile',views.load_studcounslerprofile,name='load_studcounslerprofile'),
    path('currentstucounsiler',views.currentstucounsiler,name='currentstucounsiler'),
    path('ithead',views.ithead, name='ithead'),
    path('currentithead',views.currentithead,name='currentithead'),
    path('previousithead',views.previousithead,name='previousithead'),
    path('documentofficerprofile',views.documentofficerprofile,name='documentofficerprofile'),
    path('documentofficers',views.documentofficers,name='documentofficers'),
    path('documentofficercard',views.documentofficercard,name='documentofficercard'),
    path('currentdocoff',views.currentdocoff,name='currentdocoff'),
    path('previousdocoff',views.previousdocoff,name='previousdocoff'),
    path('previousdocoffprofile',views.previousdocoffprofile,name='previousdocoffprofile'),
    path('currentdocoffprofile',views.currentdocoffprofile,name='currentdocoffprofile'),
    path('attendanceview',views.attendanceview,name='attendanceview'),
    path('attendancesearch',views.attendancesearch,name='attendancesearch'),
    path('studentcouncilorcard',views.studentcouncilorcard,name='studentcouncilorcard'),
    path('previousstudcounc',views.previousstudcounc,name='previousstudcounc'),
    path('teamprofile',views.teamprofile,name='teamprofile'),
]