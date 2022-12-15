# restautant_menu

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

how to get Token Obtain Pair:
go to link, enter your name/passsword:
http://127.0.0.1:3000/api/v1/token/
get access token, enter it to header-> Authorization: Bearer HEADER.PAYLOAD:DATA/VERIFY SIGNATURE: