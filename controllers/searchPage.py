@auth.requires_login()
def searchPage():
    name = request.vars['name']
    contact = request.vars['contact']
    From = request.vars['from']
    To = request.vars['to']
    received = request.vars['received']
    queries = []
    if name != '':
        queries.append(db.courierDetails.Name == name)
    if contact != None and contact != 'None':
        queries.append(db.courierDetails.Contact_No == int(contact))
    if From != 'None':
        queries.append(db.courierDetails.Date_received >=From)
    if To != 'None':
        queries.append(db.courierDetails.Date_received <= To)
    if received != 'None':
        queries.append(db.courierDetails.Received == received)
    if auth.has_membership(group_id='student'):
        queries.append(db.courierDetails.Email == auth.user.email)
    query = reduce(lambda a,b:(a&b),queries)    
    if auth.has_membership(group_id='student'):
        rows=SQLFORM.grid(query = query,searchable=False,details=False,deletable=False,editable=False,create=False,csv=False)
    else:
        rows=SQLFORM.grid(query = query,searchable=False,details=False,deletable=False,create=False,csv=False)
    
    return {'rows':rows}

@auth.requires_membership('security')
def sendAcceptanceMail(): 
    sub = 'Courier has been collected by you [Tracking ID: ' + request.vars['Package_Tracking_ID'] + ']'
    msg = 'Hi ' + request.vars['Name'] + ', \n\nThis is a notificaiton mail.\nCourier with mentioned Tracking ID from ' + request.vars['Company_Name'] + ' has been collected by you.\n\nThanks. \nIIIT Security Staff.' 
    mail.send(to=[request.vars['Email']],
                subject=sub,
                reply_to='iiitcourierportal@gmail.com',
                message=msg)
    return ''
