
from calendar import day_abbr
from socket import EAGAIN
from unicodedata import name
from math import floor,trunc
from matplotlib.style import available
from numpy import product
import frappe
from frappe.utils.data import date_diff
import processscheduler as ps
from datetime import date, timedelta, datetime
from operator import itemgetter
from frappe.utils import cint,flt,time_diff,time_diff_in_hours,time_diff_in_seconds,today,add_to_date
from nextproject.nextproject.doctype.resource_allocation.resource_allocation import get_task
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff


@frappe.whitelist()
def task1(project):
    # doc = frappe.get_doc("Employee",emp)
    # print("99999999999999992222222222222222222222222222",doc.name)
    doc1 = frappe.get_all("Employee",["employee_name"])
    print("**************************",doc1)
    doc2 = frappe.get_all("Task",{'project':project},['subject'])
    print("7777777777777777777",doc2)
    d = frappe.get_all("Task",{'project':project},['name'])
    #print(d)

    final_list = []
    
    for i in d:
        final_dict ={}
        final_dict.update({
            'task_id':i.name,
            
        } )
        final_list.append(final_dict)
    print("yyyyyyyyyyyyyyyyyyy")
    print(final_list)
    # if final_list:
    #     return final_list



@frappe.whitelist()
def schedule(values):
    v = eval(values)
    print('llllllllll',v)
    vd_project = frappe.db.get_value('Project Schedule',{"project_name":v.get('project_name') },'name')
    if vd_project:
        doc1 = frappe.get_doc('Project Schedule',vd_project)
        doc1.start_date = v.get('start_date')
        doc1.save(ignore_permissions=True)
    else:
        doc = frappe.new_doc('Project Schedule')
        doc.start_date = v.get('start_date')
        doc.project_name = v.get('project_name')  
        print('???????????????????????????????????????????????????????????????') 
        doc.save(ignore_permissions=True)   
    frappe.db.set_value("Project",name,"expected_start_date",v.get('start_date'))


    
