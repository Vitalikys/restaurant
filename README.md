# restautant_menu
http://78.27.236.114:8000/  <-deployed

http://127.0.0.1:3000/api-auth/login/


API FUNCTIONALITY:
- Authentication
- Creating restaurant
- Uploading menu for restaurant (There should be a menu for each day)
- Creating employee
- Getting current day menu
- Getting results for the current day

ROLE Users and permissions:
    0 - 'employee' - no access to create users, create order
    1 - 'restaurant' (superuser) - create employee, create menu

we can't create admin(restaurant) from API, we should use createsuperuser:


how to get Token Obtain Pair:
Go to link, enter your name/passsword:
http://127.0.0.1:3000/api/v1/token/
get access token, enter it to header-> Authorization: Bearer HEADER.PAYLOAD:DATA/VERIFY SIGNATURE:

GET all week menu (permission: Admin or Restaurant):
**/api/v1/menu_all_week/**

GET today menu (permission: IsAuthenticated):
**/api/v1/menu_for_today/**

start app in docker:
$ docker compose up --build & 
$ docker exec -it app_restaurant bash
$ docker exec -it app_restaurant python manage.py createsuperuser


run tests:
$ pytest Tests/tests.py

add flake8, RUN: flake8 path/to/code/to/check.py