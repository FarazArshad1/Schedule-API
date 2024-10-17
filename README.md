# Weekly Schedule Management API

This project is a simple Django application that implements a CRUD API (Create, Read, Update, and Delete) for managing a weekly schedule. Each day of the week has associated time slots, with a list of IDs for each interval. The API includes **Swagger documentation** and **Basic Authentication** for secure access.

## Features

- **CRUD API** for managing time slots for each day of the week.
- **Swagger UI** for API documentation and testing.
- **Basic Authentication** to secure the API endpoints.
  
## API Endpoints

### Time Slot Management Endpoints

All time slot-related API endpoints require authentication.

1. **Get all time slots**
   - **URL**: `/api/timeslots/`
   - **Method**: `GET`
   - **Description**: Retrieve a list of all time slots.
   - **Authentication**: Required

2. **Create a new time slot**
   - **URL**: `/api/timeslots/`
   - **Method**: `POST`
   - **Description**: Create a new time slot for a specific day.
   - **Authentication**: Required
   - **Sample Request Body**:
   ```json
   {
     "day_of_week": "monday",
     "start_time": "08:00:00",
     "stop_time": "10:00:00",
     "ids": [1, 2]
   }
   ```

3. **Get a single time slot by ID**
   - **URL**: `/api/timeslots/{id}/`
   - **Method**: `GET`
   - **Description**: Retrieve a time slot by its ID.
   - **Authentication**: Required

4. **Update a time slot**
   - **URL**: `/api/timeslots/{id}/`
   - **Method**: `PUT`
   - **Description**: Update an existing time slot by ID.
   - **Authentication**: Required
   - **Sample Request Body**:
   ```json
   {
     "day_of_week": "tuesday",
     "start_time": "09:00:00",
     "stop_time": "11:00:00",
     "ids": [3, 4]
   }
   ```

5. **Delete a time slot**
   - **URL**: `/api/timeslots/{id}/`
   - **Method**: `DELETE`
   - **Description**: Delete a time slot by ID.
   - **Authentication**: Required

### Swagger Documentation

- **URL**: `/swagger/`
- **Method**: `GET`
- **Description**: Access Swagger UI for interactive API documentation and testing.

### Authentication

The API is protected by **Basic Authentication**, so you need to provide your username and password to access any of the endpoints.

#### Example using `curl`:
```bash
curl -u username:password http://localhost:8000/api/timeslots/
```

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x
- Django REST Framework
- `drf-yasg` (for Swagger documentation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weekly-schedule-api.git
   cd weekly-schedule-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin and API access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Accessing the API

- Visit `http://localhost:8000/swagger/` to explore the API using Swagger UI.
- Use `http://localhost:8000/api/timeslots/` to interact with the time slot API.

### Project Structure

```
schedule_project/
│
├── schedule/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py           
│   ├── serializers.py      
│   ├── views.py            
│   ├── urls.py             
│
├── schedule_project/
│   ├── __init__.py
│   ├── settings.py         
│   ├── urls.py             
│
├── manage.py               
├── requirements.txt        
```

## Testing the API

You can test the API via Swagger or using tools like Postman, `curl`, or any HTTP client.



