import requests

URL = "https://my-json-server.typicode.com/JohnDrD-UdA/Trabajo_PI_1"

print("##### get #####")
request= requests.get(URL+"/users")

print(request.json())

print("##### post #####")
request= requests.post(URL+"/users",{
    "id": 4,
    "name":"paco"
})
print(request.json())

# De la documentacion de My-json-serve: 
#resource will not be really updated on the server but it will be faked as if.
#Se aplica para cada request que cambie el recurso, no se ve el cambio reflejado

print("##### put #####")
request= requests.put(URL+"/users/1",{
    "id": 1,
    "name":"julio"
})
print(request.json())

print("##### delete #####")
request= requests.delete(URL+"/users/1")
print(request.json())


