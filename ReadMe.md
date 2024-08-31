# These are the Notes for the Fast-Api Tutoial

we import the fastapi and Fastapi from the fastapi library and use that after installing it and the class and make a object of it and save it in app variable 

```
app = FastAPI()
```

For running the program we use the unicron server and start a server with the command 

```
unicron main:app
```

Now we use that app variable and create different routes like get,post,put,delete and create a function specific to that route on what the route will do on being called 

```
example 
@app.get
async def root():
    return {"data":"Api is Live"}
```

## Pydantic 

Now there are times that we want the user to send data in specific format and of specific type for that we need to validate the request body and we can do tha with a library called pydantic with this we can easily validate the request body 

In This we create a class and define static variables with their datatypes with this we can easily create the request body as an object of this type with these static variables and that act as the fields that should be there inside the request body 