@frappe.whitelist()
def schedule_task(project,empg,start_date):
    aval = []
    r=[]
    b=[]
    d=[]
    first_task = frappe.get_all("Task",{'project':project,'status':'open'},['total_duration_in_days','name','primary_consultant','skills_required','task_length','expected_time','optional','duration_per_day_in_hours'],order_by='task_start_at asc')
    print("888888888888888888",first_task)
    eg = frappe.get_all('Employee Group Table',{'parent':empg},['employee'])
    a=[]
    exp_sd = frappe.get_value("Project",{'status':'Open'},'expected_start_date')
    exp_ed = frappe.get_value("Project",{'status':'Open'},'expected_end_date')
    dt1 = datetime.strptime(str(exp_sd), "%Y-%m-%d")
    dt2 = datetime.strptime(str(exp_ed), "%Y-%m-%d")
    delta = dt2 -dt1
    print('Difference is days',type(delta.days))
    ecr = frappe.get_all('Employee',['employee_costing_rate','name','availibility'])
   



    pro_dt = frappe.get_all('Project',['expected_start_date','expected_end_date'])
    for pro in pro_dt:
        differ = date_diff(pro.expected_end_date , pro.expected_start_date)
    for dts in range(differ):
        diff_dt = add_to_date(pro.expected_start_date , days= dts,as_string=True)
        r.append(diff_dt)
              

    absent = frappe.get_all('Attendance',{'status':'absent'},['employee','attendance_date'])
    for ab in absent:
        if ab:
            lwp = ab.attendance_date.strftime("%Y-%m-%d")
            if lwp in r:
                r.remove(lwp)
        

    present = frappe.get_all('Attendance',{'status':'present'},['employee','attendance_date'])
   
    pre = frappe.get_doc('Project',project)
    cmpny = frappe.get_doc('Company',pre.company)

    holiday = frappe.get_all('Holiday',{'parent':cmpny.default_holiday_list},['holiday_date']) 
    for holi in holiday:
        date_time = holi.holiday_date.strftime("%Y-%m-%d")
        
        if date_time in r:
            r.remove(date_time)
   
    
    
    hr = frappe.get_doc('HR Settings')
    for cst in ecr:
        print(',,,,,,,,,,,,,,,',(cst.employee_costing_rate))
                # first_task = frappe.db.get_list('Task',
                # filters={
                #     'project':project,   
                # },
                # fields=['name','primary_consultant','skills_required','task_length','expected_time'],
                # order_by='task_start_at asc',
                
                # )


    problem = ps.SchedulingProblem(project,
                                       
                                        start_time=datetime.strptime(today(),"%Y-%m-%d"))
    print('@@@@@@@@@@@@@@@@@@@@@2',problem)
    s = 1           
    l = 0
    emp_list =[]
    tsk_list=[]
    if  first_task:
        for k in first_task:
            # if l == l + 1:
            #     if l == 1:
            if k.name not in b:
                # problem = ps.SchedulingProblem(project,
                #                         delta_time=timedelta(days= k.total_duration_in_days),
                #                         start_time=datetime.strptime(start_date,"%Y-%m-%d"))
                c=[]
                for pc in eg:
                    empl,product= frappe.get_value("Employee",{'name':pc.employee},['default_shift','productivity'])
                    
                    
                    if empl:
                        shift = frappe.get_all("Shift Type",['start_time','end_time'])
                        for sft in shift:
                            time_diff =time_diff_in_hours( sft.end_time , sft.start_time)
                            # day = time_diff / 60
                            # print('|||||||||||||',(day))


                        
                        em = frappe.get_doc("Employee",pc.employee)
                        # day = round((k.expected_time)/24 ,1)
                        

                        if em.name not in a:
                            RA = frappe.get_value("Resource Allocation",{'date':today(),'primary_consultance':pc.employee},['date'])
                            rt = frappe.get_value("Resource Allocation",{'date':today(),'primary_consultance':pc.employee},['rup'])
                            if r:
                                if RA: 
    
                                    if rt < 100:
                                       
                                        if em.skills == k.skills_required:
                                            a.append(em.name)
                                            b.append(k.name)
                                           

                                else:
                                    dic ={}
                                    dic.update({
                                        "exp_start_date":today(),
                                        "exp_end_date":today(),
                                        "primary_consultant":pc.employee
                                    })
                                    dicty = str(dic)
                                    get_task(dicty)
                                
                                    
                                
                                    if flt(rt) < 100:
                                        if em.skills == k.skills_required:
                                           
                                            a.append(em.name)
                                            # b.append(ftd.name)
                                            # emp = ps.Worker(em.name, productivity=4, cost=ps.ConstantCostPerPeriod(600))
                   
                   
                   
                    if r:
                        if pc.employee not in c:
                            e = frappe.get_doc("Employee",pc.employee)
                            if e.skills == k.skills_required:
                            
                                c.append(e.name)
                            
                                emp = ps.Worker(e.name, productivity=product, cost=ps.ConstantCostPerPeriod(int(cst.employee_costing_rate)))
                                d.append(emp)
                                
                            
                                day = round((k.expected_time)/hr.standard_working_hours)
                                dt = add_to_date(today(), days = int(day))
                            
                                tsk_list.append({str(k.name):dt})
                                emp_list.append(pc.employee)
                            
                                h= timedelta(hours= (k.total_duration_in_days))
                            
                                # fts = ps.Worker(emp.name)
                                # # print('hhhhhhhhhhhhhh',fts)
                                ftd = frappe.get_doc("Task",k.name)
                                if k.task_length == "Fixed":
                                    if k.optional == 0:
                                        first_task_schedule = ps.FixedDurationTask('{0}'.format(ftd.name), duration=day)
                                        ps.TaskStartAt( first_task_schedule, 0)
                                        first_task_schedule.add_required_resource(emp)
                                    else:
                                    
                                        first_task_schedule = ps.FixedDurationTask('{0}'.format(ftd.name), duration=day,optional= True)
                                        # ps.TaskStartAt( first_task_schedule, 0)
                                        # first_task_schedule.add_required_resource(emp)
                                elif k.task_length == "Variable":
                                    
                                    variable_schedule= ps.VariableDurationTask('{0}'.format(ftd.name), work_amount=int(k.expected_time))
                                    ps.TaskStartAt( variable_schedule, 0)
                                    variable_schedule.add_required_resource(emp)
                                else :
                                    zero_schedule = ps.ZeroDurationTask('{0}'.format(ftd.name))
                                    ps.TaskStartAt( zero_schedule, 0)
                                    zero_schedule.add_required_resource(emp)

                        
                                # cost_ind = problem.add_indicator_resource_cost([emp])
                                solver = ps.SchedulingSolver(problem)
                                solution = solver.solve()
                                print("$$$$$$$$$$$$$$$$$$: ", solution)
                               
                                copy_object = solution.tasks.copy()
                                print("copy_object: ", copy_object)
                                print("keys of copy_object: ", copy_object.keys())
                                
                                for k1 in copy_object.keys():
                                
                                    print(copy_object[k1].__dict__)
                                    t = copy_object[k1].__dict__
                                
                                    # g = eval(t)
                                    for p in t:
                                        if p =='name':
                                            doc = frappe.get_doc('Task',t[p])
                                        
                                            l = l + 1
                                            if l == 1:
                                            
                                                doc.exp_start_date = today()
                                                doc.exp_end_date = add_to_date(today(), days = int(day))
                                            
                                                for el in emp_list:
                                                    doc.primary_consultant = el
                                                if doc.exp_start_date in r:
                                                    r.remove(doc.exp_start_date)
                                                if doc.exp_end_date in r:
                                                    r.remove(doc.exp_end_date)
                                                    
                                            doc.save(ignore_permissions = True)
                                            for jk in tsk_list: 
                                                if l != 1:
                                                    doc1 = frappe.get_doc('Task',k.name)
                                                    s = s + 1  
                                                    
                                                    doc1.exp_start_date = jk.get(str(k.name))
                                                    doc1.exp_end_date =add_to_date(jk.get(str(k.name)), days = int(day))
                                                    for el in emp_list:
                                                        doc1.primary_consultant = el
                                                         # if p == 'duration':
                                                        #     days = t[p] /24
                                                    doc1.save(ignore_permissions = True)
                                if solution:
                                    df = pd.DataFrame([
                                    dict(Task=k.name, Start=dt, Finish=dt),
                                    
                                ])

                                fig = ff.create_gantt(df)
                                fig.show()
        
                        


