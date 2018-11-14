# ItinGen

ItinGen is a web based application that allows users to randomly
generate optimized itineraries for their schedules to explore a new city
or rediscover a city they have been living in for years

**Table of Contents**

[TOC]

##Setup
https://gorails.com/setup/osx/10.14-mojave
Currently setup with Postgres as the DataBase.
###Initializing the app
```bash
bundle install
rake db:setup
rails s
```
##Running Unit Tests
Unit Tests for the Data Aggregation scripts will be found in the `activities_data` directory
To run tests for the application, simply run:
```bash
rspec
```
