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

	```json
		example:
	
	{
		//假设这是头部
		"username": "john",
		"project_id": 1,
		"action_id": 1,
	
	
		"file": {
			"file_name": "a.html",
			"file_content": "12rdfdfs3" //一段base64代码，或者直接上传，看最后怎么实现
		}
	}
	
	...
	
	{
		//假设这是头部
		"username": "john",
		"project_id": 1,
		"action_id": 1,
	
	
		"file": {
			"file_name": "a.css",
			"file_content": "sfa3516" //一段base64代码，或者直接上传，看最后怎么实现
		}
	}
```


	save a new project 

###/users/username/projects/pj_id
- **GET**

	get it 

- **UPDATE**

	edit the corresponding project

- **DELETE**


###TODO:
share





