# ItinGen

ItinGen is a web based application that allows users to randomly
generate optimized itineraries for their schedules to explore a new city
or rediscover a city they have been living in for years

Table of Contents

[TOC]

## Setup

https://gorails.com/setup/osx/10.14-mojave
Currently setup with Postgres as the DataBase.

### Initializing the app
```bash
bundle install
rake db:setup
rails s
```

## Running Unit Tests
Unit Tests for the Data Aggregation scripts and instructions on how to use them will be found in the `activities_data` directory.

To run tests for the application, simply run:
```bash
rspec
```
These tests will test to make sure that all of the front-end objects are
displaying on the home page properly and as are intended.:w


## Who Did What:
### Back-end
Omar and Anthony wrote the back-end together. They implemented a seeds
file to make sure that the JSON data that the Data Aggregation Team
extracted was populating the database. They also redeveloped the
application to utilize PosgreSQL instead of MongoDB. Additionally,
established the route and testing suite, wrote DB migrations, model
validations, and implemented controller logic.

### Front-end

## Changes:
We decided to switch the application from using MongoDB to Postgresql.
We were having issues with MongoDB working properly with the Rails
application and so we switched it out for Postgres.
