# Goal

Build an API endpoint for storing a timestamp and a message within a database.

## Tech Stack
- DjangoRestFramwork
- SQLite


## Run (Linux)
Clone this repository:
```git clone https://github.com/IsmailBiswas/remind_me_later```

Create a Python virtual environment, activate it and install the requirments

```
python -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt
  
```

Migrate the DB
```
./manage.py migrate
  
```

Run the development server
```
./manage.py runserver
  
```

## Manual Test

Visit `http://localhost:8000/reminders/` there you will be able to test this API. 


Or Use **curl** to test this API

**POST**

```
curl -X POST "http://localhost:8000/reminders/" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello World",
    "trigger_time": "2025-05-30T16:58:00Z"
  }'
  
```

**GET**: All reminders

```
curl -X GET "http://localhost:8000/reminders/"   -H "Content-Type: application/json"
```

**GET**: Retrieve a specific reminder using its unique identifier (e.g., id 1)

```
curl -X GET "http://localhost:8000/reminders/1/"   -H "Content-Type: application/json"
```

**PUT**
```
curl -X PUT "http://localhost:8000/reminders/1/" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Updated message",
    "trigger_time": "2025-05-30T16:58:00Z"
  }'
  
```

**DELETE**

```
curl -X DELETE "http://localhost:8000/reminders/1/"   -H "Content-Type: application/json"
  
```
