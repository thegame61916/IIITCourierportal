@auth.requires_membership('security')
def securityHome():
    form1 = SQLFORM.factory(Field('Student_Name', 'string'),
                            Field('Contact_No', 'integer'),
                            Field('From','datetime'),
                            Field('To','datetime'),
                            Field('Received', requires=IS_IN_SET(['YES', 'NO']),default='NO')).process()
    db.courierDetails.Received.writable = False
    form = crud.create(db.courierDetails).process()    #SQLFORM(db.courierDetails).process()
    db.courierDetails.Received.writable = True
    if form1.accepted:
         redirect(URL('searchPage', 'searchPage', 
             vars={'name':form1.vars.Student_Name, 
             'contact':form1.vars.Contact_No, 
             'from':form1.vars.From, 
             'to':form1.vars.To, 
             'received':form1.vars.Received}))
    return locals()
    
def getEmailFromHostelDB():
    import cgi
    s = cgi.escape(str(request.vars))
    query = (db.studentHostelDetails.Hostel_Name == request.vars['Hostel_Name']) & (db.studentHostelDetails.Name == request.vars['Name']) & (db.studentHostelDetails.Room_No == request.vars['Room_No'])
    rows = db(query).select()
    emailId = ''
    for row in rows:
        emailId = row.Email
    t = 'mohit'
    return "jQuery('#courierDetails_Email').val(%s);" % repr(str(emailId))
