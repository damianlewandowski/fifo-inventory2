# FIFO inventory

[![Build Status](https://travis-ci.org/damianlewandowski/ciklum.svg?branch=master)](https://travis-ci.org/damianlewandowski/ciklum)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Recruitment exercise. Check out the project's [documentation](http://damianlewandowski.github.io/ciklum/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Journal

## First decisions
- I need to choose tools for the job. Since I am not sure if I'll get this job, and it's not a contract job, I will treat it more as a learning experience
- I will choose python and django instead of node and express.js, because that's what I've been playing with lately and is perfectly suitable for this problem.

## Need to
- Setup CI 
- Learn how to setup logging
- Containerize django-rest-framework app using docker
- Check how error handling is handled by said framework
- Setup auto generation of OpenAPI schemas
- Ask if you want it deployed somewhere
- Design database models (super easy)
- Write Business logic
- Write tests for API


## First things done:
- Read a lot about writing production ready code in django.
- Found awesome template for writing django-rest code. Cookiecutter django-rest. Kickass tool!
- Generated project and wrote 3 endpoints to answer the questions.

## How many items in inventory ultimo {ultimo}
- All I had to do here is count amount of bought and solds items ultimo {ultimo} and return the result.

## Value of inventory ultimo {ultimo}
- Had to fetch from database total amount of sold items ultimo {ultimo}. Then calculate the total value of inventory ultimo {ultimo}
Finally loop through bought items and subtract on each iteration from inventory value amount of sold items * items bought on given days using FIFO.
- This one was trickier. I had a couple of ideas, first was stupid and involved fetching all of data from database and
calculating the result in python. Very slow and not scalable. Easy to run out of memory and block the service because of too much 
load on cpu.
- Second one was much better, but still involved fetching all of the items from database at once. Needed something better
- Found .iterator() function, that chunks data from database so I won't run out of memory or process too many items at once.
- In the end I am pretty happy about this solution. Futher optimizations could be done by going on lower level sql and performing queries directly 
to the database instead of through ORM.

## Cost of current item ultimo {ultimo}
- Easy, used most of the logic from previous question. Instead of breaking the iteration I return a response of current bought items cost_per_item.

## Pushed to github before adding CRUD endpoints for Bought and Sold.