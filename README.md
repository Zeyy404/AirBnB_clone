# AirBnB Clone - Command Interpreter #

## Background Context ##

Welcome to the AirBnB clone project! This project is the first step toward building a full web application. The goal is to create a command interpreter to manage AirBnB objects such as User, State, City, Place, etc. The command interpreter will allow users to create, retrieve, perform operations on, update, and destroy objects.

## Command Interpreter ##

### How to Start ###

To start the command interpreter, run the following command:

`$ ./console.py`


### How to Use ###

Once the command interpreter is running, you can use the following commands:
* **create**: Create a new object (e.g., User, Place).
* **show**: Retrieve an object from a file or database.
* **destroy**: Destroy an object.
* **all**: Display all objects or all objects of a specific type.
* **update**: Update attributes of an object.
* **quit**: Exit the command interpreter.


### Examples ###

Interactive Mode

```
$ ./console.py

(hbnb) create User

0763d362-8c74-4f7f-9b65-3ea1f49ac9e1

(hbnb) show User 0763d362-8c74-4f7f-9b65-3ea1f49ac9e1

[User] (0763d362-8c74-4f7f-9b65-3ea1f49ac9e1) {'id': '0763d362-8c74-4f7f-9b65-3ea1f49ac9e1', 'created_at': '2024-02-13T12:00:00', 'updated_at': '2024-02-13T12:00:00'}

(hbnb) all

["[User] (0763d362-8c74-4f7f-9b65-3ea1f49ac9e1) {'id': '0763d362-8c74-4f7f-9b65-3ea1f49ac9e1', 'created_at': '2024-02-13T12:00:00', 'updated_at': '2024-02-13T12:00:00'}"]

(hbnb) quit

$
```

Non-Interactive Mode

```
$ echo "create User" | ./console.py

0763d362-8c74-4f7f-9b65-3ea1f49ac9e1

$ echo "show User 0763d362-8c74-4f7f-9b65-3ea1f49ac9e1" | ./console.py

[User] (0763d362-8c74-4f7f-9b65-3ea1f49ac9e1) {'id': '0763d362-8c74-4f7f-9b65-3ea1f49ac9e1', 'created_at': '2024-02-13T12:00:00', 'updated_at': '2024-02-13T12:00:00'}

$ echo "all" | ./console.py

["[User] (0763d362-8c74-4f7f-9b65-3ea1f49ac9e1) {'id': '0763d362-8c74-4f7f-9b65-3ea1f49ac9e1', 'created_at': '2024-02-13T12:00:00', 'updated_at': '2024-02-13T12:00:00'}"]

$
```