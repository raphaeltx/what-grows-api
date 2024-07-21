# What Grows API 🍊🍋🍠🍅

Get suggestions of what vegetables grow and the recommended soil humidity given your location!

## Endpoint: It Grows

**Purpose:**  
This endpoint returns a list of vegetables and the soil humidity percentage given your location and the current date.

### **URL**

`POST /it-grows`

### **Body**

```
{
  "latitude": <latitude value>,
  "longitude": <longitude value>
}
```

### Response example

```
[
    {
        "name": "Lettuce",
        "soil_humidity": 60
    },
    {
        "name": "Spinach",
        "soil_humidity": 65
    },
    {
        "name": "Carrot",
        "soil_humidity": 70
    },
    {
        "name": "Bell Pepper",
        "soil_humidity": 75
    },
    {
        "name": "Green Beans",
        "soil_humidity": 80
    }
]
```

## How to run locally

Make sure you have python3 installed. Create a Virtual Environment:

```
python -m venv venv
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the following command at the root of the project: 

```
fastapi dev main.py
```

You can also with docker compose. Make sure you have docker and docker compose installed.
Run the following command in the root directory:

```
    docker-compose up --build
```

### You can access the endpoint by the URL http://localhost:8000