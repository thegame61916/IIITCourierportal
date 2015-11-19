@auth.requires_membership('student')
def studentHome():
    query = (db.courierDetails.Email == auth.user.email) & (db.courierDetails.Received == 'NO')
    rows=SQLFORM.grid(query = query,searchable=False,details=False,deletable=False,create=False,csv=False,editable=False);
    form = SQLFORM.factory(Field('Student_Name', 'string'),
                            Field('Contact_No', 'integer'),
                            Field('From','datetime'),
                            Field('To','datetime'),
                            Field('Received', requires=IS_IN_SET(['YES', 'NO']),default='NO')).process()
    if form.accepted:
         redirect(URL('searchPage', 'searchPage', 
             vars={'name':form.vars.Student_Name, 
             'contact':form.vars.Contact_No, 
             'from':form.vars.From, 
             'to':form.vars.To, 
             'received':form.vars.Received}))
            
    return {'rows':rows, 'form':form}
