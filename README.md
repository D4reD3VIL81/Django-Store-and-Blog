# Django Store and Blog
A basic Django ecommerce website using Django ORM, Django Template Language, HTML, CSS, Js and JQuery.

## Project Summary

The website displays products. Users can add and remove products to/from their cart while also specifying the quantity of each item. They can then enter their address and choose Stripe to handle the payment processing.

## Running this project
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with
```shell
pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project
```shell
virtualenv env
```
That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:
```shell
source env/bin/active
```
Then install the project dependencies with
```shell
pip install -r requirements.txt
```
Now you can run the project with this command
```shell
python manage.py runserver
```
