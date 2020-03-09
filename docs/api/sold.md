# Sold
Supports CRUD operations.

## Create

**Request**:

`POST` `/sold/`

Parameters:

Name           | Type   | Required  | Description
---------------|--------|-----------|------------
date           | string | Yes       | {year}-{month}-{day}
quantity       | number | Yes       | Quantity of sold items

**Response**:

```json
Content-Type application/json
201 Created

{
    "date": "2020-03-19",
    "quantity": 20
}
```

## Total Value
Retrieves total value of sold items

**Request**:

`GET` `/bought/total_value/`

**Response**:

```json
Content-Type application/json
200 OK

{
    "total_value": 450.0
}
```