from django.shortcuts import render


#sherry george
def login(request):
    return render(request,'login.html')
def studens(request):
    return render(request,'councilordashboard.html')#studentscouncilor tab
def sales(request):
    return render(request,'salesnewly.html')  
def newlyleades(request):
    return render(request,'newlyleads.html')    
def currentleadss(request):
    return render(request,'currentleads.html') 
def previousleadss(request):
    return render(request,'previouslyassleads.html')      
def previousdash(request):
    return render(request,'previousleads.html')     
def statuscurrent(request):
    return render(request,'status1.html')   

    #IT HEAD   

def IT_head_document_officers_list(request):
    return render(request,'IT_head_document_officers_list.html')      
def IT_head_DocumentOfficer1(request):
    return render(request,'IT_head_DocumentOfficer1.html')      
def IT_head_DocumentOfficer2(request):
    return render(request,'IT_head_DocumentOfficer2.html')      
def IT_head_DocumentOfficer3(request):
    return render(request,'IT_head_DocumentOfficer3.html')      
def IT_head_DocumentOfficer_newly_assign_leads(request):
    return render(request,'IT_head_DocumentOfficer_newly_assign_leads.html')      
def IT_head_DocumentOfficer_current_leads(request):
    return render(request,'IT_head_DocumentOfficer_current_leads.html')      
def IT_head_DocumentOfficer_previous_leads(request):
    return render(request,'IT_head_DocumentOfficer_previous_leads.html') 
def IT_head_Teamlead_currentlead(request):
    return render(request,'IT_head_Teamlead_currentlead.html')
def IT_head_Teamlead_previoslead(request):
    return render(request,'IT_head_Teamlead_previouslead.html')

def IT_head_add_lead(request):
    return render(request,'IT_head_add_lead.html') 



def IT_head_DocumentOfficer_current_canadaDocuments(request):
    return render(request,'IT_head_DocumentOfficer_current_canadaDocuments.html') 
def IT_head_DocumentOfficer_current_UKDocuments(request):
    return render(request,'IT_head_DocumentOfficer_current_UKDocuments.html') 
def IT_head_DocumentOfficer_previous_UKDocuments(request):
    return render(request,'IT_head_DocumentOfficer_previous_UKDocuments.html') 
def IT_head_DocumentOfficer_previous_canadaDocuments(request):
    return render(request,'IT_head_DocumentOfficer_previous_canadaDocuments.html')



def Team_Lead_dashboard(request):
    return render(request,'Team_Lead_dashboard.html') 
def Team_Lead_current_leads(request):
    return render(request,'Team_Lead_current_leads.html') 
def Team_Lead_previous_leads(request):
    return render(request,'Team_Lead_previous_leads.html') 
def Team_Lead_new_leads(request):
    return render(request,'Team_Lead_new_leads.html') 

def Team_Lead_current_canadaDocuments(request):
    return render(request,'Team_Lead_current_canadaDocuments.html')
def Team_Lead_current_UKDocuments(request):
    return render(request,'Team_Lead_current_UKDocuments.html')
def Team_Lead_previous_canadaDocuments(request):
    return render(request,'Team_Lead_previous_canadaDocuments.html')
def Team_Lead_previous_UKDocuments(request):
    return render(request,'Team_Lead_previous_UKDocuments.html')    

#dilshad
def dashboard(request):
    return render(request,'dashboard_head.html')    
def team_leader_clints(request):
    return render(request,'clints.html')  
def status_progress(request):
    return render(request, 'status.html')      

# counsilor dashboard
#sambhu
def home(request):
     return render(request,'councilor/home.html')
def currentleads(request):
     return render(request, 'councilor/current_leads.html')
def previousleads(request):
    return render(request, 'councilor/previous_leads.html')
def councilornewlyprofile(request):
    return render(request, 'councilor/councilornewprof.html') 
def status2(request):
    return render(request, 'councilor/counstatus1.html')  
# #eldho    


def signupp(request):
    return render(request,'signup.html')
def newlyassignleads(request):
     return render(request, 'councilor/newly_leads.html')
