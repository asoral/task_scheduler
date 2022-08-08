frappe.ui.form.on('Task', {

    refresh:function(frm){
        frm.fields_dict['precedencies'].grid.get_field("task_id").get_query = function(doc,cdt,cdn) {
            return {
                        filters: [
                            ['project','=', frm.doc.project],
                            ['name','!=',frm.doc.name]
                        ]
                        }
            }
        }        
    
});