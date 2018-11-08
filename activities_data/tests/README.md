# Activity Tests

This directory contains all of the scripts that run tests on our
data pipeline scripts to ensure data integrity and so that bad
pipelines do not break our database.

## Running Tests

Most of the tests are not run individually to check data validity. Tests are
integrated into implementation and are running constantly as we make API calls.
Tests are run to make sure that after every call and after processing our
data is still valid and is properly formatted for entry into our database.