def status1(request):
    return render(request, 'councilor/counstatus.html')       



def DocumentOfficer_index(request):
    return render(request,"DocumentOfficer_index.html")

def DocumentOfficer_newly_assigned_leads(request):
    return render(request, "DocumentOfficer_newly_assigned_leads.html")

def DocumentOfficer_Previous_leads(request):
    return render(request, "DocumentOfficer_Previous_leads.html")

def DocumentOfficer_index(request):
    return render(request,"DocumentOfficer_index.html")
    
def DocumentOfficer_dashboard(request):
    return render(request,"DocumentOfficer_dashboard.html")
    
def DocumentOfficer_CurrentLeads_table(request):
    return render(request,"DocumentOfficer_CurrentLeads_table.html")
    
def DocumentOfficer_CanadaDocuments(request):
    return render(request,"DocumentOfficer_CanadaDocuments.html")

def DocumentOfficer_UKDocuments(request):
    return render(request,"DocumentOfficer_UKDocuments.html")

def DocumentOfficer_Accsetting(request):
    return render(request,"DocumentOfficer_Accsetting.html")

def DocumentOfficer_Previous_CanadaDocuments(request):
    return render(request,"DocumentOfficer_Previous_CanadaDocuments.html")

def DocumentOfficer_Previous_UKDocuments(request):
    return render(request,"DocumentOfficer_Previous_UKDocuments.html")    




#Shebin Shaji ==> admin

def load_admin(request):
    return render(request,'admin.html')

def load_leads(request):
    return render(request,'admin_leads.html')

def load_concilors(request):
    return render(request,'admin_concilors.html')

def load_docofficers(request):
    return render(request,'admin_docofficers.html')

def load_documets(request):
    return render(request,'admin_document.html')

def load_admin_profile(request):
    return render(request,'admin_profile.html')

def load_cuttentdoc(request):
    return render(request,'admin_currentdoc.html')

def load_priviousdoc(request):
    return render(request,'admin_priviousdoc.html')

def load_completed(request):
    return render(request,'admin_completed.html')

def load_previous_lead(request):
    return render(request,'admin_previs_leads.html')

def current_lead(request):
    return render(request,'admin_current_leads.html')

def load_previous_consilers(request):
    return render(request,'admin_prev_consilers.html')

def load_admin_clients_more(request):
    return render(request,'admin_client_more.html')

def load_admin_client_compstatus(request):
    return render(request,'admin_client_status_comp.html')

def load_admin_client_currentstatus(request):
    return render(request,'admin_client_status_current.html')


#Yamuna 
def load_hr_dashboard(request):
    return render(request,'dashboard_hr.html')
def attendance(request):
    return render(request,'attendance.html')
def addteamlead(request):
    return render(request,'addteamlead.html')
def ithead(request):
    return render(request,'itheadprofile.html')
def currentithead(request):
    return render(request,'currentithead.html')
def previousithead(request):
    return render(request,'previousithead.html')
def documentofficerprofile(request):
    return render(request,'documentofficerprofile.html')
def documentofficers(request):
    return render(request,'documentofficers.html')
def documentofficercard(request):
    return render(request,'documentofficercard.html')
def currentdocoff(request):
    return render(request,'currentdocoff.html')
def previousdocoff(request):
    return render(request,'previousdocoff.html')
def attendancecard(request):
    return render(request,'attendancecard.html')
def attendanceview(request):
    return render(request,'attendanceview.html')
def attendancesearch(request):
    return render(request,'attendancesearch.html')
def studentcouncilorcard(request):
    return render(request,'studentcouncilorcard.html')
def previousstudcounc(request):
    return render(request,'previousstudcounc.html')
def teamprofile(request):
    return render(request,'teamprofile.html')
def previousdocoffprofile(request):
    return render(request,'previousdocoffprofile.html')
def currentstucounsiler(request):
    return render(request,'stud_currentcounsiler.html')
def load_studcounslerprofile(request):
    return render(request,'studcounsilerprofile.html')
def currentdocoffprofile(request):
    return render(request,'currentdocoffprofile.html')