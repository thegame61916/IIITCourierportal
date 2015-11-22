def scanUnreceivedItemSendMails():
    query = db.courierDetails.Received == 'NO'
    mailsR = db(query).select(db.courierDetails.Email,distinct=True)
    emails = []
    sub = '[Reminder] Please collect your courier from security'
    msg = 'Hi, \n\nA gentle reminder.\nPlease collect your courier from security.\n\nThanks. \nIIIT Security Staff.' 
    for email in emialR:   
        mail.send(to=[c.Email],
                    subject=sub,
                    reply_to='iiitcourierportal@gmail.com',
                    message=msg)
    
from gluon.scheduler import Scheduler
Scheduler(db, dict(our_function = scanUnreceivedItemSendMails))
