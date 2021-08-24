A small Flask application using SQLAlchemy. 

# Getting started 

## Installation

To get up and running, just run `deploy.sh`:
```shell
./deploy.sh
```

This will expose the Flask app on `http://0.0.0.0:5000/`. 

## Create a user 

```shell
curl -H "Content-Type: application/json"  \
  -d '{"username":"user1"}' \
  http://0.0.0.0:5000/users
```


## Get the users 

```shell
curl http://0.0.0.0:5000/users
```