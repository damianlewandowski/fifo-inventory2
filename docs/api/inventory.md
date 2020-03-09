# Inventory
Answers following questions:
1. How many pens does Sebastian have in stock ultimo Jan 11th 2016?
2. What is the value of the inventory ultimo Jan 11th 2016?
3. What are the costs of pen solds ultimo Jan 11th 2016?

## 1.

**Request**:

`GET` `/inventory/inventory_status`

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