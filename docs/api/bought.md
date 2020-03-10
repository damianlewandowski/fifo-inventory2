# Bought
Supports CRUD operations.

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

## Quantity
Retrieves total amount of bought items

**Request**:

`GET` `/bought/quantity/`

**Response**:

```json
Content-Type application/json
200 OK

{
    "quantity": 180
}
```

## Total Value
Retrieves total value of bought items

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

