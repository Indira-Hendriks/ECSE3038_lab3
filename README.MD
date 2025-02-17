The attached app.py file contains a code who's main goal is demonstrate the use of POST, GET, GET {id}, PATCH{id} and DELETE{id} request handlers in fastAPI in python.

***POST /tank :

    Description: 
    Creates a new tank entry with a uniquely generated ID, location, latitude, and longitude.

     Expected Results:

        Example Request #1: 

         POST/tank
         {
            {
            "location":"Chemistry Department" ,
            "lat": 26.262525,
            "long": 262.3833333333338373
            }
         }

        Expected Response:

        {
            "success": true,
            "result": {
                "id": "0f34995e-4ee8-4cce-9636-52110ea4bacd",
                "location": "Chemistry Department",
                "lat": 26.262525,
                "long": 262.38333333333384
            }
        }

    Example Request #2: 

         POST/tank
         {
            {
            "location":" " ,
            "lat": 26.262525,
            "long": 262.3833333333338373
            }
         }

    Expected Response:

        {
            "detail": "400: Invalid request: Missing required fields"
        }
  
***GET /tank :

Description:

Retrieves a list of all stored tanks.

    Expected Results:

        Example Request: 

        POST/tank

        Expected Response:

        [
            {
                "id": "0f34995e-4ee8-4cce-9636-52110ea4bacd",
                "location": "Chemistry Department",
                "lat": 26.262525,
                "long": 262.38333333333384
            },
            {
                "id": "c8944b35-825c-4eae-b6a7-52c947829edf",
                "location": "Engineering Department",
                "lat": 26.2525,
                "long": 19.383333333333837
            },
            {
                "id": "736687e7-74a9-471a-b0e1-ed38644f84d7",
                "location": "Art Department",
                "lat": 26.2525,
                "long": 50.38373
            }
            {
                "id": "e6c12463-34e5-4912-acaa-d60edfa36ec9",
                "location": "Physics department",
                "lat": 18.004741066082236,
                "long": 76.74875280426826
            }
        ]

***GET /tank/{id} :

Description:

Retrieves details of a specific tank using its ID

    Expected Results:

            Example Request#1: 

            GET/tank/{c8944b35-825c-4eae-b6a7-52c947829edf}

            Expected Response:

            {
                "id": "c8944b35-825c-4eae-b6a7-52c947829edf",
                "location": "Engineering Department",
                "lat": 26.2525,
                "long": 19.383333333333837
            }

            Example Request#2: 

            GET/tank/{736687e7-74a9-471a-b0e1-ed38644f84d8}

            Expected Response:

                {
                  "detail": "Tank not found"
                }

***PATCH /tank/{id} :

Description: 

Updates an existing tank entry with new data while keeping the original fields intact.

Expected Results:

        Example Request #1: 

         PATCH/tank{0f34995e-4ee8-4cce-9636-52110ea4bacd}

        {
        "location":"Old Chemistry Department" ,
        }

        Expexted Response:

        {
            "id": "0f34995e-4ee8-4cce-9636-52110ea4bacd",
            "location": "Old Chemistry Department",
            "lat": 26.262525,
            "long": 262.38333333333384
        }
    In the terminal: "PATCH /tank/%7Be6c12463-34e5-4912-acaa-d60edfa36ec9%7D HTTP/1.1" 200 OK

***DELETE /tank{id} :

Description: 

Deletes a specific tank entry based on ID entered.

    Example Request:

    DELETE/tank{e6c12463-34e5-4912-acaa-d60edfa36ec9}

    Expected Response:

    In the terminal: "DELETE /tank/%7Be6c12463-34e5-4912-acaa-d60edfa36ec9%7D HTTP/1.1" 204 No Content

***Two truths and a lie :

    1. My ex-neighbors stole 2 tanks from my house and used them to water an "illegal farm".
    2. My ex-neighbors made all the dogs in my neighborhood (including mine) "disappear".
    3. My ex-neighbors stole the awnings from my house and then attached them to the side their house that was facing mine. 