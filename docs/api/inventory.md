# Inventory
Answers following questions:
1. How many pens does Sebastian have in stock ultimo Jan 11th 2016?
2. What is the value of the inventory ultimo Jan 11th 2016?
3. What are the costs of pen solds ultimo Jan 11th 2016?

## Quantity of items

**Request**:

`GET` `/inventory/quantity/`

Query Parameters:

Name           | Type   | Required  | Description
---------------|--------|-----------|------------
year           | number | Yes       | Year
month          | number | Yes       | Month
day            | number | Yes       | Day

**Response**:

```json
Content-Type application/json
200 OK

{
    "date": "2020-03-19",
    "quantity": 20,
    "cost_per_item": 10.0
}
```

## Value of the inventory

**Request**:

`GET` `/inventory/value/`

Query Parameters:

Name           | Type   | Required  | Description
---------------|--------|-----------|------------
year           | number | Yes       | Year
month          | number | Yes       | Month
day            | number | Yes       | Day

**Response**:

```json
Content-Type application/json
200 OK

{
    "total_value": 225.0
}
```

## Value of an item

**Request**:

`GET` `/inventory/item_value/`

Query Parameters:

Name           | Type   | Required  | Description
---------------|--------|-----------|------------
year           | number | Yes       | Year
month          | number | Yes       | Month
day            | number | Yes       | Day

**Response**:

```json
Content-Type application/json
200 OK

{
    "current_item_price": 1.0
}
```

