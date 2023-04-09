# Restautant_menu Test Task
[![version](https://img.shields.io/badge/python-3.10-green)](https://semver.org)
[![version](https://img.shields.io/badge/Django_Rest_Framework-latest-green)](https://semver.org)
[![version](https://img.shields.io/badge/unittest-latest-green)](https://semver.org)
[![version](https://img.shields.io/badge/flake8-6.0.0-green)](https://semver.org)

http://78.27.236.114:8000/  <-deployed here

###  [Swagger documentation](http://78.27.236.114:8000/swagger/)
### [Postman documentation](https://documenter.getpostman.com/view/23239505/2s8YzZPJoS)

http://78.27.236.114:8000/api-auth/login/


## API FUNCTIONALITY:
- Authentication
- Creating restaurant
- Uploading menu for restaurant (There should be a menu for each day)
- Creating employee
- Getting current day menu
- Getting results for the current day

#### Availible ROLEs for Users and permissions:
* 0 - 'employee' - no access to create users, create order
* 1 - 'restaurant' (superuser) - create employee, create menu

### How to use API:
##### [URL to Get Token Obtain Pair](http://78.27.236.114:8000/api/v1/token/) - (Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.)

#### Test Users Credentials:
* Email address: restaurant1@mail.ua
* Password: admin

Get access token, enter it to header-> Authorization: Bearer HEADER.PAYLOAD:DATA/VERIFY SIGNATURE:

GET all week menu (permission: Admin or Restaurant):
**/api/v1/menu_all_week/**

GET today menu (permission: IsAuthenticated):
**/api/v1/menu_for_today/**

### Start app in docker:
```shell
docker compose up --build & 
docker exec -it app_restaurant bash
docker exec -it app_restaurant python manage.py createsuperuser
```



### How run tests:
```shell
pytest Tests/test_create_employee.py
```

start flake8:
```shell
flake8 api/views.py     # check one file
flake8 flake8 app_restaurant/  # check all folder
flake8 path/to/code/to/check.py
```
