###### You need to follow below commands one by one to install it successfully in your system. ######

1) To clone from git
$ git clone 

2) To install required module run requirement.txt file. 
$ pip install -r requirements.txt


3) Now you have to create a database with username and password in PostgreSQL and need to set required parameter inside "config.py" file. to set it directly from terminal use this command:
$ nano config.py  or gedit config.py

4) After adding and saving your database details run below commands one by one.
$ python migrate.py db init
$ python migrate.py db migrate
$ python migrate.py db upgrade
$ python run.py	


###### API ENDPOINT ######
1) GET
- http://localhost:5000/api/v1/users.json : For returning a list of all users
- http://localhost:5000/api/v1/users/<PASS ID HERE>.json  : For returning user details for the given user id if it exists

2) POST
- http://localhost:5000/api/v1/users.json : For creating a user and returns with user id

3) PUT
- http://localhost:5000/api/v1/users/<PASS ID HERE>.json : For updating the user details if the user exists and returns with the updated results

4) DELETE
- http://localhost:5000/api/v1/users/<PASS ID HERE>.json : For deleting the user by passing their particular id.