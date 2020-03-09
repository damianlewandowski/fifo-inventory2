# Bought
Supports CRUD operations and answers 3 questions.

## Create

**Request**:

`POST` `/bought/`

Parameters:

Name           | Type   | Required  | Description
---------------|--------|-----------|------------
date           | string | Yes       | {year}-{month}-{day}
quantity       | number | Yes       | Quantity of bought items
cost_per_item  | number | Yes       | Cost of a single item

**Response**:

```json
Content-Type application/json
201 Created

{
    "date": "2020-03-19",
    "quantity": 20,
    "cost_per_item": 10.0
}
```

## Get a user's profile information

**Request**:

`GET` `/users/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks",
  "email": "richard@piedpiper.com",
}
```


## Update your profile information

**Request**:

`PUT/PATCH` `/users/:id`

Parameters:

Name       | Type   | Description
-----------|--------|---
first_name | string | The first_name of the user object.
last_name  | string | The last_name of the user object.
email      | string | The user's email address.



*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks",
  "email": "richard@piedpiper.com",
}
```
