Ride My Way Api

Ride-my App is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers

Motivation

Ride My Way focuses on reducing carbon emission, traffic jam by allowing people to share a ride and reduce the cost and hustle of driving

**Code style**_
The user interface was build using css javascript and HTML The api was build using python

Installation

Clone the repo to your local machine install a virtual enviroment install the dependacies from terminal run manage.py test the endpoint using postman

Features

Users can create an account and log in. Drivers can add ride offers.. Passengers can view all available ride offers. Passengers can see the details of a ride offer and request to join the ride. E.g What time the ride leaves, where it is headed e.t.c Drivers can view the requests to the ride offer they created. Drivers can either accept or reject a ride request.

Tests

The test were carried out from the unittest library. for python version 3.5 and below use py.test to run yur test for python version 3.5 and above use pytest to run your test

EndPoint	Functionality

POST /auth/signup	Register a user

POST /auth/signin	Login a user

GET /rides/	Get all the ride offers

GET /rides/Id/	Get a ride single by id

POST /rides/	Add a ride offer

PUT /rides/Id/	Update the information of a ride offer

DELETE /rides/Id/	Remove a offer offer

GET /rides/id/requets/	Get the ride requests for a given ride

POST /rides/id/requets/	Create a ride request for a given ride

DELETE /requets/id	Delete a ride request

Authors

Kwame Asiago

[![Build Status](https://travis-ci.org/SelaDanti/RideMyWay2.0.svg?branch=ft-signup-158949454)](https://travis-ci.org/SelaDanti/RideMyWay2.0)

[![Coverage Status](https://coveralls.io/repos/github/SelaDanti/RideMyWay2.0/badge.png?branch=ft-signup-158949454)](https://coveralls.io/github/SelaDanti/RideMyWay2.0?branch=ft-signup-158949454)
