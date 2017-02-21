# ReimbursementApp

This application contains only the backend. 
The application consists of APIs for getting the list of all the reimbursement submitted by a user, create a reimbursement, view details of a specific reimbursement claimed by the user and get a list of all the pending reimbursements.

A superuser can see the details of all users.

Create superuser from : `python manage.py createsuperuser`

Add users from `http://localhost:8000/admin/` (login through superuser)

<br>
<h3><b> API Documentation </b></h3>

<b>Generate Auth Token</b>

Http POST to http://localhost:8000/app/api-auth-token/

POST body
```
{
"username": "user1"
"password": "passworduser1"
}
```
Response
```
{
  "token": "9128a7f6f19c444f1719ff877d82c55e819e2138"
}
```

<b>Reimbursement</b>

Http GET to  http://localhost:8000/app/v1/reimbursement/
Header
```
Authorization : Token 9128a7f6f19c444f1719ff877d82c55e819
```

Response
```
{
  "total_reimbursement": 37.5,
  "details": [
    {
      "id": 1,
      "amount": 12.5,
      "description": "Petrol",
      "attachment": "/media/user_2/25.jpg",
      "reimbursed_flag": true,
      "date_created": "2017-02-19T06:34:21.822000Z"
    },
    {
      "id": 2,
      "amount": 25,
      "description": "Team Lunch",
      "attachment": "/media/user_2/TestImageFile.jpg",
      "reimbursed_flag": false,
      "date_created": "2017-02-19T10:35:55.291000Z"
    }
  ],
  "total_pending": 1
}
```

<b>Create Reimbursement</b> <br>
Http POST to  http://localhost:8000/app/v1/reimbursement/

POST body
```
Header- 
Authorization : Token 9128a7f6f19c444f1719ff877d82c55e819

===========================================================

Body- (form-data)

amount: 25
description: Food
attachement: <<choose file>>
```

Response
```
{
  "amount": 25,
  "description": "Food",
  "attachment": "/media/user_2/image_uploaded_from_ios.jpg"
}
```

<b>Get details of specific Reimbursement</b><br>
Http GET to  http://localhost:8000/app/v1/reimbursement/id/

Header
```
Authorization : Token 9128a7f6f19c444f1719ff877d82c55e819
```

Response
```
{
  "id": 2,
  "amount": 25,
  "description": "Team Lunch",
  "attachment": "/media/user_2/TestImageFile.jpg",
  "reimbursed_flag": false,
  "date_created": "2017-02-19T10:35:55.291000Z"
}
```

<b>Pending reimbursement</b> <br>
Http GET to http://localhost:8000/app/v1/pending/

Header
```
Authorization : Token 9128a7f6f19c444f1719ff877d82c55e819
```

Response
```
{
  "total_pending_reimbursement": 91,
  "total_pending": 4
}
```
