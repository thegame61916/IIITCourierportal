The application has two user groups : 1. security 2. student

sign up is not allowed on Courier portal. Application is supposed to use existing IIIT accounts of security and students. If you want to create a new account for this application then manually add the user details in following tables:
1. db.auth_user
2. db.auth_membership

Currently two accounts are there for testing
1. student account: user: sonam.gupta@students.iiit.ac.in password: Game
2. security account: user: sharma.mohit@students.iiit.ac.in password: Game

If you add a new student then create an entry in 'db.studentHostelDetails' in also ofr the email ids of student.

python anywhere link: https://thegame61916.pythonanywhere.com/IIITCourier/default/index
gitHub link: https://github.com/thegame61916/IIITCourierportal

All functionalities are working as expected. No major known bug in flow.
