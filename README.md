#README
a simple server based on flask

##API
according to the requirements, this server does not conform to REST exactly but uses verbs in part of its urls.

###/login 
- **POST** 

	```json
	{"username": "user",
	"password": "pw" }
	```
  

###/logout
- **GET**


###/users
- **POST**
	
	create a new user
	
	```json
	{"username": "user",
	"password": "pw" }
	```
	
###/users/username
- **GET**

	get basic info of the relavant user

###/users/username/projects
- **POST**

	save a new project 

###/users/username/projects/pj_id
- **GET**

	get it 

- **UPDATE**

	edit the corresponding project

- **DELETE**


###TODO:
share





