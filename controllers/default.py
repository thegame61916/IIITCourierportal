# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
from gluon.tools import Crud
crud = Crud(db)

def index():
    redirect(URL('login'))

@auth.requires_login()    
def login():
    if auth.has_membership(group_id='security'):
        redirect(URL('securityHome'))
    else:
        redirect(URL('studentHome'))
        
@auth.requires_membership('security')
def securityHome():
    form1 = SQLFORM.factory(Field('Student_Name', 'string'),
                            Field('Contact_No', 'integer'),
                            Field('From','datetime'),
                            Field('To','datetime'),
                            Field('Received', requires=IS_IN_SET(['YES', 'NO']),default='NO')).process()
    form = crud.create(db.courierDetails).process()    #SQLFORM(db.courierDetails).process()
    if form1.accepted:
         redirect(URL('searchPage', 
             vars={'name':form1.vars.Student_Name, 
             'contact':form1.vars.Contact_No, 
             'from':form1.vars.From, 
             'to':form1.vars.To, 
             'received':form1.vars.Received}))
    return locals()

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
       
    rows=SQLFORM.grid(query = query);
    return {'rows':rows}
    
@auth.requires_membership('student')
def studentHome():
    query = (db.courierDetails.Email == auth.user.email) & (db.courierDetails.Received == 'NO')
    rows=SQLFORM.grid(query = query);
    return {'rows':rows}

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

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
