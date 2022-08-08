frappe.ui.form.on('Project', {
    refresh: function(frm) {
            console.log("9242**********************************")
			frm.add_custom_button(__('Schedule Task'), () => {
				// frm.events.task_schedule(frm);
                frappe.call({
                    method: "task_scheduler.task_scheduler.custom_project.schedule_task",
                    args:{
                        "project":frm.doc.name,
                        "empg":frm.doc.employee_group,
                        "start_date":frm.doc.expected_start_date
                    },
                    callback: function(r) {
                        frm.trigger("schedule_task")
                    }
                });
	        });
            
        

        
    } ,
    schedule_task:function(frm){
        let d = new frappe.ui.Dialog({
            title: '            What Kind Of Solution Do You Want?',
            
            fields: [
               
                {

                    fieldtype: "Button",
                    label: __("Standard"),
                    fieldname: "standard",
                    cssClass: "btn-primary"

                },
                {

                    fieldtype: "Date",
                    label: __("Start Date"),
                    fieldname: "start_date",
                    //options:"Task"

                },
                {

                    fieldtype: "Link",
                    label: __("Project Name"),
                    fieldname: "project_name",
                    options: "Project"

                },
                
                {

                    fieldtype: "Column Break",
                    fieldname: "column_break",

                },

                {

                    fieldtype: "Button",
                    label: __("Makespan Objective"),
                    fieldname: "makespan_objective",
                    cssClass: "btn-primary"

                },
                // {

                //     fieldtype: "Date",
                //     label: __("End Date"),
                //     fieldname: "end_date",
                   

                // },
                
                

            ],
            primary_action_label: 'Submit',
            primary_action(values) {
                frappe.call({
                    method: "task_scheduler.task_scheduler.custom_project.schedule",
                    args:{
                        "values":values,
                    },
                   
                });
                
                console.log(values);
                d.hide();
            }
        });
        
        d.show();
    }

});





    