# moveeasy
Address Management Service Demo

This demo contains 2 REST URL's to add new address and fetch existing address

After Coloning the project, exec command "python moveesy_service/manage.py migrate"

FETCH ADDRESS -

Get Address URL (GET Request):-

localhost:8000/address/<page_no>
eg:- http://localhost:8000/address/1/

CREATE ADDRESS -

localhost:8000/create/address/
eg:- http://127.0.0.1:8000/create/address/

sample body:-
{
    "username": "admin",
    "address": "Venlo",
    "available_from": "20181120 00:08:00",
    "available_to": "20181120 00:17:00"
}
