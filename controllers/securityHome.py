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
    if form.accepted:
        sub = 'Courier from ' + form.vars.Company_Name + ' is received [Tracking ID: ' + form.vars.Package_Tracking_ID+']'
        msg = 'Hi ' + form.vars.Name + ', \n\nWe have received a courier for you from ' + form.vars.Company_Name + '. Please collect it from security.\n\nThanks. \nIIIT Security Staff.' 
        mail.send(to=[form.vars.Email],
                  subject=sub,
                  reply_to='iiitcourierportal@gmail.com',
                  message=msg)
    return locals()

@auth.requires_membership('security')  
def getEmailFromHostelDB():
    query = (db.studentHostelDetails.Hostel_Name == request.vars['Hostel_Name']) & (db.studentHostelDetails.Name == request.vars['Name']) & (db.studentHostelDetails.Room_No == request.vars['Room_No'])
    rows = db(query).select()
    emailId = ''
    for row in rows:
        emailId = row.Email
    return "jQuery('#courierDetails_Email').val(%s);" % repr(str(emailId))
