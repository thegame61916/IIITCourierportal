def scanUnreceivedItemSendMails():
    import time
    open('/time/tasks', 'w').write(time.ctime() + '\n')
    return 'hello'
    
from gluon.scheduler import Scheduler
Scheduler(db, dict(our_function = scanUnreceivedItemSendMails))
