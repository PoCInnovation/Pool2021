# go-message

A simple Go API that manage users and message

## Getting started

Launch docker-compose

```
docker-compose up -d --build
```

> :warning: Si vous n'avez pas `direnv allow`, faites la commande `source .envrc` pour charger l'environnement

## Entities

### User
- `userID` : **int**
- `username` : **string**
- `profilePicture` : **string**
- `password` : **string**

### Message
- `messageID` : **int**
- `message` : **string**
- `sender` : **User**

### Room
- `roomID` : **int**
- `messages` : **Message[]**


## HTTP Routes

Quick description of routes exposed by Go-message API

### Check state

Route: `xxx/api/health`<br>
Method: **GET**<br>
Return:
 - **200**: OK

### Register

Route: `xxx/api/register`<br>
Method: **POST**<br>
Body:
```
{
  username: "xxxx"
  password: "xxxx"
  profilePicture: "xxxx"
}
```
Return:
 - **201** : User created
 - **400** : Bad request
 - **403** : User already exist
 - **500** : Internal server error

### Login

Route: `xxx/api/login`<br> 
Method: **POST**<br>
Body:
```
{
  username: "xxxx"
  password: "xxxx"
}
```
Return:
 - **404** : User doesn't exist
 - **200** : User connected
 - **500** : Internal server error

### Logout

Route: `xxx/api/logout`<br>
Method: **POST**
Return:
 - **200** : OK
 - **401** : Unauthorized
 - **404** : Not found
 
 ### getRooms
 
 Route: `xxx/api/room`<br>
 Method: **GET**<br>
 Return:
  - **200** : Rooms
  - **401** : User not connected
  - **500** : Internal server error
  
 
### createRoom

Route: `xxx/api/room`<br>
Method: **POST**<br>
Return:
 - **201** : Room created (with roomID)
 - **401** : User not connected
 - **500** : Internal server error 
 
### joinRoom

Route: `xxx/api/room/join?roomID=xxx`<br> 
Method: **POST**<br>
Return:
 - **200** : Room joined
 - **400** : Bad request
 - **401** : User not connected
 - **404** : Room not found
 - **500** : Internal server error 
 
### roomMessage (GET)

Route: `xxx/api/room/message?roomID=xxxx`<br>
Method: **GET**<br>
Return:
 - **200** : Room
 - **400** : Bad request
 - **401** : User not connected
 - **404** : Room not found
 - **500** : Internal server error
 
### roomMessage (POST)

Route: `xxx/api/room/message?roomID=xxxx`<br>
Method: **POST**<br>
Body:
```
{
  message: "xxx"
}
```
Return:
 - **201** : Message created
 - **400** : Bad request
 - **401** : User not connected
 - **404** : Room not found
 - **500** : Internal server error
 
### roomMessage (PUT)

Route: `xxx/api/room/message?roomID=xxxx&messageID=xxx`<br>
Method: **PUT**<br>
Body:
```
{
  message: "xxx"
}
```
Return:
 - **201** : Message created
 - **400** : Bad request
 - **401** : User not connected
 - **404** : Room not found
 - **500** : Internal server error 

### roomMessage (DELETE)

Route: `xxx/api/room/message?roomID=xxxx&messageID=xxxx`<br>
Method: **DELETE**<br>
Return:
 - **200** : Message deleted
 - **400** : Bad request
 - **401** : User not connected
 - **404** : Room not found
 - **500** : Internal server error
