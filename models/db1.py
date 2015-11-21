# coding: utf8

db.define_table('courierDetails', 
    Field('Name', 'string',requires=IS_NOT_EMPTY()), 
    Field('Hostel_Name','string',requires=IS_NOT_EMPTY()), 
    Field('Room_No','integer',requires=IS_INT_IN_RANGE(0,600)), 
    Field('Contact_No', 'integer',requires=IS_INT_IN_RANGE(1111111111,9999999999)), 
    Field('Package_Tracking_ID', 'string',requires=IS_NOT_EMPTY()), 
    Field('Company_Name', 'string',requires=IS_NOT_EMPTY()), 
    Field('Email', 'string',requires=IS_EMAIL()), 
    Field('Received',requires=IS_IN_SET(['YES', 'NO']),default='NO'), 
    Field('Size', requires=IS_IN_SET(['SMALL', 'MEDIUM', 'LARGE']),default='SMALL'),
    Field('Date_received', 'datetime',readable=False,writable=False,default=request.now))

db.define_table('feedbackDetails',
                Field('Company_Name', 'string',requires=IS_NOT_EMPTY()),
                Field('Item_ID', 'string',requires=IS_NOT_EMPTY()),
                Field('Name', 'string',requires=IS_NOT_EMPTY()),
                Field('Contact_No', 'integer',requires=IS_INT_IN_RANGE(1111111111,9999999999)),
                Field('Delively_On_Time',requires=IS_IN_SET(['YES', 'NO']),default='YES'),
                Field('Packaging_Quality', requires=IS_IN_SET(['Excellent', 'Good', 'Fair','Poor']),default='Good'),
                Field('Feedback', 'text',requires=IS_NOT_EMPTY()),
                Field('Actions_Taken',requires=IS_IN_SET(['YES', 'NO']),default='NO'))
    
db.define_table('studentHostelDetails', 
    Field('Name', 'string',requires=IS_NOT_EMPTY()), 
    Field('Hostel_Name','string',requires=IS_NOT_EMPTY()), 
    Field('Room_No','integer',requires=IS_INT_IN_RANGE(0,600)), 
    Field('Email', 'string',requires=IS_EMAIL()))
