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

	return:
	
	```json
	成功:
		{
			"status": true
		}
	
		or
		
		
	失败:
		{
			"status": false,
			"cause": "the reason or cause of this failure"
		}

	```
  

###/logout
- **GET**

	```json
	未登录:
		{
			"status": false,
     		"cause": "unauthorized"
     	}
     	
     	or
     	
     	
    已登录:
    	{
    		"status": true
    	}
	```
	


###/register
- **POST**
	
	create a new user
	
	```json
	{"username": "user",
	"password": "pw" }
	```
	
	return:
	
	```json
		{
			"status": false, 
			"cause": "username already exists"
		}
		
		or
		
		{
    		"status": true
    	}
	```
	
###/users/username/projects/pj_id

ATTENTION: POST and DELETE require login. Otherwise the server returns 

```json
{
	"status": false, 
	"cause": "unauthroized"
}
```


- **GET**

	return the cover html for corresponding project. 
	use this to **share** the project.

- **POST**

	what this route cares about is the uploaded file.
	any file will be saved to replace the former file in this project
	
	if the project with the pj_id does not exist yet, then it will be created 	and your file will be saved too.
	
	return:
		
	```json
		{
			"status": false, 
			"cause": "cause"
		}
		
		or
		
		{
    		"status": true
    	}
	```
	
- **DELETE**
	
	the whole project folder will be deleted from the server.

	
	```json
		{
			"status": false, 
			"cause": "cause"
		}
		
		or
		
		{
    		"status": true
   
	```


	
	
	




