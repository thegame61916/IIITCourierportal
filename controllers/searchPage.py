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
    query = reduce(lambda a,b:(a&b),queries)    
       
    rows=SQLFORM.grid(query = query,searchable=False,details=False,deletable=False,create=False,csv=False)
    return {'rows':rows}
